#!/usr/bin/env python3
"""
Dewesoft ERP / CRM API client (API v1) — dependency-free (Python stdlib only).

A thin wrapper over the Dewesoft ERP REST API that handles:
  - OAuth2 authentication (password grant or client-credentials grant)
  - automatic Bearer-token injection + one transparent retry on 401
  - the universal six-route CRUD pattern (index / all / get / create / update / delete)
  - pagination (the `data` + `meta.pagination` envelope) via iterate()
  - request-criteria query building (include / filter / search / orderBy / sortedBy / page / limit)

Configuration is read from environment variables — NEVER hard-code secrets:

    DEWESOFT_ERP_BASE_URL      e.g. https://erpapi-it-erp.dewesoft.com     (preferred)
    DEWESOFT_ERP_REGION        e.g. it   -> https://erpapi-{region}-erp.dewesoft.com
    DEWESOFT_ERP_USERNAME      user email           (password grant)
    DEWESOFT_ERP_PASSWORD      user password        (password grant)
    DEWESOFT_ERP_CLIENT_ID     OAuth client id      (create a Client in the ERP web app)
    DEWESOFT_ERP_CLIENT_SECRET OAuth client secret
    DEWESOFT_ERP_GRANT         'password' (default) or 'client_credentials'
    DEWESOFT_ERP_SCOPE         optional (usually empty)

Source of API shape: apiDoc spec `api_data.js`, groups OAuth2 / Contacts / *.
  - POST   /v1/oauth/token   (login: password or client_credentials grant)
  - DELETE /v1/logout        (revoke the access token)
  - <resource> CRUD:  GET /v1/<r>  ·  GET /v1/<r>/all  ·  GET /v1/<r>/{id}
                      POST /v1/<r>  ·  PATCH /v1/<r>/{id}  ·  DELETE /v1/<r>/{id}

NOTE on query criteria: the filter/sort/search parameter *names* are the standard
Apiato request-criteria vocabulary (this API is built on Apiato/Laravel). They are
NOT enumerated inside api_data.js — confirm them against the documentation's
general page (`#api-_`). Until confirmed, pass anything verbatim via `extra=`.
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, Iterator, List, Optional, Union

REGION_HOST_TEMPLATE = "https://erpapi-{region}-erp.dewesoft.com"  # IT confirmed; pattern inferred
TOKEN_PATH = "/v1/oauth/token"
LOGOUT_PATH = "/v1/logout"


class DewesoftERPError(RuntimeError):
    """Raised for any non-2xx response or connection failure."""

    def __init__(self, status: int, message: str, body: Any = None):
        super().__init__(f"[{status}] {message}")
        self.status = status
        self.body = body


def _resolve_base_url(explicit: Optional[str] = None) -> str:
    base = explicit or os.environ.get("DEWESOFT_ERP_BASE_URL")
    if base:
        return base.rstrip("/")
    region = os.environ.get("DEWESOFT_ERP_REGION")
    if region:
        return REGION_HOST_TEMPLATE.format(region=region.strip().lower()).rstrip("/")
    raise DewesoftERPError(0, "Set DEWESOFT_ERP_BASE_URL (e.g. https://erpapi-it-erp.dewesoft.com) "
                              "or DEWESOFT_ERP_REGION (e.g. it).")


class DewesoftERP:
    def __init__(
        self,
        base_url: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant: Optional[str] = None,
        scope: Optional[str] = None,
        timeout: int = 30,
    ):
        self.base_url = _resolve_base_url(base_url)
        self.username = username or os.environ.get("DEWESOFT_ERP_USERNAME")
        self.password = password or os.environ.get("DEWESOFT_ERP_PASSWORD")
        self.client_id = client_id or os.environ.get("DEWESOFT_ERP_CLIENT_ID")
        self.client_secret = client_secret or os.environ.get("DEWESOFT_ERP_CLIENT_SECRET")
        self.grant = (grant or os.environ.get("DEWESOFT_ERP_GRANT") or "password").lower()
        self.scope = scope if scope is not None else os.environ.get("DEWESOFT_ERP_SCOPE", "")
        self.timeout = timeout
        self._access_token: Optional[str] = None
        self._refresh_token: Optional[str] = None
        self._expires_at: float = 0.0

    # ------------------------------------------------------------------ HTTP
    def _http(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Dict[str, Any]] = None,
        body: Optional[Any] = None,
        form: Optional[Dict[str, Any]] = None,
        auth: bool = True,
    ):
        url = self.base_url + path
        if query:
            url += "?" + urllib.parse.urlencode(query, doseq=True)

        data: Optional[bytes] = None
        headers: Dict[str, str] = {"Accept": "application/json"}
        if form is not None:
            data = urllib.parse.urlencode(form).encode("utf-8")
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        elif body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"
        if auth:
            headers["Authorization"] = "Bearer " + self.token()

        req = urllib.request.Request(url, data=data, method=method.upper(), headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                raw = resp.read().decode("utf-8", "replace")
                return resp.status, (json.loads(raw) if raw.strip() else None)
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8", "replace")
            try:
                parsed = json.loads(raw)
            except Exception:
                parsed = raw
            raise DewesoftERPError(exc.code, exc.reason, parsed)
        except urllib.error.URLError as exc:
            raise DewesoftERPError(0, f"connection error: {exc.reason}")

    # ------------------------------------------------------------------ auth
    def authenticate(self) -> Dict[str, Any]:
        """Acquire an access token via the configured grant. Caches it in memory."""
        if self.grant == "client_credentials":
            form = {
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "scope": self.scope,
            }
        else:  # password grant (first-party)
            form = {
                "grant_type": "password",
                "username": self.username,
                "password": self.password,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "scope": self.scope,
            }
        _, payload = self._http("POST", TOKEN_PATH, form=form, auth=False)
        self._access_token = payload["access_token"]
        self._refresh_token = payload.get("refresh_token")
        # refresh 60s before stated expiry; expires_in is very long (~10y) for this API
        self._expires_at = time.time() + float(payload.get("expires_in", 3600)) - 60
        return payload

    def token(self) -> str:
        if not self._access_token or time.time() >= self._expires_at:
            self.authenticate()
        return self._access_token  # type: ignore[return-value]

    def logout(self) -> None:
        """Revoke the current access token (DELETE /v1/logout)."""
        if self._access_token:
            self._http("DELETE", LOGOUT_PATH)
            self._access_token = None
            self._refresh_token = None
            self._expires_at = 0.0

    # --------------------------------------------------------------- request
    def request(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Dict[str, Any]] = None,
        body: Optional[Any] = None,
    ) -> Any:
        """Authenticated request with one transparent retry if the token is rejected."""
        try:
            _, payload = self._http(method, path, query=query, body=body)
        except DewesoftERPError as exc:
            if exc.status == 401:
                self._access_token = None  # force re-auth and retry once
                _, payload = self._http(method, path, query=query, body=body)
            else:
                raise
        return payload

    # ------------------------------------------------- request-criteria query
    @staticmethod
    def criteria(
        *,
        include: Optional[Union[str, List[str]]] = None,
        filter: Optional[Union[str, List[str]]] = None,
        search: Optional[str] = None,
        search_fields: Optional[str] = None,
        order_by: Optional[str] = None,
        sorted_by: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Build a query dict from Apiato request criteria. `extra` passes through
        any additional/raw params verbatim (use it for anything not yet confirmed)."""
        q: Dict[str, Any] = {}
        if include:
            q["include"] = include if isinstance(include, str) else ",".join(include)
        if filter:
            q["filter"] = filter if isinstance(filter, str) else ";".join(filter)
        if search is not None:
            q["search"] = search
        if search_fields:
            q["searchFields"] = search_fields
        if order_by:
            q["orderBy"] = order_by
        if sorted_by:
            q["sortedBy"] = sorted_by
        if page is not None:
            q["page"] = page
        if limit is not None:
            q["limit"] = limit
        if extra:
            q.update(extra)
        return q

    # --------------------------------------------- universal six-route CRUD
    def index(self, resource: str, **crit) -> Any:
        """GET /v1/<resource> — paginated list (data + meta.pagination envelope)."""
        return self.request("GET", f"/v1/{resource}", query=self.criteria(**crit))

    def all(self, resource: str, **crit) -> Any:
        """GET /v1/<resource>/all — unpaginated list."""
        return self.request("GET", f"/v1/{resource}/all", query=self.criteria(**crit))

    def get(self, resource: str, id: Union[str, int], **crit) -> Any:
        """GET /v1/<resource>/<id> — single resource."""
        return self.request("GET", f"/v1/{resource}/{id}", query=self.criteria(**crit))

    def create(self, resource: str, data: Dict[str, Any]) -> Any:
        """POST /v1/<resource> — create."""
        return self.request("POST", f"/v1/{resource}", body=data)

    def update(self, resource: str, id: Union[str, int], data: Dict[str, Any]) -> Any:
        """PATCH /v1/<resource>/<id> — partial update."""
        return self.request("PATCH", f"/v1/{resource}/{id}", body=data)

    def delete(self, resource: str, id: Union[str, int]) -> Any:
        """DELETE /v1/<resource>/<id> — delete."""
        return self.request("DELETE", f"/v1/{resource}/{id}")

    # ------------------------------------------------------------ pagination
    def iterate(
        self,
        resource: str,
        *,
        page_size: int = 50,
        max_pages: Optional[int] = None,
        **crit,
    ) -> Iterator[Dict[str, Any]]:
        """Yield every item across all pages of a paginated index endpoint."""
        page = 1
        while True:
            payload = self.index(resource, page=page, limit=page_size, **crit)
            items = payload.get("data", []) if isinstance(payload, dict) else []
            for item in items:
                yield item
            if not items:
                break
            meta = (payload or {}).get("meta", {}).get("pagination", {})
            total_pages = meta.get("total_pages")
            if total_pages and page >= total_pages:
                break
            if max_pages and page >= max_pages:
                break
            page += 1


