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
   possono cadere fuori dal bottone se la pagina ha scrollato. **Attenzione:**
   questo vale solo per un pulsante gia' visibile a schermo - per gli elementi
   sotto la piega vale la regola opposta, vedi "Pulsanti dell'ERP che sembrano
   morti".
4. Se vuoi diagnosticare, attiva prima `read_network_requests` (il tracking
   parte dalla prima chiamata al tool, quindi va attivato **prima** dell'azione)
   e filtra su `erpapi`. L'app manda anche envelope a Sentry: la presenza di un
   POST a `ingest.sentry.io` subito dopo il click è indizio di errore JS lato
   client.

## Il Configurator perde l'aggancio alla quote a ogni reload

**Sintomo:** il pulsante in fondo al carrello legge `CHECKOUT` (scolorito)
invece di `SAVE ITEM(S) TO QUOTE`, e cliccarlo non fa nulla: nessun dialog,
nessun errore a schermo, **nessuna chiamata di rete**. In console solo warning
Sentry, nessuna eccezione.

**Causa (verificata 2026-09-21):** il Configurator carica la quote con
`GET https://api.dewesoft.com/api/quotes/{id}?...&type=Quote&tenant=erp`.
Quando quella chiamata torna **HTTP 500** l'aggancio e' rotto e all'apertura
compare il popup `This action is unauthorized - getQuote`. Il 500 si presenta
dopo qualsiasi **ricaricamento di pagina** nel tab del Configurator (`navigate`
su un URL diretto, F5): lo stato della sessione quote vive solo nella SPA.

**Cosa fare:**

1. Chiudere il tab del Configurator e riaprirlo da `+ Add from Configurator`
   sul dettaglio della quote.
2. Da li' in poi **navigare solo dentro la SPA**, cliccando i link della
   sidebar (`OBSIDIAN` -> `OBSIDIAN-R12`). Mai `navigate` su un URL del
   Configurator.
3. Per azzerare la configurazione di un sistema e costruirne un altro, usare
   l'**icona cerchio-barrato** in alto a sinistra del pannello prodotto, non il
   reload.
4. Prima di salvare, **verificare che il pulsante legga `SAVE ITEM(S) TO
   QUOTE`**: se legge `CHECKOUT`, l'aggancio e' perso e il salvataggio
   fallirebbe in silenzio.

Diagnosi rapida: `read_network_requests` sul tab del Configurator, filtro
`quotes` - un 500 su `/api/quotes/{id}` conferma il problema.

## Pulsanti dell'ERP che sembrano morti

**Sintomo:** `+ Quick Add` e `+ Add from Configurator` non aprono nulla:
nessun dialog, nessun nuovo tab, nessuna chiamata verso `erpapi`.

**Causa:** il click e' stato fatto **per `ref`** su un elemento fuori dalla
porzione visibile della pagina. Nemmeno `scroll_to` seguito da click per `ref`
e' sufficiente.

**Cosa fare:** scrollare la pagina, fare uno `screenshot`, leggere le coordinate
dallo screenshot e cliccare **per coordinate**. Poi attendere 8-10 secondi: i
dialog dell'ERP sono lenti ad aprirsi.

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
