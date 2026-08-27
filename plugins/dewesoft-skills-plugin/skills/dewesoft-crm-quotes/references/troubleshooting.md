# Anomalie osservate e workaround

## Save silenzioso che non salva

**Sintomo:** clic su `Save` nel form di creazione quote; il pulsante si
scolorisce come se stesse lavorando, poi la pagina resta su
`/orders-quote/create`, **nessun messaggio di errore**, nessun campo evidenziato
in rosso. Nessun record creato (verificato in lista: l'ultimo documento era
ancora il precedente).

**Cosa fare:**
1. **Non ricliccare a raffica.** Apri la lista (`/orders-quote` oppure
   `/opportunities`) e verifica se il record esiste: se esiste, hai finito; se
   non esiste, ritenta.
2. Ritentare funziona: al secondo tentativo il salvataggio è andato a buon fine.
3. Per il secondo tentativo, prendi il riferimento del pulsante con `find`
   ("Save button") e clicca per `ref` invece che per coordinate: le coordinate
   possono cadere fuori dal bottone se la pagina ha scrollato.
4. Se vuoi diagnosticare, attiva prima `read_network_requests` (il tracking
   parte dalla prima chiamata al tool, quindi va attivato **prima** dell'azione)
   e filtra su `erpapi`. L'app manda anche envelope a Sentry: la presenza di un
   POST a `ingest.sentry.io` subito dopo il click è indizio di errore JS lato
   client.

## Il tab del Configurator si chiude da solo

Dopo `SAVE ITEM(S) TO QUOTE` il tab `configurator.dewesoft.com` viene chiuso
dall'app. Qualsiasi tool chiamato su quel `tabId` restituisce
"Tab ... is not in the same group" oppure "Couldn't determine which page this
action targets".

**Cosa fare:** richiama `tabs_context_mcp`, riprendi il `tabId` dell'ERP,
ricarica `/orders-quote/{id}` e verifica le righe.

## Combobox con ricerca server-side

I campi `ACCOUNT`, `CONTACT PERSON`, prodotti in Quick Add e simili sono
combobox custom con fetch remoto:
- `form_input` non è affidabile: clicca il textbox e **digita**;
- attendi 3-4 secondi prima di leggere le opzioni;
- seleziona con un click sull'opzione, poi `Escape` per chiudere il dropdown;
- per sostituire il testo digitato usa `cmd+a` e riscrivi (`triple_click` da solo
  non sempre seleziona).

## Dropdown più lunghi della viewport

`SOLUTION AREAS`, `SOLUTION`, alcune liste del Configurator mostrano ~8 voci ma
ne contengono di più. Scrolla dentro il dropdown o digita per filtrare prima di
dichiarare che un valore non esiste.

## Badge "Missing fields on account"

Warning giallo in header quote quando l'anagrafica cliente è incompleta. Non
blocca il salvataggio. Non "sistemarlo" modificando l'anagrafica senza mandato
esplicito dell'utente.

## Colonne vuote in lista

Nella lista opportunità le colonne `NAME` e `ACCOUNT` possono apparire vuote su
alcune righe mentre gli importi sono popolati. Non dedurne che i record siano
corrotti: apri il dettaglio.
