# Revisioni di una quote — `Create new version`

Verificato il **2026-08-31** creando `Q-00137-2026/2` (id 13688) da
`Q-00137-2026` (id 13676) su `OP-00114-2026` (id 12685).

## Revisione ≠ nuova quote

Quando il cliente cambia idea su un'offerta **già inviata**, non creare una
quote nuova: crea una **versione** del documento esistente.

| | Nuova quote (`+ Add new`) | Nuova versione (`Create new version`) |
|---|---|---|
| Numerazione | nuovo numero (`Q-00138-2026`) | stesso numero + suffisso (`Q-00137-2026/2`) |
| Documento precedente | resta attivo | **passa da solo a `CANCELED`** |
| `VALUE` dell'opportunità | **si somma** → valore in pipeline raddoppiato | conta **solo la versione attiva** → nessun doppio conteggio |
| Storico per il cliente | due documenti scollegati | una sola offerta con le sue revisioni |

**Regola: per una revisione usa sempre `Create new version`.** Evita il
problema del `VALUE` gonfiato e non serve annullare a mano il documento vecchio.

## Dove si trova

Sul dettaglio dell'opportunità, sezione **Quotes**, ogni riga ha tre icone in
colonna `Actions`:

| Icona | Tooltip | Effetto |
|---|---|---|
| fogli sovrapposti | `Create new version` | crea `Q-000NN-AAAA/N+1`, copia header e tutte le righe, annulla la versione precedente |
| cerchio barrato | `Cancel quote` | porta la quote a `CANCELED` (chiede conferma) |
| cestino | `Delete` | cancella il documento |

Dopo il click si atterra direttamente sul dettaglio della nuova versione, con
righe, prezzi, descrizioni, payment terms, lead time, garanzia e validità già
copiati. Restano da fare solo le modifiche richieste dal cliente.

## Automatismo sullo stage dell'opportunità

Creando una versione da una quote in stato `SENT TO CUSTOMER`, l'opportunità
**avanza da sola** a `NEGOTIATION 75%` (probability 75). È corretto: stai
rinegoziando un'offerta già in mano al cliente. Non forzare lo stage a mano.

## Modificare le righe della revisione

### Eliminare una riga

Il menu **`Actions`** in alto a destra del Product list è **globale** e non
contiene il delete: dentro ci sono solo `Round to 1`, `Round to 10`,
`Round to 10 up`, `Bulk discount rate change`, `Bulk tax rate change`,
`Export quote items`, `Recalculate from price list`.

Per cancellare una riga:
1. spunta la **checkbox della riga** (prima colonna);
2. compare in basso una **barra contestuale**: `N Item | Alternative | Optional |
   Hide SW Options | 🗑`;
3. click sul **cestino** della barra → `Are you sure?` → `Confirm`.

La numerazione delle righe si ricompatta da sola (la riga 2 diventa 1, ecc.).

### Cambiare una quantità

`QTY` si edita **sulla riga padre**, non sulla sotto-riga. È l'eccezione alla
regola dei prezzi: `TRS. PRICE` e `PRICE` restano editabili solo sulla
sotto-riga `N.1` (vedi `references/custom-items.md`).

Click sul valore QTY → `cmd+a` → digita → `Return`. Ricalcolo in 3-7 secondi.

## Esempio verificato

`Q-00137-2026` (3 righe, Net 13.724,20) → il cliente riduce da 4 a 2
accelerometri → `Q-00137-2026/2`: eliminata la riga `Triax PCB 3713F1110G`,
cavo `037P50` da 4 a 2 pz. Risultato: Net **6.879,60**, IVA 22% **1.513,51**,
Gross **8.393,11 EUR**, acquisto 5.000,84, margine **27,31%**.
`Q-00137-2026` passata automaticamente a `CANCELED`, `VALUE` dell'opportunità
allineato a 6.879,60 e stage avanzato a `NEGOTIATION 75%`.
