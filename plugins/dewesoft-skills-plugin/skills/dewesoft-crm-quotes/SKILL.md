---
name: dewesoft-crm-quotes
description: Crea e modifica opportunità e quote (offerte) nel CRM/ERP Dewesoft Booster (it-erp.dewesoft.com) pilotando il browser dell'utente, e legge/cerca record esistenti. Attivala quando l'utente vuole aprire, aggiornare, far avanzare o chiudere un'opportunità, creare o modificare una quote e le sue righe prodotto, aggiungere articoli dal Configurator, applicare sconti, rigenerare il PDF dell'offerta, o cercare account, contatti, opportunità e quote nell'ERP. Frasi tipiche - "apri un'opportunità", "crea un'offerta per", "aggiungi una riga alla quote", "quota un SIRIUS/KRYPTON/IOLITE per il cliente X", "porta l'opp a proposal sent", "quanto costa quotare", "Q-00xxx", "OP-00xxx", "Booster ERP", "CRM Dewesoft". NON usarla per domande solo tecniche sui prodotti (usa dewesoft-technical-expert) né per generare documenti .docx/.pptx (usa dewesoft-brand-identity).
license: Proprietario Dewesoft Italia - uso interno
metadata:
  version: 1.0.0
  owner: alberto.boffi@dewesoft.com
  verified-instance: it (it-erp.dewesoft.com)
  last-field-verification: 2026-08-24
---

# Dewesoft CRM — Opportunità e Quote

Skill operativa per lavorare sul CRM/ERP Dewesoft **Booster ERP** (istanza IT
verificata: `https://it-erp.dewesoft.com`). Copre creazione e modifica di
**opportunità**, **quote** e delle loro **righe prodotto**, più lettura/ricerca
dei record esistenti.

Questa skill è **auto-apprendente**: ogni utilizzo termina proponendo un
aggiornamento del learning log in Open Brain, che viene riletto all'avvio
successivo. Vedi `references/learning-log.md`.

## Regole non negoziabili

1. **Non inventare mai** codici prodotto, prezzi, campi, path o valori di
   enumerazione. Tutto viene letto a schermo dall'ERP o dal Configurator, o dai
   file `references/` di questa skill. Se un dato non c'è, dichiaralo.
2. **Ogni scrittura passa da conferma esplicita dell'utente.** Prima di premere
   Save, Add to quote, Save item(s) to quote, Send, Lost, Cancel o On hold,
   mostra il riepilogo esatto di ciò che verrà scritto e attendi l'ok. Le
   letture sono libere.
3. **Mai premere Send** (invio offerta al cliente) senza richiesta esplicita e
   inequivocabile dell'utente in quel messaggio.
4. **Dati di produzione.** Se il record è un test, il nome deve iniziare con
   `TEST - ` e la description deve dire chi l'ha creato e che va cancellato.
5. **Verifica prima di ritentare un Save.** Il Save può fallire in silenzio
   (vedi `references/troubleshooting.md`): controlla la lista record prima di
   ricliccare, altrimenti crei duplicati.

## Passo 0 — Contesto (sempre)

1. Cerca in Open Brain il contesto accumulato:
   `search_thoughts` su **openbrain-priv** con `tags: ["DEWESOFT","quote_skill"]`.
   Se ci sono ricordi, applicali: sovrascrivono i `references/` di questa skill
   quando più recenti.
2. Se l'utente ha nominato un cliente, un'applicazione di misura o un
   concorrente, cerca anche con `tags: ["DEWESOFT"]` sul nome del cliente.

## Passo 1 — Accesso (leggi `references/access-and-auth.md`)

L'ERP **non è raggiungibile** da container/script: no egress, Cloudflare 403 sui
client HTTP, auth Clerk con JWT a vita breve. **L'unica via è Claude in Chrome**
sul browser dell'utente già loggato. Non tentare curl/requests/Playwright.

## Passo 2 — Dimensionamento tecnico prima di quotare

Prima di costruire le righe di una quote, se la richiesta è espressa in termini
di applicazione ("serve misurare NVH su un banco", "power analysis su inverter")
e non di codici prodotto:

- invoca **`dewesoft-technical-expert`** per scegliere moduli, amplificatori,
  numero di canali, sample rate, sensori, alimentatori e software necessari, e
  per verificare compatibilità e vincoli (connettori, sincronizzazione,
  alimentazione);
- invoca **`dewesoft-business-development`** per il posizionamento commerciale:
  configurazione tipica per quell'applicazione, alternative, elementi di
  confronto con la concorrenza, cosa vale la pena includere in offerta.

Presenta all'utente la configurazione proposta con motivazione tecnica **prima**
di inserirla nell'ERP. Non quotare a caso: una riga sbagliata in una quote è un
errore commerciale, non un errore di UI.

Per il deliverable documentale (offerta tecnica .docx, presentazione .pptx)
invoca **`dewesoft-brand-identity`**. Per interrogazioni API in lettura (quando
un giorno saranno raggiungibili) c'è **`dewesoft-erp-api`**.

## Passo 3 — Esecuzione

- Opportunità: segui `references/opportunity-playbook.md`
- Quote e righe: segui `references/quote-playbook.md`
- Ricerca articoli e mappa del catalogo: `references/catalog-map.md`
- Anomalie e workaround: `references/troubleshooting.md`

Regola di navigazione: preferisci sempre l'URL diretto
(`/opportunities/{id}`, `/orders-quote/{id}`) al click nelle liste, e usa
`browser_batch` per raggruppare click+type+wait+screenshot.

## Passo 4 — Chiusura e auto-aggiornamento

A fine task, **sempre**:

1. Riepiloga all'utente: cosa è stato creato/modificato, con document number,
   id e URL, e i totali (Net / IVA / Gross).
2. Estrai le **novità** rispetto a questa skill: campi obbligatori nuovi o
   cambiati, valori di enumerazione visti per la prima volta, codici e prezzi
   verificati, comportamenti automatici dell'ERP, bug e workaround, nomi di
   account/contatti utili.
3. Proponi all'utente il ricordo distillato da salvare in **openbrain-priv** con
   `tags: ["DEWESOFT","quote_skill"]` e **attendi il suo ok** prima di scrivere.
   Prima di scrivere, `search_thoughts` per non duplicare: se esiste un ricordo
   sullo stesso tema, proponi di sostituirlo (mostra l'ID e chiedi conferma).
   Formato e criteri: `references/learning-log.md`.
4. Se in questa sessione hai imparato qualcosa che meriterebbe di stare nel file
   della skill e non solo nel log, dillo: il file skill non si riscrive da sé,
   va rigenerato e ri-salvato dall'utente.
