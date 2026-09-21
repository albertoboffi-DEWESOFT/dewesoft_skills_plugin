# CHANGELOG

## 1.1.0 - 2026-09-21

Sessione ALTEN: popolamento di `Q-00192-2026` (id 13756) sull'opportunita'
`OP-00146-2026` con 3 sistemi OBSIDIAN-R12 dal Configurator, 60 `DSIi-10A`,
4 custom item da HQ e 2 giornate di training scontate al 30%.
Net finale 106.479,47 EUR, Gross 129.904,95 EUR.

Nuovo in questa versione:

- `troubleshooting.md`: il Configurator perde l'aggancio alla quote a ogni
  reload di pagina (HTTP 500 su `/api/quotes/{id}`, pulsante `CHECKOUT`
  inerte, salvataggio silenziosamente fallito); i pulsanti dell'ERP vanno
  cliccati per coordinate, non per `ref`, quando sono sotto la piega. Il
  secondo punto **corregge** la regola della 1.0.0.
- `quote-playbook.md`: regole del Configurator agganciato (navigazione solo
  SPA, reset con cerchio-barrato, prezzi slice come delta del `Total price`,
  sincronizzazione del carrello senza duplicati), convenzione
  `Training on-site` a 1.400,00 EUR/giornata con sconto in colonna `DISCOUNT`,
  e cartelle di raggruppamento del Product list.
- `catalog-map.md`: OBSIDIAN-R12 e slice IOLITE rack con prezzi e stock
  END_ITA 2025, `DSIi-10A`, e la trappola DSUB9 contro D37.

Da verificare / non ancora coperto:

- creazione e gestione delle cartelle del Product list dalla skill;
- rinomina delle righe generate dal Configurator (non espongono la matita);
- comportamento di `Send` e `Generate`.

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
