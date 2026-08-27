# Accesso all'ERP — cosa funziona e cosa no

Verificato il 2026-08-24 sull'istanza IT.

## Endpoint

| Cosa | URL |
|---|---|
| Web app (Booster ERP) | `https://it-erp.dewesoft.com` |
| API REST v1 | `https://erpapi-it-erp.dewesoft.com/v1` |
| Configurator prodotti | `https://configurator.dewesoft.com` |

Pattern multi-region: `https://<slug>-erp.dewesoft.com` e
`https://erpapi-<slug>-erp.dewesoft.com/v1`. Istanze note attive: `it`, `uae`.
Solo `it` è verificata in campo.

## Vie di accesso

**Funziona: Claude in Chrome sul browser dell'utente.**
L'app autentica via **Clerk** (login Google); i token sono JWT a vita breve
rinnovati dal browser. Pilotando il Chrome dell'utente già loggato si opera
sull'ERP con i suoi permessi, in lettura e in scrittura.

Sequenza di avvio:
1. `list_connected_browsers` — se torna `[]` l'estensione non è connessa: chiedi
   all'utente di aprire/attivare l'estensione Claude per Chrome
   (`claude.ai/chrome`), loggata con lo stesso account, e di abilitare il sito
   `it-erp.dewesoft.com` nei permessi.
2. Presenta all'utente la lista dei browser connessi e fallo scegliere, poi
   `select_browser`.
3. `navigate` all'URL ERP e `screenshot` per verificare di essere loggati.

**Non funziona (non tentare):**
- `curl` / `requests` / qualsiasi client HTTP scriptato → **403 Cloudflare**
  ("Sorry, you have been blocked"), anche sulla pagina di documentazione API.
- Rete dal container cloud di sessione → nessun egress verso `*.dewesoft.com`
  (HTTP code `000` su entrambi gli host). Non è un problema di credenziali.
- Playwright dentro il container → stesso blocco di rete, e comunque nessuna
  sessione Clerk.
- OAuth2 `client_id`/`client_secret`: l'app non li usa per questo flusso, e
  nello spec API non esiste un endpoint per crearli (si generano solo a mano
  nella web app).

## Note sull'API (per quando sarà raggiungibile)

- Le **opportunità NON esistono come risorsa API**: nei 1.501 endpoint dello
  spec `api_data.js` non c'è nessun gruppo `opportunities`/`leads`/`deals`.
  Ricerca su `oppo|lead|deal|pipel`: zero risultati. Le opportunità si creano e
  si modificano **solo dalla UI**.
- Le quote invece ci sono: `/v1/orders-quote`, `/v1/orders-quote/all`,
  `/v1/orders-quote/{id}`, `/v1/order-quote-items` (CRUD Apiato standard).
- Ordini di vendita: `/v1/orders-sale` (**non** `order-sales`).
- Query params reali: `limit`, `page`, `sort=campo` (`sort=-campo` per desc),
  `search=`, `filter[campo]=`, `include=`. **Non** `orderBy`/`sortedBy`.
- Ultima pagina: `meta.last_page` (non `meta.pagination.total_pages`).
- Se serve chiamare l'API, il modo che ha funzionato storicamente è farlo da
  **dentro il contesto della pagina** con il token Clerk:
  `const t = await window.Clerk.session.getToken()` e poi `fetch` con
  `Authorization: 'Bearer ' + t`. Usa `javascript_tool` sul tab ERP.
  Per le scritture preferisci comunque la UI: valida i campi e aggiorna i
  totali e gli stage in automatico.

Fonte: verifiche in campo 2026-07-31 (lettura 2.420 partner, 4.929 contatti) e
2026-08-24 (creazione OP-00132-2026 e Q-00136-2026).
