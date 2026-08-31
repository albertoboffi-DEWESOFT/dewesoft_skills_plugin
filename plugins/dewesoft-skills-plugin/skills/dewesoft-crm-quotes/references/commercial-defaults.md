# Default commerciali — garanzia e lead time

Regole date da **Alberto Boffi il 2026-08-24**. Valgono per l'istanza IT.
Si applicano ai campi `WARRANTY` e `LEAD TIMES` della sezione
**Terms & Conditions** della quote.

## Regola di composizione

La quote può contenere righe **solo di terze parti** (custom item da preventivo
fornitore) oppure **anche prodotti Dewesoft**. Il criterio è binario: basta
**una** riga Dewesoft perché valgano i default Dewesoft su tutta la quote.

| Contenuto della quote | `LEAD TIMES` | `WARRANTY` |
|---|---|---|
| **Solo custom item di terze parti** | lead time dichiarato dal fornitore **+ 1 settimana** | **1 anno** |
| **Contiene almeno un prodotto Dewesoft** | **8-10 settimane** (default) | **1 anno** |

La settimana aggiuntiva sui soli item di terze parti copre il transito
fornitore → Dewesoft Italia → cliente.

## Esempio verificato

Preventivo PCB `Q-232193 V-2`: consegna dichiarata **"2 Sett. DRO"** su tutte
le righe → in quote `LEAD TIMES` = **3 settimane**, `WARRANTY` = **1 anno**.

Se il fornitore dichiara lead time diversi riga per riga, prendi **il più
lungo** e sommaci la settimana.

## Estensione di garanzia — solo prodotti Dewesoft

La garanzia Dewesoft di 1 anno è **estendibile annualmente fino a 7 anni**,
condizionata alla **calibrazione annuale** del prodotto.

Vincoli:
- vale **solo per i prodotti Dewesoft**, mai per sensori, cavi o accessori di
  terze parti rivenduti come custom item;
- l'estensione va quotata come riga a sé (Configurator, categoria
  `Warranty & Calibration`), non dichiarata solo a testo;
- senza calibrazione annuale l'estensione decade: se la proponi, quota anche
  le calibrazioni.

Non promettere estensione di garanzia su una quote mista senza separare
chiaramente a quali righe si applica.

## Applicazione operativa

Compila `WARRANTY` e `LEAD TIMES` **prima** del Save dell'header quote, e
rivedili se dopo aggiungi righe che cambiano la composizione della quote
(es. una quote nata solo-PCB a cui aggiungi un IOLITE passa a 8-10 settimane).

`LEAD TIME OVERRIDE` è un campo di testo libero che **prevale** sul valore
scelto in `LEAD TIMES`: usalo quando il lead time reale non esiste come voce di
elenco (es. `3 settimane` se la lista non lo prevede, o formule tipo
`3 settimane dalla conferma d'ordine`).
