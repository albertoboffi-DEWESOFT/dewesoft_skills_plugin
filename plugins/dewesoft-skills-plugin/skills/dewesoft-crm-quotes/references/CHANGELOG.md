# CHANGELOG

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
