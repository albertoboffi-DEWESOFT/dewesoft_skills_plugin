# Mappa del catalogo (Configurator) e fatti prodotto verificati

Prezzi e stock osservati il **2026-08-24** con price list **END_ITA 2025**.
I prezzi cambiano con la versione di listino: **rileggili sempre a schermo**,
non citare da qui come se fossero attuali.

## Struttura del Configurator

Categorie di primo livello: SIRIUS, IOLITE, OBSIDIAN, KRYPTON, DEWE-43,
MINITAURs, NEMOSENSE, CAN instruments, Navigational products,
General accessories, Aerospace instruments, Sensors, Shakers,
Warranty & Calibration, Educational packages, DEMO Training and EXPO, Software,
Promotional, Spare parts, Custom item, MBDA, Custom upgrades, CRM custom items.

Sotto **SIRIUS**: Modular, Waterproof, Mini, Real-time Systems,
Portable all-in-one systems, Compact Systems,
High-channel rack mountable systems, XHS-PWR, Rack accessories, SBOX.

Sotto **SIRIUS > Modular**: Dual Core, High Speed, High Density,
Dual Core EtherCAT, High Speed EtherCAT, High Density EtherCAT,
eXtra High Speed, **SIRIUS X**.

Ricerca prodotto: `CMD+SHIFT+S` (il campo in sidebar è solo l'etichetta della
scorciatoia, cliccarlo non apre nulla). La ricerca è per **codice**, non per
descrizione libera.

Pagina prodotto: tab `DESCRIPTION / GALLERY / UPGRADES / ACCESSORIES / SOFTWARE
/ FILES` e, in DESCRIPTION, Tariff code, Reference number, Included software,
Base price, Software price, Total price, Weight, Software/Hardware/Slice
upgrades, e un box di avvertenze del prodotto. Il badge numerato colorato sulle
card è la **disponibilità a magazzino** (verde = alta, arancio = bassa,
rosso = 0); l'icona `i` apre le info.

## Trappole di naming (verificate)

- **`SIRIUSX` non esiste come stringa in catalogo.** Il ramo corretto è
  `SIRIUS > Modular > SIRIUS X`. Cercare "SIRIUSX" in Quick Add o nella ricerca
  del Configurator restituisce zero risultati.
- **`XHS-PWR` NON è un alimentatore.** È il **power analyzer**
  `SIRIUSi-XHS-PWR-1xHV-1xDC-CT-*` (1 ingresso HV fino a 2000 V + 1 DC-CT),
  12.832,00 EUR nelle tre varianti viste (`-1000A-CON` con connettori PowerLok
  500 Series, `-1000A-UNI` e `-250A-UNI` con harness HV universale).
  Sotto `SIRIUS > XHS-PWR` ci sono `Instruments` e `Accessories`.
- `SIRIUS XHS` (eXtra High Speed) è una famiglia distinta da `SIRIUS X`. Slice
  XHS viste: `SIRIUSi-XHS-4xHV-4xLV` 20.094,00, `SIRIUSi-XHS-4xHV-4xLV-8xCNT`
  22.644,00, `SIRIUSi-XHS-8xACC` 18.913,00, `SIRIUSi-XHS-8xACC-8xCNT`
  21.463,00, `SIRIUSi-XHS-8xHV` 20.528,00, più varianti `-VT` (Variable
  Trigger), `-8xCHG-8xCNT`, `-BAN`, `-BAN-8xCNT-VT (IP3)`.

## SIRIUS X — moduli (END_ITA 2025)

| Codice | Prezzo | Note |
|---|---|---|
| `SIRIUS-X-16xUNI` | 18.750,00 € | 16 ch CH-GND isolati: Voltage, Strain, IEPE, Resistance, Temperature, Current, Potentiometer. Tariff code 90303370. Software incluso: DEWESOFT-X-PROF, DEWESOFT-OPT-CAN, DEWESOFT-OPT-CAN-FD (e altri). Peso 2,00 kg |
| `SIRIUSf-X-16xACC` | 12.863,00 € | 16 ch isolati per Voltage, IEPE |
| `SIRIUSf-X-16xLVe` | 12.428,00 € | 16 ch isolati Low Voltage, Current, Potentiometer, connettori D-SUB9 femmina |
| `SIRIUSf-X-16xLVe-TB` | 10.803,00 € | come sopra, terminal block |
| `SIRIUSf-X-16xSTGS` | n.d. | strain gauge |
| `SIRIUSf-X-16xSTGS-TB` | n.d. | strain gauge, terminal block |
| `SIRIUSf-X-32xLV` | n.d. | 32 ch low voltage |
| `SIRIUSi-X-8xUNI` | n.d. | 8 ch universale |
| `SIRIUSif-X-8xCAN-FD` | n.d. | 8 ch CAN-FD |

Prezzi visti anche su card senza etichetta nella stessa pagina: 12.003,00,
10.807,00, 9.682,00, 17.709,00 € — da riassociare al codice leggendo la card.

