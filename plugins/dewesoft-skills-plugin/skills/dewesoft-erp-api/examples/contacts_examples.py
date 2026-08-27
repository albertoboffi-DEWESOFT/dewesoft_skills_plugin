#!/usr/bin/env python3
"""
Worked examples for the Contacts group (Dewesoft ERP API v1).

Prerequisites — export your credentials first (never hard-code them):

    export DEWESOFT_ERP_BASE_URL=https://erpapi-it-erp.dewesoft.com
    export DEWESOFT_ERP_USERNAME=you@dewesoft.com
    export DEWESOFT_ERP_PASSWORD=********
    export DEWESOFT_ERP_CLIENT_ID=...
    export DEWESOFT_ERP_CLIENT_SECRET=...

Then:  python examples/contacts_examples.py

Contacts routes (from api_data.js, group Contacts):
    GET    /v1/contacts          IndexContact   (paginated)
    GET    /v1/contacts/all      GetAllContact
    GET    /v1/contacts/{id}     GetContact
    POST   /v1/contacts          CreateContact
    PATCH  /v1/contacts/{id}     UpdateContact
    DELETE /v1/contacts/{id}     DeleteContact

Create/Update body fields: first_name (req), last_name (req), email (req),
country_id (req, exists:countries,id), company (opt), phone (opt, max:25),
support_type (opt), content (opt).
"""

import os
import sys

# make ../scripts importable when run from the skill folder
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from dewesoft_erp import DewesoftERP, DewesoftERPError  # noqa: E402


def main() -> int:
    erp = DewesoftERP()  # reads config from environment

    # 0) confirm auth works
    info = erp.authenticate()
    print(f"Authenticated ({info.get('token_type')}), "
          f"refresh_token={'yes' if info.get('refresh_token') else 'no'}")

    # 1) first page of contacts, 10 per page, newest-ish ordering
    page = erp.index("contacts", limit=10, page=1,
                     order_by="last_name", sorted_by="asc")
    pag = page.get("meta", {}).get("pagination", {})
    print(f"\nContacts: {pag.get('total', '?')} total, "
          f"{pag.get('total_pages', '?')} pages")
    for c in page.get("data", []):
        print(f"  #{c.get('id')}  {c.get('first_name','')} {c.get('last_name','')}"
              f"  <{c.get('email','')}>")

    # 2) iterate every contact across all pages (lazy)
    count = sum(1 for _ in erp.iterate("contacts", page_size=100))
    print(f"\nIterated {count} contacts across all pages")

    # 3) read a single contact by id
    # one = erp.get("contacts", 1)
    # print(one)

    # 4) create a contact  (uncomment to run — this writes data)
    # created = erp.create("contacts", {
    #     "first_name": "Mario",
    #     "last_name": "Rossi",
    #     "email": "mario.rossi@example.com",
    #     "country_id": 1,            # must exist in /v1/countries
    #     "company": "Acme S.p.A.",
    #     "phone": "+39 02 1234567",
    # })
    # print("created:", created)

    # 5) update + delete  (uncomment to run)
    # erp.update("contacts", created["id"], {"phone": "+39 02 7654321"})
    # erp.delete("contacts", created["id"])

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except DewesoftERPError as exc:
        print(f"API error {exc.status}: {exc}", file=sys.stderr)
        if exc.body:
            print(exc.body, file=sys.stderr)
        raise SystemExit(1)
