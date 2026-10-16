# Custom item da HQ — righe di terze parti in una quote

Verificato il **2026-08-24** creando `Q-00137-2026` (id 13676) su
`OP-00114-2026` (id 12685), replicando il preventivo fornitore
PCB Piezotronics `Q-232193 V-2`.

## Quando serve un custom item

Quando l'articolo **non è a catalogo Dewesoft**: sensoristica e cavi di terze
parti (PCB, Kistler, Brüel & Kjær...), servizi, ricambi non codificati,
rivendita di materiale acquistato su preventivo fornitore.

Non usare il custom item per prodotti Dewesoft: quelli vanno da **Quick Add**
(articoli semplici) o dal **Configurator** (sistemi rack, licenze software,
calibrazioni, lunghezze cavo custom).

## Creazione — Quick Add con flag

Sul dettaglio `/orders-quote/{id}`, sezione **Product list** → **`+ Quick Add`**.
Nel dialog "Add Dewesoft item to quote" spunta **`CUSTOM ITEM FROM HQ`**: i
campi cambiano da `PRODUCT`/`QUANTITY` a:

| Campo | Contenuto |
|---|---|
| `CUSTOM ITEM` | testo libero = nome riga. Convenzione IT: `<famiglia> <codice fornitore>`, es. `Triax PC 3713F1110G`, `Cavo 15mt 037P50` |
| `QUANTITY` | quantità della riga |
| `HQ RESP. PERSON` | testo libero. Convenzione IT: `Alberto Boffi (DWS ITA)` |

Checkbox **`After save, create another`**: spuntala per inserire più custom
item di fila senza riaprire il dialog. Il flag `CUSTOM ITEM FROM HQ` **non**
resta spuntato tra un inserimento e l'altro: va rimesso ogni volta.

Il dialog impiega **5-10 secondi** a diventare cliccabile (compare prima in
dissolvenza). Non cliccare sui campi mentre è semitrasparente: il click cade
sull'overlay e chiude il dialog. Attendi e verifica con uno screenshot.

## Prezzi — si editano solo sulla sotto-riga

Appena creata, la riga ha `TRS. PRICE €0.00`, `PRICE Incl.`, `TOTAL Incl.`.
I valori **non sono editabili sulla riga padre**: espandi la riga con il
chevron `>` e edita la **sotto-riga `N.1`**, dove `TRS. PRICE` e `PRICE` sono
sottolineati e quindi editabili in linea.

Procedura per riga:
1. click sul chevron della riga padre → compare la sotto-riga `N.1`
2. click su `TRS. PRICE` della sotto-riga → `cmd+a`, digita il valore, `Return`
3. click su `PRICE` della sotto-riga → `cmd+a`, digita il valore, `Return`
4. richiudi la riga padre prima di passare alla successiva: la tabella si
   ricalcola e le coordinate delle righe sotto slittano

**Formato numerico in input: punto decimale, senza separatore di migliaia**
(`1940.40`, `560.02`). A schermo viene poi reso `€1,940.40`.

Il ricalcolo di Cost Analysis / Order Summary richiede 3-5 secondi.

## Descrizioni — matita "Edit product name or description"

L'icona matita accanto al nome della riga apre il dialog con quattro campi:

| Campo | Contenuto |
|---|---|
| `ENTER NAME` * | nome riga (già valorizzato) |
| `HQ RESP. PERSON` | già valorizzato |
| `ENTER DESCRIPTION` | **descrizione generale** — testo semplice. Convenzione: descrizione **verbatim dal preventivo del fornitore**, in lingua originale |
| `TECHNICAL DESCRIPTION` | **descrizione tecnica** — editor rich text. Convenzione: URL alla scheda prodotto del fornitore, es. `https://www.pcb.com/products?m=<codice>` |

Poi `Save`. La descrizione generale compare nella colonna DESCRIPTION del PDF
di offerta; la tecnica no (resta interna al record).

## Convenzione di prezzo su rivendita da preventivo fornitore

Verificata su Q-00113-2026 e replicata su Q-00137-2026 (fornitore PCB):

- **`TRS. PRICE`** = prezzo **scontato** del fornitore (il costo Dewesoft)
- **`PRICE`** = prezzo di **listino** del fornitore (nessuno sconto in quote)

Conseguenza: il `Net` della quote coincide con il "Totale Prezzo" di listino
del preventivo fornitore e il `Purchase Price` con il suo "Totale parziale".
Il margine è lo sconto che il fornitore riconosce a Dewesoft (27% circa con PCB).

Non applicare sconto in colonna `DISCOUNT` salvo richiesta esplicita: lo sconto
è già dentro la differenza TRS/PRICE.

## Trappole

- Il campo `VALUE` dell'opportunità **somma tutte le quote collegate**, anche
  quelle superate. Creando la revisione di un'offerta il valore in pipeline
  raddoppia: dopo aver creato la nuova quote, chiedi all'utente se disattivare
  o annullare la precedente, oppure forzare `VALUE` a mano.
- Il form di creazione quote **non contiene** `QUOTE VALIDITY DATE`: compare
  solo sul dettaglio dopo il primo salvataggio (default +30 giorni).
- Nella lista opportunità il numero documento appare come `IT26-00xxxx`, mentre
  nel dettaglio e nelle relazioni è `OP-00xxx-2026`. Sono lo stesso record.
