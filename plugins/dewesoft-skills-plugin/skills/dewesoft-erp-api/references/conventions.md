# Conventions — base URLs, response shape, CRUD pattern, query criteria

> Sources: the response envelope and route shapes below are taken from the
> apiDoc spec `api_data.js` (every `Index*` example + the repeated CRUD groups).
> The request-criteria parameter **names** (filter/sort/search/include) are the
> Apiato framework standard and are **NOT enumerated in `api_data.js`** — they
> are documented on the spec's general page (`#api-_`). Treat the criteria
> section below as "to verify against `#api-_`" and prefer pass-through (`extra=`)
> for anything unconfirmed. Do not present unverified parameter names as fact.

## Base URL (per region)

| region   | base URL                                    | status    |
|----------|---------------------------------------------|-----------|
| Italy    | `https://erpapi-it-erp.dewesoft.com`        | confirmed |
| central  | `https://erpapi-central.dewesoft.com`       | docs host |
| other    | `https://erpapi-{cc}-erp.dewesoft.com`      | inferred pattern — verify |

All endpoint paths are versioned under `/v1/...`.

## Response envelope

**Single resource** (`GET /v1/<r>/{id}`, create, update): a bare JSON object.

**Paginated list** (`GET /v1/<r>`):

```json
{
  "data": [ /* array of resource objects */ ],
  "include": [ /* related resources, when requested */ ],
  "custom": [],
  "meta": {
    "pagination": {
      "total": 0, "count": 0, "per_page": 0,
      "current_page": 0, "total_pages": 0, "links": []
    }
  }
}
```

Use `meta.pagination.total_pages` to drive paging (the client's `iterate()`
does this automatically).

**Unpaginated list** (`GET /v1/<r>/all`): the full collection without the
`meta.pagination` block.

## Universal six-route CRUD pattern

Most resources expose the same six routes (`<r>` = the resource segment, e.g.
`contacts`, `partners`, `order-sales`, `work-orders`):

| operation        | method + path                |
|------------------|------------------------------|
| list (paginated) | `GET /v1/<r>`                |
| list (all)       | `GET /v1/<r>/all`            |
| read one         | `GET /v1/<r>/{id}`           |
| create           | `POST /v1/<r>`               |
| update           | `PATCH /v1/<r>/{id}`         |
| delete           | `DELETE /v1/<r>/{id}`        |

Resources with extra/non-CRUD actions (e.g. Work_Orders, Production,
Statistic, Timeline) are listed in `endpoints.md`; per-endpoint body
parameters are in `endpoints.json`.

## Request criteria (Apiato standard — verify against `#api-_`)

Applied as query-string parameters on list/read endpoints:

| param          | purpose                                  | example                          |
|----------------|------------------------------------------|----------------------------------|
| `include`      | embed related resources                  | `include=country,tags`           |
| `filter`       | sparse fieldset (limit returned fields)  | `filter=id;first_name;email`     |
| `search`       | search by field:value pairs              | `search=first_name:Mario`        |
| `searchFields` | search operator per field                | `searchFields=first_name:like`   |
| `orderBy`      | sort field                               | `orderBy=last_name`              |
| `sortedBy`     | sort direction                           | `sortedBy=asc` / `desc`          |
| `page`         | page number                              | `page=2`                         |
| `limit`        | items per page                           | `limit=50`                       |

The client builds these via `DewesoftERP.criteria(...)`; anything not listed
here can be passed verbatim with `criteria(extra={...})`.

## Errors

Non-2xx responses raise `DewesoftERPError(status, message, body)`. A `401`
triggers one automatic re-authentication + retry inside `request()`.