# ---------------------------------------------------------------------- CLI
def _main(argv: Optional[List[str]] = None) -> int:
    import argparse

    p = argparse.ArgumentParser(prog="dewesoft_erp",
                                description="Dewesoft ERP API client (v1)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("auth-test", help="acquire a token and print confirmation")

    g = sub.add_parser("get", help="GET an arbitrary path, e.g. /v1/contacts/1")
    g.add_argument("path")

    li = sub.add_parser("list", help="paginated index of a resource, e.g. contacts")
    li.add_argument("resource")
    li.add_argument("--limit", type=int, default=10)
    li.add_argument("--page", type=int, default=1)
    li.add_argument("--include", default=None)
    li.add_argument("--search", default=None)
    li.add_argument("--order-by", default=None)
    li.add_argument("--sorted-by", default=None)

    a = sub.add_parser("all", help="unpaginated /all of a resource")
    a.add_argument("resource")

    args = p.parse_args(argv)
    client = DewesoftERP()

    if args.cmd == "auth-test":
        payload = client.authenticate()
        tok = payload.get("access_token", "")
        print(f"OK — {payload.get('token_type', 'Bearer')} token acquired "
              f"({len(tok)} chars), expires_in={payload.get('expires_in')}, "
              f"refresh_token={'yes' if payload.get('refresh_token') else 'no'}")
    elif args.cmd == "get":
        print(json.dumps(client.request("GET", args.path), indent=2, ensure_ascii=False))
    elif args.cmd == "list":
        payload = client.index(
            args.resource, limit=args.limit, page=args.page,
            include=args.include, search=args.search,
            order_by=args.order_by, sorted_by=args.sorted_by,
        )
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    elif args.cmd == "all":
        print(json.dumps(client.all(args.resource), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
