# Learning log — protocollo di auto-aggiornamento

La skill non può riscrivere il proprio file (i file skill in sessione sono una
cache read-only). L'apprendimento persistente vive in **Open Brain**.

## Dove

- Cassetto: **openbrain-priv** (progetto [DEWESOFT], mai il cassetto ALUM)
- Tag: **`["DEWESOFT","quote_skill"]`** — sempre entrambi, sempre questa grafia

## Quando leggere

**All'inizio di ogni task**, prima di toccare l'ERP:
`search_thoughts` su openbrain-priv con `tags: ["DEWESOFT","quote_skill"]`.
Un ricordo più recente **prevale** su quanto scritto nei `references/` di questa
skill: cita la data del ricordo quando lo applichi.

## Quando scrivere

**A fine task, proponendo e attendendo l'ok dell'utente.** Non chiamare mai
`capture_thought` di iniziativa. Prima di scrivere, `search_thoughts` sullo
stesso tema: se esiste un ricordo che il nuovo sostituisce, mostra l'ID e chiedi
se aggiornarlo o affiancarlo.

## Cosa merita di essere salvato

- campi obbligatori nuovi, rinominati o spariti nei form;
- valori di enumerazione visti per la prima volta (SOLUTION AREAS, SOLUTION,
  PRIMARY PURPOSE, payment terms, incoterm, lead time);
- codici prodotto e prezzi verificati a schermo, **con la versione di listino e
  la data**;
- automatismi dell'ERP (campi che si popolano da soli, stage che avanzano);
- bug, save silenziosi, comportamenti dei tab, e il workaround che ha funzionato;
- account/contatti/department ricorrenti e le loro particolarità;
- decisioni commerciali dell'utente riusabili (sconti standard, configurazioni
  tipiche per applicazione, cosa includere o escludere in offerta);
- numeri documento creati in sessione, se servono da riferimento.

## Cosa NON salvare

- trascrizioni di conversazione o log integrali;
- screenshot o dump di pagina;
- prezzi "a memoria" non letti a schermo;
- dati personali di contatti oltre a nome e ruolo, se non necessari;
- nulla nel cassetto ALUM.

## Formato del ricordo

Testo breve e distillato, autoconsistente, con provenienza. Modello:

> **[quote_skill] <argomento in tre parole>** — <fatto o regola>.
> Contesto: <come l'ho verificato: URL, documento, azione>.
> Verificato: <data>, istanza <it/uae>, listino <nome> (se pertinente).
> Impatto: <cosa cambia nel modo di operare>.

Esempio:

> **[quote_skill] Quick Add esclude i sistemi rack** — Quick Add accetta solo
> articoli semplici; sistemi rack, licenze software, calibrazioni e cavi custom
> vanno inseriti dal Configurator. Cercare "SIRIUSX" in Quick Add dà "No
> elements found" pur esistendo il ramo SIRIUS > Modular > SIRIUS X.
> Contesto: creazione Q-00136-2026 su it-erp.dewesoft.com.
> Verificato: 2026-08-24, istanza it.
> Impatto: per un sistema, andare direttamente al Configurator.

## Manutenzione del file skill

Quando il log accumula abbastanza da rendere obsoleto un `references/`, dillo
all'utente e proponi di rigenerare il pacchetto `.skill` con i contenuti
aggiornati, alzando `metadata.version` e aggiungendo una voce al `CHANGELOG.md`.
Il file va poi ri-salvato dall'utente: non c'è modo di aggiornarlo dalla
sessione.
