# Authentication — OAuth2 (API v1)

> Source: apiDoc spec `api_data.js`, group **OAuth2**. Token endpoint and field
> names are taken verbatim from the spec; do not invent additional fields.

All data endpoints require a Bearer access token. There are two grants.

## Password grant (first-party — the default for internal tools)

`POST /v1/oauth/token`

Body parameters (sent as `application/x-www-form-urlencoded`):

| field           | required | notes                                   |
|-----------------|----------|-----------------------------------------|
| `grant_type`    | yes      | must be `password`                      |
| `username`      | yes      | user **email**                          |
| `password`      | yes      | user password                           |
| `client_id`     | yes      | from a Client created in the ERP web app|
| `client_secret` | yes      | from the same Client                    |
| `scope`         | no       | usually empty                           |

Success response:

```json
{
  "token_type": "Bearer",
  "expires_in": 315360000,
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbG...",
  "refresh_token": "Oukd61zgKzt8TBwRjnasd..."
}
```

`expires_in` is effectively long-lived (~10 years). A `refresh_token` is issued
only by the password grant.

## Client-credentials grant (third-party clients)

`POST /v1/oauth/token` with `grant_type=client_credentials`, `client_id`,
`client_secret`, optional `scope`. **No** `refresh_token` is returned.

> The description in the spec states: *"You must have client ID and secret first.
> You can generate them by creating a new Client in our Web App."*

## Using the token

Send on every subsequent request:

```
Authorization: Bearer <access_token>
```

## Logout

`DELETE /v1/logout` revokes the current access token → `202 Accepted`
`{ "message": "Token revoked successfully." }`.

## Where login happens

Use the regional instance base URL for both auth and data
(IT = `https://erpapi-it-erp.dewesoft.com`, so the token endpoint is
`https://erpapi-it-erp.dewesoft.com/v1/oauth/token`). The published docs are
hosted on `erpapi-central.dewesoft.com`; if a deployment authenticates against a
central host instead of the regional one, set `DEWESOFT_ERP_BASE_URL`
accordingly. **Confirm this against your tenant.**

## Credentials handling

Never hard-code credentials. The client reads them from environment variables
(`DEWESOFT_ERP_USERNAME`, `DEWESOFT_ERP_PASSWORD`, `DEWESOFT_ERP_CLIENT_ID`,
`DEWESOFT_ERP_CLIENT_SECRET`). Do not write tokens or secrets into files,
logs, or Claude memory.
