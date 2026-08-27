# Playbook — Quote (offerte) e righe prodotto

Verificato il 2026-08-24 creando `Q-00136-2026` (id 13675) collegata a
`OP-00132-2026`.

## URL

| Azione | URL |
|---|---|
| Lista | `/orders-quote` |
| Creazione libera | `/orders-quote/create` |
| Creazione collegata a un'opp | `/orders-quote/create?opportunity={opp_id}` |
| Dettaglio / modifica | `/orders-quote/{id}` |

Usa **sempre** la forma con `?opportunity={id}` quando la quote nasce da
un'opportunità: precompila name, account, contact person, department, price list,
payment terms, incoterm e lead time. Risparmia dieci campi e non sbaglia
l'aggancio.

Numerazione: `Q-000NN-AAAA` (es. `Q-00136-2026`). Nella lista convivono anche
documenti con numerazione vecchia stile `004089/2025`.

## Il flusso è in due tempi

**Il form di creazione NON contiene le righe prodotto.** Prima si salva
l'intestazione, poi sul dettaglio appare la sezione `Product list`. Non cercare
il Product list nella pagina di creazione: non c'è.

### Tempo 1 — intestazione

Sezione **Basic information**: `NAME` *obbligatorio*, `RESP. SALES PERSON`
*obbligatorio*, `RESP. SALES REP`, `TAGS`.

Sezione **Price lists and currencies**: `END USER PRICE LIST VERSION`
*obbligatorio* (es. `END_ITA 2025`), `END USER PRICE LIST CURRENCY` *obbligatorio*
(EUR), `QUOTED CURRENCY` *obbligatorio* (EUR), `END PRICE CURRENCY RATE` (1),
`TRANSFER PRICE LIST VERSION` (es. `TRANSFER [€] 2026`), `TRANSFER CURRENCY`
(EUR), `TRANSFER CURRENCY RATE` (1). Ogni rate ha un pulsante di refresh.

Sezione **Opportunity**: `OPPORTUNITY`, `CONTACT PERSON` *obbligatorio*,
`ACCOUNT` *obbligatorio*, `DEPARTMENT`, `LEAD SOURCE`, `SALES ORDER`,
`END USER`, `CAMPAIGN`.

Sezione **Terms & Conditions**: `PAYMENT TERMS` *obbligatorio* (default IT visto:
`50% BB ALL'ORDINE e 50% BB 30GG DFFM`), `INCOTERM CODE` (`DAP, Porto Franco`),
`LEAD TIMES` (`20-24 settimane`), `LEAD TIME OVERRIDE` (testo, prevale sul lead
time), `WARRANTY`, `TERMS AND CONDITIONS OF SALE`, `NOTE` (editor rich text con
immagini, video, heading H1-H5, liste, tabelle e un pulsante `TEMPLATES`).

Checkbox `After save, create another` accanto a Save: lasciala deselezionata
salvo batch.

### Tempo 2 — righe prodotto

Sul dettaglio `/orders-quote/{id}`, sezione **Product list** con colonne
`ID / PRODUCT / TRS. PRICE / QTY / PRICE / DISCOUNT / TOTAL`, un toggle per riga
(attivo/disattivo) e una maniglia di riordino. Pulsanti `Columns` e `Actions`.

Tre modi per aggiungere righe:

**a) `+ Quick Add`** — dialog "Add Dewesoft item to quote". Combobox con ricerca
su codice e descrizione, campo `QUANTITY`, checkbox `CUSTOM ITEM FROM HQ`,
pulsante `+ Add to quote`.
Limite dichiarato dall'ERP: **Quick Add accetta solo articoli semplici.** Non si
possono aggiungere con Quick Add:
1. tutti i sistemi rack
2. licenze software
3. calibrazioni
4. lunghezze cavo custom
Per questi serve il Configurator. Conseguenza pratica: cercare un sistema (es.
`SIRIUSX`) in Quick Add restituisce "No elements found" — non significa che non
esista in catalogo.

**b) `+ Add from Configurator`** — apre `configurator.dewesoft.com` in un **nuovo
tab**, agganciato alla quote: in header compare
`You are editing: #Q-00136-2026 <nome quote>` con un pulsante `DESELECT`, e il
price list selezionato (es. `END_ITA 2025`) è quello della quote.
Flusso: naviga il catalogo o usa la ricerca (`CMD+SHIFT+S`), aggiungi al
carrello con il `+` sulla card (o con l'icona carrello nella pagina prodotto),
verifica il pannello `Cart items (N)` a destra con totale, peso e spedizione
stimata, poi **`SAVE ITEM(S) TO QUOTE`**.
Dopo il salvataggio il **tab del Configurator si chiude da solo**: rileggi
`tabs_context_mcp`, poi ricarica `/orders-quote/{id}` per vedere le righe.

**c) `+ Add local products`** — articoli locali non a catalogo HQ.

## Totali

- **Cost Analysis**: Purchase Price, Sales Price, Net profit, Net margin (%).
- **Order Summary**: Discount, Shipping (link `Empty` se non impostata), Net,
  IVA (%), Gross.
- La colonna `TRS. PRICE` è il transfer price (costo interno): compare in
  chiaro nella riga. Attenzione a non condividerla col cliente.

Esempio verificato: SIRIUS-X-16xUNI (trs. 9.000,00 / prezzo 18.750,00) +
PS-120W-L1B2f (trs. 97,00 / prezzo 160,00) → Net 18.910,00 EUR, IVA 22%
4.160,20 EUR, Gross 23.070,20 EUR, Net margin 51,89%.

## Sezioni collegate sul dettaglio

`Sales orders` e `Purchase orders` (tabelle con contatore, vuote su una quote
nuova), `Shipping information` e `Billing information` (collassabili).

Pannello laterale destro: `Quote preview` con il PDF renderizzato (selettore
lingua `IT` / `EN`), e i pulsanti `Send`, `Generate`, download e refresh.
Tab: Quote preview, Activity timeline, Email client, Notes, Tasks.

- `Generate` rigenera il PDF dell'offerta.
- **`Send` invia l'offerta al cliente**: non premerlo mai senza richiesta
  esplicita dell'utente nel messaggio corrente.

Barra di stato della quote: `NEW` → `SENT TO CUSTOMER` → `ORDER CREATED`.
Stati visti in lista: NEW, SENT TO CUSTOMER, ORDER CREATED, CLOSED.
Header del dettaglio: `Cancel`, `History`, e un badge di warning
`Missing fields on account` quando l'anagrafica cliente è incompleta.

## Modifica di una quote esistente

- Quantità, prezzo e sconto si editano in linea nel Product list.
- Il toggle di riga esclude una riga dal calcolo senza cancellarla.
- Per righe di sistema, riapri il Configurator dalla quote (`Add from
  Configurator`) così resta agganciato allo stesso documento.
- Dopo ogni modifica ai totali, controlla se l'opportunità collegata ha
  aggiornato `VALUE` e stage.