**Avvertenze `SIRIUS-X-16xUNI`** (dal box prodotto, testuali):
non supportati **ECAT IN/OUT** e **SD card (Logging)**. La linea SIRIUS X è
stata aggiornata con nuovi connettori Lemo; **tutti gli alimentatori L1B2f sono
compatibili**; il power chaining è disponibile **solo** con
`L1B2mB-L1B2fL-Xm`.

## SIRIUS X — accessori

Sottocategorie: Power supplies, Power daisy chain cables, USB cables,
Network switches, Standard ethernet cables, Connector sets, Calibration,
Cases and bags, Mounting plates.

**Power supplies** (`SIRIUS > Modular > SIRIUS X > Accessories > Power supplies`):

| Codice | Prezzo | Stock 2026-08-24 |
|---|---|---|
| `PS-120W-L1B2f` | 160,00 € | 461 |
| `PS-220W-L1B2fL-56V` | 238,00 € | 0 |
| `PS-60W-L1B2f` | 104,00 € | 152 |

Tutti "AC/DC power supply adapter". Default sensato per un modulo SIRIUS X a 16
canali: **`PS-120W-L1B2f`** (compatibile, disponibile, potenza intermedia).
Verifica sempre con `dewesoft-technical-expert` se la configurazione richiede
più potenza o power chaining.

Altri alimentatori presenti in anagrafica ERP (visti via Quick Add, appartengono
ad altre famiglie di prodotto): `RAC.0000239.000 PS-200W-L1B2f`,
`RAC.2040031.000 PS-450W-L2B2f`, `RPS.3500032.000 PS-220W-L1B2fL-56V`,
`RPS.3500031.000 PS-220W-OPEN-56V`.

## Regola d'oro

Quando l'utente nomina un prodotto con un nome "parlato" (SiriusX, Sirius XHS,
Krypton...), **non assumere il codice**: naviga il ramo del Configurator, leggi
i codici a schermo e proponi la scelta con prezzi e disponibilità. Se il nome è
ambiguo tra due famiglie, chiedi.

## OBSIDIAN e IOLITE rack (END_ITA 2025, letti 2026-09-21)

Le **slice IOLITE rack non sono articoli autonomi**: nel Configurator esistono
solo come configurazione dentro un chassis. `IOLITE > IOLITE rack` contiene solo
i chassis (`IOLITE R12`, `IOLITE R8`, `IOLITE R8r`); le slice compaiono nella
sidebar sotto il chassis OBSIDIAN selezionato, con il badge di stock, e un click
le **aggiunge alla configurazione** (non naviga alla scheda prodotto).

| Codice | Prezzo | Stock | Note |
|---|---|---|---|
| `OBSIDIAN-R12` | 6.200,00 EUR | 0 | chassis 19" fino a 12 slice IOLITE, ECAT ridondante, tariff code 90303900. Scope of supply: `PS-120W-L1B2f` + `RJ45-3m`. Software incluso: DEWESOFT-X-PROF, OPT-CAN, OPT-CAN-FD |
| `OBSIDIAN-R12-GPS-1kHz` | 5.981,79 EUR | 0 | |
| `OBSIDIAN-R12-GPS-10kHz` | 6.816,67 EUR | 0 | |
| `IOLITEr-16xAO` | 2.197,00 EUR | 0 | 16 ch analog output |
| `IOLITEr-16xLV` | 2.197,00 EUR | 0 | 16 ch low voltage |
| `IOLITEr-32xDO` | 900,00 EUR | 0 | 32 ch digital output |
| `IOLITEr-8xLVe` | 3.073,00 EUR | 26 | 8 ch low voltage, connettore **DSUB9 femmina** |
| `IOLITEr-8xUNI-D37` | 6.017,86 EUR | 0 | 8 ch universale, connettore **D37** |
| `DSIi-10A` (`RAD.3500257.000`) | 417,00 EUR | 0 | adattatore DSI isolato per misura di corrente; ingresso BAN, **uscita DSUB9**; fino a 10 A (0,5%), banda 100 kHz, CAT III 600 V, TEDS |

**Trappole verificate:**

- **`IOLITEr-8xUNI` non esiste** come slice OBSIDIAN: l'unica variante UNI rack
  e' `IOLITEr-8xUNI-D37`.
- Gli **adattatori DSI escono su DSUB9**: non si collegano a una slice `-D37`
  senza un breakout D37 -> 8x DSUB9, che a catalogo non c'e'. Per una misura di
  corrente con adattatori DSI su rack, la slice con il connettore giusto e'
  `IOLITEr-8xLVe`.
- Lo `OBSIDIAN-R12` avverte che in **standalone** un rack pieno non riesce a
  salvare tutti i canali a 20 kHz: ridurre sample rate o canali storati.
- La lista completa delle slice compatibili con OBSIDIAN-R12 (32 codici, dalle
  `IOLITEhir-4x*` a `IOLITEr-JUMPER`) e' leggibile a schermo nella sidebar del
  chassis, con lo stock accanto a ogni codice.
