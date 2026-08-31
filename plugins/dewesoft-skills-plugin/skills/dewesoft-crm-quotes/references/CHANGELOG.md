# CHANGELOG

## 1.2.0 — 2026-08-31

Sessione di revisione `Q-00137-2026` → `Q-00137-2026/2` (id 13688) su
`OP-00114-2026`, dopo che AERO SEKUR ha ridotto l'ordine da 4 a 2 accelerometri.

Nuovo file:

- `references/versioni-quote.md` — **`Create new version`**: numerazione con
  suffisso `/N`, annullamento automatico della versione precedente, `VALUE`
  dell'opportunità che conta solo la versione attiva (niente doppio conteggio,
  a differenza di due quote separate), avanzamento automatico a
  `NEGOTIATION 75%` da una quote `SENT TO CUSTOMER`; eliminazione di una riga
  via checkbox + barra contestuale + cestino (il menu `Actions` è globale e non
  contiene il delete); `QTY` editabile sulla riga padre.

Aggiornati:

- `SKILL.md` — nuova regola non negoziabile n.6 ("una revisione non è una quote
  nuova").
- `references/quote-playbook.md` — sezione "Revisione di una quote già inviata",
  precisazioni su dove si editano quantità e prezzi e su come si cancella una riga.

Nota: la 1.1.0 correggeva il `VALUE` gonfiato annullando a mano la quote
superata. Con `Create new version` quel workaround non serve più.

## 1.1.0 — 2026-08-24 (pomeriggio)

Sessione di creazione `Q-00137-2026` (id 13676) su `OP-00114-2026` (id 12685),
replica del preventivo fornitore PCB Piezotronics `Q-232193 V-2` per AERO SEKUR.

Nuovi file:

- `references/custom-items.md` — flusso completo dei **custom item da HQ**:
  Quick Add con flag `CUSTOM ITEM FROM HQ`, campi `CUSTOM ITEM` / `QUANTITY` /
  `HQ RESP. PERSON`, editing dei prezzi **solo sulla sotto-riga `N.1`**,
  dialog matita per descrizione generale (verbatim dal fornitore) e tecnica
  (URL scheda prodotto), convenzione `TRS. PRICE` = prezzo scontato fornitore /
  `PRICE` = listino fornitore.
- `references/commercial-defaults.md` — regole **garanzia e lead time**:
  quote di sole terze parti → lead time fornitore +1 settimana, garanzia 1 anno;
  quote con almeno un prodotto Dewesoft → 8-10 settimane, garanzia 1 anno
  estendibile annualmente fino a 7 anni con calibrazione annuale (solo Dewesoft).

Aggiornati:

- `SKILL.md` — regola non negoziabile su garanzia/lead time, rimandi ai nuovi file.
- `references/quote-playbook.md` — Quick Add con custom item, prezzi sulla
  sotto-riga, `QUOTE VALIDITY DATE` assente nel form di creazione.

Anomalie nuove osservate:

- il dialog Quick Add impiega 5-10 s a diventare cliccabile; cliccare durante
  la dissolvenza chiude il dialog;
- il flag `CUSTOM ITEM FROM HQ` non persiste tra un inserimento e l'altro anche
  con `After save, create another` attivo;
- il campo `VALUE` dell'opportunità **somma tutte le quote collegate** (ma non
  le versioni dello stesso documento — vedi 1.2.0);
- in lista opportunità il numero documento è `IT26-00xxxx`, nel dettaglio
  `OP-00xxx-2026`.

## 1.0.0 — 2026-08-24

Prima versione. Basata interamente su una sessione di verifica in campo
sull'istanza IT (`it-erp.dewesoft.com`, Booster ERP), in cui sono stati creati:

- opportunità `OP-00132-2026` (id 12703)
- quote `Q-00136-2026` (id 13675) con righe `SIRIUS-X-16xUNI` e
  `PS-120W-L1B2f`, Net 18.910,00 EUR / Gross 23.070,20 EUR

Contenuti verificati in quella sessione:

- accesso: solo via Claude in Chrome; nessun egress dal container, 403 Cloudflare
  sui client HTTP, auth Clerk
- assenza della risorsa `opportunities` nell'API v1 (1.501 endpoint controllati)
- campi obbligatori e automatismi dei form opportunità e quote
- flusso a due tempi della quote (header, poi righe)
- limiti di Quick Add e flusso Configurator con `SAVE ITEM(S) TO QUOTE`
- mappa del catalogo SIRIUS X e alimentatori, con prezzi END_ITA 2025
- trappole di naming: `SIRIUSX` inesistente, `XHS-PWR` = power analyzer
- anomalia del Save silenzioso e chiusura automatica del tab Configurator

Da verificare / non ancora coperto:

- liste complete di SOLUTION AREAS e SOLUTION (viste solo le prime 8 voci)
- prezzi dei moduli SIRIUS X marcati `n.d.`
- comportamento di `Send`, `Generate` e dei template di nota (mai eseguiti)
- transizioni `PROPOSAL SENT` / `NEGOTIATION` / `DECISION - WON` / `On hold`
- modifica di righe esistenti (sconti, quantità) mai testata in scrittura
- istanze diverse da `it`
