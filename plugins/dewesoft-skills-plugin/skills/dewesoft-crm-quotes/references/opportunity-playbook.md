# Playbook — Opportunità

Verificato il 2026-08-24 creando `OP-00132-2026` (id 12703).

## URL

| Azione | URL |
|---|---|
| Lista | `/opportunities` |
| Creazione | `/opportunities/create` |
| Dettaglio / modifica | `/opportunities/{id}` |
| Duplica | `/opportunities/{id}/duplicate` |
| Nuova quote collegata | `/orders-quote/create?opportunity={id}` |

Nella lista, ogni riga espone le quattro azioni: Edit, View, Duplicate,
Create new quote. Il pulsante `+` in alto a destra apre `/opportunities/create`.
La lista mostra 25 righe per default (5/10/25/50/100/200/500 selezionabili) e ha
un campo Search in alto e un filtro con contatore di filtri attivi.

## Form di creazione — campi

Sezione **Basic information**
- `NAME` *obbligatorio* — testo libero
- `ACCOUNT` *obbligatorio* — combobox con ricerca server-side. Digita almeno
  3-4 caratteri e attendi ~3 s. Il valore visualizzato è
  `<nome breve>, <ragione sociale>`.
- `END USER` — opzionale
- `DEPARTMENT` — si popola automaticamente scegliendo l'account
- `CONTACT PERSON` *obbligatorio* — si popola automaticamente dall'account
- `OTHER CONTACT PERSONNEL` — opzionale, multi
- `RESP. SALES PERSON` *obbligatorio* — precompilato con l'utente loggato
- `RESP. SALES REP` — opzionale
- `COLABORATORS` — business developer / application engineer, multi
- `TAGS` — multi, permette di crearne di nuovi

Sezione **Deal metrics**
- `PROBABILITY (%)` *obbligatorio* — default 10, legato allo stage
- `VALUE` *obbligatorio* — default `0,00` EUR. **Si aggiorna da solo** quando
  salvi le righe di una quote collegata: non forzarlo a mano se c'è una quote.
- `DECISION DATE` *obbligatorio* — tre campi separati `dd` / `mm` / `yyyy`,
  precompilata a +30 giorni circa
- `PRICE LIST VERSION` *obbligatorio* — si popola dall'account (es. `END_ITA 2025`)
- `IS LIABLE FOR TAX` — toggle, si imposta dall'account
- `ISSUE PO TO HQ` — toggle, default NO

Sezione **Additional information**
- `OPPORTUNITY SOURCE` — opzionale
- `CAMPAIGN` — opzionale
- `LEAD` — read-only, "Automatically matched lead"
- `INDUSTRY` *obbligatorio* — si popola dall'account
- `SOLUTION AREAS` *obbligatorio* — multi-select
- `SOLUTION` *obbligatorio* — multi-select
- `PRIMARY PURPOSE` *obbligatorio* — single select
- `DESCRIPTION` — testo libero

Sezione **Competition** — pulsante `+ Add new`, opzionale.

Sezione **Taxes** — tabella `Tax Type / Default Tax Rate / Tax Override (%)`.
Lasciare vuoto l'override salvo richiesta esplicita. Righe viste sull'istanza IT:
VAT 20 (20%), 10-DDV 22% osnovna stopnja (22%), 7-Prejemniki kot plač. DDV 22%
(22%), 4-DDV 22% osnovna stopnja (22%), 6-DDV 0% oproščen promet (0%),
5-DDV 9,5% znižana stopnja (9,5%), 8-Prejemniki kot plač. DDV 9,5% (9,5%),
1-DDV 22% osnovna stopnja (22%), IVA 22%, IVA 0%, IVA 10%.

**Scorciatoia importante:** scegliere l'`ACCOUNT` per primo riempie da solo
department, contact person, price list version, industry e il flag tax. Fallo
sempre prima degli altri campi: risparmi cinque combobox.

## Valori di enumerazione osservati

`SOLUTION AREAS` (lista scrollabile, primi otto visti): General data recording,
Power & Energy analysis, Vehicle Testing, Vibration analysis, Acoustic analysis,
Monitoring, Automation & Control, Telemetry.

`SOLUTION` (lista scrollabile, primi otto visti): High speed and transient
recording, Fatigue, High channel count data recording, Industrial bus systems,
Aerospace bus systems, Vehicle bus systems, Video, GPS & IMU.

`PRIMARY PURPOSE` (completa): Operations, Other, Production, R&D,
Service / Maintenance.

Le prime due liste sono più lunghe di quanto entri a schermo: se il valore che
cerchi non compare, **scrolla dentro il dropdown** o digita per filtrare, non
concludere che non esiste.

## Stage e transizioni

Barra di stato sul dettaglio:
`NEW 10%` → `IN PROGRESS 25%` → `PROPOSAL SENT 50%` → `NEGOTIATION 75%` →
`DECISION - WON 100%`.

Pulsanti in header del dettaglio: `Lost`, `Cancel`, `On hold`, `History`.
Nel record appena creato (stage NEW) l'header mostra `Decision - lost`, `Cancel`,
`History`; gli altri pulsanti compaiono con l'avanzare dello stage.

**Automatismo verificato:** salvando le righe prodotto di una quote collegata,
l'opportunità passa da `NEW 10%` a `IN PROGRESS 25%` e il campo `VALUE` si
allinea al netto della quote. Non serve intervenire a mano.

Il dettaglio ha anche il pannello laterale: Activity timeline (con `Create`),
Email client, Notes, Tasks, NSRF.

## Modifica di un'opportunità esistente

Apri `/opportunities/{id}`, modifica i campi in place, poi Save. Le sezioni
Additional information / Competition / Taxes sono collassate: espandile prima di
cercarci un campo. Mostra sempre il diff (campo: da → a) e attendi conferma
prima di salvare.
