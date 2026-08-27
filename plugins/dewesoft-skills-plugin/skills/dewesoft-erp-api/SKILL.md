---
name: "dewesoft-erp-api"
description: "Usa l'API REST del CRM/ERP Dewesoft (v1, OAuth2) per leggere e scrivere dati: contatti, partner, ordini, fatture, magazzino, work order, task e altre risorse. Attivala quando l'utente vuole interrogare, creare o aggiornare record nell'ERP/CRM Dewesoft via API o automatizzare operazioni su erpapi-*-erp.dewesoft.com. Non per domande sui prodotti hardware/software o materiali commerciali."
---

# Dewesoft ERP / CRM API (v1)

Skill aziendale per chiamare l'API REST del CRM/ERP Dewesoft in modo corretto e
sicuro. L'API è versionata sotto `/v1/...`, usa autenticazione OAuth2 con Bearer
token, ed è costruita su Apiato (Laravel): quasi tutte le risorse seguono lo
stesso schema CRUD a sei rotte e lo stesso involucro di risposta paginata.

Fonte della forma dell'API: lo spec apiDoc `api_data.js` (1.501 endpoint, 224
gruppi), riassunto in `references/endpoints.md` e `references/endpoints.json`.

## Regole fondamentali (sempre valide)

1. **Mai inventare endpoint, campi o parametri.** Path, metodi, campi del body e
   forma delle risposte vanno presi dalle fonti di questa skill
   (`references/endpoints.json` per i dettagli per-endpoint, `references/auth.md`,
   `references/conventions.md`). Se un dato non è nelle fonti, dichiararlo e
   indicare dove verificarlo — non riempire i vuoti a memoria.
2. **Mai hard-codare credenziali o token.** Username, password, `client_id` e
   `client_secret` si leggono da variabili d'ambiente (vedi sotto). Non scrivere
   segreti o access token in file, log o memoria.
3. **Operazioni distruttive solo su conferma esplicita.** `POST`, `PATCH` e
   `DELETE` modificano dati aziendali reali: prima di eseguirli mostra
   all'utente cosa verrà fatto (risorsa, id, payload) e procedi solo dopo
   conferma. Le letture (`GET`) sono libere.
4. **Verifica regione e base URL.** Confermato solo IT
   (`https://erpapi-it-erp.dewesoft.com`); altre region seguono il pattern
   `erpapi-{cc}-erp.dewesoft.com` (da verificare). Imposta sempre il base URL
   in modo esplicito.
5. **Criteri di query (filtri/ordinamento/ricerca).** I *nomi* dei parametri
   (`include`, `filter`, `search`, `orderBy`, `sortedBy`, `page`, `limit`) sono
   lo standard Apiato e **non** sono enumerati in `api_data.js`: vanno confermati
   sulla pagina generale della documentazione (`#api-_`). Finché non confermati,
   trattali come tali e usa il pass-through `extra=` per qualsiasi parametro non
   verificato. Vedi `references/conventions.md`.

## Configurazione (variabili d'ambiente)

```bash
export DEWESOFT_ERP_BASE_URL=https://erpapi-it-erp.dewesoft.com   # oppure DEWESOFT_ERP_REGION=it
export DEWESOFT_ERP_USERNAME=you@dewesoft.com
export DEWESOFT_ERP_PASSWORD=********
export DEWESOFT_ERP_CLIENT_ID=...           # crea un Client nella web app ERP
export DEWESOFT_ERP_CLIENT_SECRET=...
# opzionali:
export DEWESOFT_ERP_GRANT=password          # 'password' (default) | 'client_credentials'
export DEWESOFT_ERP_SCOPE=
```

## Quickstart

Il client è in `scripts/dewesoft_erp.py` (solo libreria standard Python, nessun
`pip install`).

CLI:

```bash
python scripts/dewesoft_erp.py auth-test                 # verifica login
python scripts/dewesoft_erp.py list contacts --limit 10  # GET /v1/contacts paginato
python scripts/dewesoft_erp.py all  countries            # GET /v1/countries/all
python scripts/dewesoft_erp.py get  /v1/contacts/1       # GET arbitrario
```

Python:

```python
from dewesoft_erp import DewesoftERP
erp = DewesoftERP()                                   # legge le env vars

erp.index("contacts", limit=25, order_by="last_name", sorted_by="asc")  # GET /v1/contacts
erp.all("partners")                                   # GET /v1/partners/all
erp.get("contacts", 1, include="country")             # GET /v1/contacts/1
erp.create("contacts", {...})                         # POST /v1/contacts
erp.update("contacts", 1, {...})                      # PATCH /v1/contacts/1
erp.delete("contacts", 1)                             # DELETE /v1/contacts/1

for c in erp.iterate("contacts", page_size=100):      # tutte le pagine
    ...
```

Esempio completo e commentato (lettura + create/update/delete guidati):
`examples/contacts_examples.py`.

## Pattern CRUD universale

Per la maggior parte delle risorse (`<r>` = segmento, es. `contacts`,
`order-sales`, `work-orders`):

| operazione        | metodo + path          |
|-------------------|------------------------|
| lista paginata    | `GET /v1/<r>`          |
| lista completa    | `GET /v1/<r>/all`      |
| lettura singola   | `GET /v1/<r>/{id}`     |
| creazione         | `POST /v1/<r>`         |
| aggiornamento     | `PATCH /v1/<r>/{id}`   |
| cancellazione     | `DELETE /v1/<r>/{id}`  |

Risposta paginata: `{ data[], include[], custom[], meta.pagination{...} }`
(dettagli in `references/conventions.md`).

## Come orientarsi nelle risorse

- Catalogo navigabile di tutti gli endpoint per gruppo → `references/endpoints.md`
- Dettagli per-endpoint (parametri del body, permessi) in formato interrogabile
  → `references/endpoints.json` (es. `grep -i contact references/endpoints.json`)
- Autenticazione → `references/auth.md`
- Involucro di risposta, base URL, criteri di query → `references/conventions.md`

Per un endpoint non-CRUD o un campo specifico, cerca prima in `endpoints.json`
e cita lo spec; se manca, dichiaralo.

## Nota operativa — accesso di rete

Le chiamate live raggiungono `erpapi-it-erp.dewesoft.com`. In ambienti con
egress di rete ristretto, il dominio deve essere in allowlist perché il client
funzioni; in caso contrario le richieste falliscono per blocco di rete (un owner
dell'organizzazione può aggiornare le impostazioni di rete). La scrittura/lettura
dei file della skill non richiede rete.
