# openDAQ — SDK, function block a bordo e comunicazione verso terzi

Riferimento per le domande su openDAQ applicato ai dispositivi Dewesoft: SDK
Python/C++, function block eseguiti **a bordo del dispositivo**, protocolli di
configurazione e streaming, e opzioni di dialogo con PLC e software terzi.

> **AVVERTENZA SULLE FONTI.** Alla data di questo file la documentazione
> ufficiale Dewesoft e openDAQ **non copre** i function block a bordo dei
> dispositivi Dewesoft (i tipi `DS*`), né il comportamento del server openDAQ
> OPC UA sul firmware IOLITE X. Tutto ciò che è marcato **[VERIFICATO]** è stato
> misurato direttamente su hardware reale; la data e il dispositivo sono sempre
> indicati. Non presentare questi dati a un cliente come specifica ufficiale:
> vanno confermati con support.dewesoft.com o con l'R&D. Ciò che è marcato
> **[DOC]** ha una fonte pubblica, citata.

---

## 1. L'errore da non fare: function block ≠ plugin DewesoftX

È la confusione più costosa in quest'area. Sono due piani **completamente
separati**, con capacità diverse:

| | Function block openDAQ | Plugin/Extension DewesoftX |
|---|---|---|
| Dove gira | **nel firmware del dispositivo** (DewesoftRT, ARM/Linux) | **su PC Windows**, dentro DewesoftX |
| Serve un PC? | **No** | Sì, sempre |
| Come si istanzia | `device.add_function_block("DSxxx")` via SDK openDAQ | GUI DewesoftX, Setup → Extensions/Devices |
| Licenza | nessuna licenza software separata rilevata | licenza per plugin (es. `DEWESOFT-PLUGIN-OPC-UA-CLIENT`) |
| Nomi tipici | `DSFft`, `DSEthernet`, `DSSerial`, `DSTrdp`, `DSXcpSlave` | OPC UA Client/Server, Modbus Client/Server TCP, Ethernet Receiver, Serial Com |

**Regola operativa**: se l'utente chiede cosa può fare *il dispositivo da solo*,
la risposta sta nei function block a bordo — enumerarli sul device, non citare i
plugin. Se chiede cosa può fare *la catena di misura con un PC*, allora entrano i
plugin DewesoftX. Se non è chiaro quale dei due piani interessa, **chiedere**.

Un function block con lo stesso nome di un plugin **non ha le stesse capacità**:
per esempio il plugin DewesoftX *Serial Com* supporta Modbus, CRC e richieste
Tx, mentre il function block `DSSerial` a bordo è di sola ricezione.

---

## 2. Architettura openDAQ in breve

openDAQ è un SDK modulare (C++ con binding Python) in cui tutto è un componente
del grafo: **device**, **channel**, **signal**, **function block**, **server**.
I moduli caricabili si dividono in device module, function block module e server
module.

**[DOC]** Stringhe di connessione ([openDAQ — Connect to a Device](https://docs.opendaq.com/manual/opendaq/3.30/howto_guides/howto_connect_to_device.html)):

| Prefisso | Ruolo | Porta tipica |
|---|---|---|
| `daq.nd://` | native **configuration and streaming** | 7420 |
| `daq.ns://` | native **streaming** | 7420 |
| `daq.opcua://` | **configuration** via OPC UA (companion spec openDAQ) | 4840 |
| `daq.lt://` | streaming LT (websocket) | — |
| `daq://` | universale: sceglie il protocollo migliore per quel device | — |

**[DOC]** I moduli OPC UA e LT sono stati **estratti dal repo principale** in
repo separati con la PR [#1049](https://github.com/openDAQ/openDAQ/pull/1049)
("Extract LT and OpcUa modules to remote repos"), visibile nel changelog
3.30→3.40. Restano comunque distribuiti nel wheel Python.

**[DOC]** L'information model OPC UA di openDAQ è una companion spec propria:
[openDAQ/opc-ua-companion-spec](https://github.com/openDAQ/opc-ua-companion-spec)
(NodeSet2.xml, Types.bsd, NodeId.csv).

### L'asse dei tempi è una **regola**, non una lista di istanti

**[VERIFICATO 14/09/2026]** È il concetto che spiega la maggior parte delle
domande su «perché i timestamp dei due dispositivi divergono se sono
sincronizzati PTP».

Un segnale openDAQ non porta un tempo per campione. Porta un **segnale di
dominio** con una regola lineare:

```
tempo(n) = origin + n × delta
```

`origin` è un istante assoluto ISO8601 nel `DataDescriptor`, `delta` è un intero
in tick e `tick_resolution` è il valore del tick (`Ratio`). Il timestamp non
viene **letto** da un orologio al momento del campionamento: viene **calcolato**
da un contatore di campioni.

Tre conseguenze, tutte osservate su hardware:

| Se… | Effetto | Si vede? |
|---|---|---|
| il `delta` dichiarato sbaglia di pochi ppm | errore **lineare** che cresce senza fine (30 ppm = 108 ms/ora; 262 ppm ≈ 1 s/ora) | no |
| si perde un campione | il contatore non avanza per lui: **tutto ciò che segue slitta** di 1/fs | **no**, il flusso resta regolare |
| l'`origin` è fissata prima che l'orologio sia corretto | **offset costante** per tutta la corsa | no |

**Il PTP non interviene su nessuno dei tre.** PTP disciplina l'orologio che dice
l'ora (il PHC dell'interfaccia e, con `phc2sys`, `CLOCK_REALTIME`), non il clock
che scandisce il convertitore. Un dispositivo può avere gli orologi allineati a
decine di nanosecondi e timestamp che divergono di secondi.

**Regola per rispondere a un cliente**: la sincronizzazione PTP garantisce che i
due dispositivi *diano la stessa ora se interrogati*, non che etichettino i
campioni sulla stessa scala. Perché lo facciano serve che il **clock di
campionamento** sia ricavato dalla base dei tempi sincronizzata. Gli strumenti
Dewesoft sincronizzabili lo fanno; una scheda generica con un divisore fisso su
quarzo proprio **non può**, e il suo ritmo va misurato contro il PTP e
compensato. È la differenza sostanziale fra *sincronizzato* e *sintonizzato*.

**Diagnosi**: confrontare l'ultimo timestamp ricevuto con l'orologio **della
sorgente**, mai con quello del PC che sta guardando. Un offset costante nel tempo
è una latenza o un `origin` storto; un offset che **cresce** è un errore di
ritmo, cioè `delta` sbagliato o campioni persi.

### Cosa NON esiste in openDAQ

**[VERIFICATO 02–03/09/2026]** Enumerazione completa di un'istanza openDAQ
3.40.3 (12 moduli, 18 FB type, 8 device type, 3 server type) filtrata su
`modbus | opcua | profinet | ethernet/ip | ethercat`:

- **nessun function block OPC UA** (client o server) — OPC UA esiste solo come
  *device type* `OpenDAQOPCUAConfiguration` e *server type* `OpenDAQOPCUA`
- **nessun function block né server Modbus**, in nessuna forma
- i 18 FB dell'istanza locale sono i 12 `RefFBModule*` (FFT, Statistics, Power,
  Scaling, Classifier, Trigger, Renderer, VideoPlayer, PowerReader, SumReader,
  StructDecoder, TimeDelay), i recorder CSV/Parquet, i WAV reader/writer e
  `WsStreamingServerOutletFb`

Nel wheel Python i moduli OPC UA sono `libopcua_client_module` e
`libopcua_server_module`: moduli di device/server, **non** FB module.

Se serve Modbus in openDAQ va **scritto**: il taglio corretto è un *device
module* custom (nuovo prefisso, i registri diventano channel/signal), non un
function block. Template ufficiale: [openDAQ/SimpleFBModule](https://github.com/openDAQ/SimpleFBModule).

---

## 3. Client Python openDAQ — pratica

```bash
python3 -m venv .venv && ./.venv/bin/pip install opendaq
```

**[VERIFICATO 02/09/2026]** Wheel disponibili anche per **macOS arm64**
(`opendaq-3.40.3-cp39-cp39-macosx_11_0_arm64.whl`). Versioni su PyPI a quella
data: 3.20.0/1/2/4, 3.30.0/3, 3.40.0/3.

**Allineare la versione del client all'SDK del dispositivo.** Un client 3.40 su
un device 3.20 maschera gli errori: il messaggio generico *"Failed to create
device from connection string"* diventa, con il client della stessa minor,
l'errore vero (es. *"Connection rejected - too many control clients"*). Tenere
due venv quando si fa troubleshooting.

### Trappole dei binding Python

- I dizionari di proprietà sono `IDict`: `daq.IDict.cast_from(dev.get_property_value("StartupServers"))`,
  poi `.keys()` / `.values()`. Non hanno `.get()`; hanno `__getitem__`/`__setitem__`.
  Per scrivere: `nd = daq.Dict(); nd["chiave"] = valore; dev.set_property_value(...)`
  (il costruttore **non** accetta un dict Python).
- Le cartelle di componenti vanno castate: `daq.IFolder.cast_from(dev.get_item("FB"))`,
  poi `.items`. `IComponent` non espone `.items`.
- Le proprietà di tipo selection sono `ctInt`: si scrive **l'indice**, e
  `prop.selection_values` elenca i valori ammessi.
- Procedure e funzioni: `daq.IProcedure.cast_from(v)()` e `daq.IFunction.cast_from(v)(arg)`.
- `operation_mode` vuole l'enum, non un intero: `dev.operation_mode = daq.OperationModeType.Operation`.
- Molte proprietà sono **derivate o ereditate** e rifiutano la scrittura senza
  che ciò sia un errore (es. `TxActive`, `PduSignal.Direction` eredita dal frame,
  `XcpMeasurement.SampleType` si autorileva dal segnale collegato). Avvolgere
  ogni `set_property_value` in try/except e **rileggere** il valore.
- Chiudere sempre con `inst.remove_device(dev)` e distruggere l'istanza: le
  sessioni di controllo appese saturano gli slot del dispositivo.

### Lettura dati

### Convivere con un altro client: `ClientType`

**[VERIFICATO 13–14/09/2026, OBSIDIAN-R8w]** Il tipo di client si dichiara nella
config di `add_device`, e il default è **Control**:

```python
conf = inst.create_default_add_device_config()
# impostare ClientType a ViewOnly su tutti i rami della config
dev = inst.add_device("daq.nd://<ip>", conf)
```

Un secondo client **Control** viene **rifiutato** se una sessione di controllo
esclusivo è già aperta (*"Failed to create device from connection string"*),
mentre un client **ViewOnly** convive: non tocca la configurazione e può leggere
lo streaming mentre un altro processo configura. Da usare sempre per i
visualizzatori.

Attenzione all'effetto collaterale noto: alla disconnessione **dell'ultimo
client di configurazione** il dispositivo può riportare proprietà ai valori di
default (osservato `SampleRate` a 1000 Hz e canale a `Voltage`). Un client di
sola lettura non lo provoca.

### Lettura dati

`daq.StreamReader(signal)` poi `reader.read(count, timeout_ms)`. Attenzione: se
il device è in `OperationModeType.Idle` la lettura restituisce **0 campioni** e
sembra un guasto. Verificare sempre `dev.operation_mode` prima di concludere che
qualcosa non funziona.

**Ricostruire l'asse dei tempi assoluto** — `read_with_domain` restituisce i tick
del dominio, che vanno convertiti con i parametri del descrittore, **non**
contando i campioni (un buco nel flusso sposterebbe l'asse in silenzio):

```python
dom  = signal.domain_signal
dd   = dom.descriptor
delta = int(dd.rule.parameters["delta"])
passo = dd.tick_resolution.numerator / dd.tick_resolution.denominator
fs    = 1.0 / (passo * delta)                  # fs DICHIARATA dal dispositivo
t0    = datetime.fromisoformat(dd.origin.replace("Z", "+00:00")).timestamp()
x, d  = reader.read_with_domain(reader.available_count)
t     = np.asarray(d, float) * passo + t0
```

**Usare sempre `fs` dichiarata dal descrittore, mai il nominale**: un dispositivo
onesto dichiara il ritmo che ha misurato. E rileggere il descrittore dopo ogni
cambio di modalità dell'amplificatore, perché con esso cambia anche **l'unità**
(in IEPE i canali Dewesoft dichiarano `mV`, non `V`).

---

## 4. IOLITE X — comportamento verificato

Unità di riferimento: **IOLITE-X S/N DB24032498**, HW rev 1.3.0.0, modulo IO
`MidRangeX-8xLVe_DSUB37` (8 canali AI), `MinDewesoftXVersion 2025.3`,
`NativeConfigProtocolVersion 16`, `SupportedDeviceBehaviours [Standalone, DewesoftDAQ]`.

**[DOC]** L'IOLITE X è **Ethernet-only**: 1 GbE con sincronizzazione IEEE1588v2,
daisy-chainable, ARM/Linux con DewesoftRT. **Non è uno slave EtherCAT** — il
techref *Third Party EtherCAT Masters* V26-3 elenca IOLITE Rack/Modular, SIRIUS e
KRYPTON, non l'IOLITE X. Attenzione: la pagina *tech specs* elenca fra i
protocolli "openDAQ, OPC-UA" mentre la pagina prodotto cita solo openDAQ —
**discrepanza fra fonti ufficiali, da chiarire con HQ**.

### Evoluzione firmware **[VERIFICATO 02–03/09/2026]**

| Firmware | SDK openDAQ a bordo | FB type | Note |
|---|---|---|---|
| 2026.2.0.15 | 3.20.1.34_d2f80237 | 17 | capability annunciate **solo su IPv6** ULA |
| 2026.2.5.0 | 3.20.1.34_d2f80237 | 17 | nessun FB nuovo; compare `SynchronizationChecker` |
| 2026.3.0.8 | **3.40.0.10_f3c81f8f** | **26** | salto dell'SDK 3.20→3.40: **10 FB nuovi**; capability annunciate anche su **IPv4**; compare la proprietà **`Reboot`** |

**Un aggiornamento firmware resetta la configurazione.** Osservato: `SampleRate`
20000 → 1000, `DeviceBehaviour` `DewesoftDAQ` → `Standalone`, `OperationMode` →
`Idle`. Verificare e ripristinare sempre dopo un update.

### Sample rate **[VERIFICATO 03/09/2026, fw 2026.3.0.8]**

`GetPossibleSampleRate(1000000)` → **200000**: il tetto è **200 kS/s**.
Impostando `SampleRate = 200000` il native streaming su AI 1 misura
**~203 000 Hz**. `AcqLoopRate` resta a 100 e **rifiuta ogni scrittura**.

### Server attivabili a bordo **[VERIFICATO]**

`AvailableServers = {'OpenDAQOPCUA': 'openDAQ OPC UA server'}` — è l'**unico**
server opzionale. `StartupServers['OpenDAQOPCUA']` è **`False` di default**: è
uno *startup* server, quindi si abilita e **richiede un riavvio**.

```python
nd = daq.Dict(); nd["OpenDAQOPCUA"] = True
dev.set_property_value("StartupServers", nd)
daq.IProcedure.cast_from(
    daq.IPropertyObject.cast_from(dev.get_property_value("Configuration"))
    .get_property_value("Save"))()
daq.IProcedure.cast_from(dev.get_property_value("Reboot"))()   # solo da fw 2026.3.0.8
```

Dal firmware 2026.3.0.8 la proprietà **`Reboot`** riavvia il dispositivo via
software (~10 s): sui firmware precedenti serviva un power cycle fisico, perché
non esisteva alcun metodo di reboot (`MethodSet` espone solo
`RestartAcqusition`, `GetPossibleSampleRate`, `GetErrorInformation`).

Con il server OPC UA attivo il config nativo **convive senza conflitti**:
`Srv attivi: ['OpenDAQNativeStreaming', 'OpenDAQOPCUA']` e `daq.nd://` risponde.

---

## 5. Function block a bordo — catalogo fw 2026.3.0.8 **[VERIFICATO 03/09/2026]**

26 tipi istanziabili sul dispositivo:

`AsamCmpCaptureModule`, `DSAlarm`, `DSDIPortDecoder`, `DSDecimator`,
**`DSEthernet`**, `DSExactFrequency`, `DSFatigue`, `DSFft`, `DSFirFilter`,
`DSFormula`, `DSIirFilter`, `DSIntegrationDerivation`, `DSPowerAC`, `DSPowerDC`,
**`DSSerial`**, `DSSftpClient`, `DSStatistics`, `DSStoringCSV`, `DSStoringCh10`,
`DSStoringDxd`, `DSStrainRosette`, `DSStructureToSignal`, `DSSystemMonitor`,
`DSTrackingFilter`, **`DSTrdp`**, `DSXcpSlave`.

I dieci nuovi rispetto al firmware 2026.2.x: `DSEthernet`, `DSSerial`, `DSTrdp`,
`DSFft`, `DSPowerAC`, `DSPowerDC`, `DSFatigue`, `DSExactFrequency`,
`DSTrackingFilter`, `DSStructureToSignal`. Rimosso: `AsamCmpDataSinkModule`.

Diversi FB sono **contenitori**: espongono `available_function_block_types`
propri e si configurano istanziando FB annidati.

### `DSExactFrequency` — frequenza calcolata a bordo, **con una banda di ricerca**

**[VERIFICATO 14/09/2026, OBSIDIAN-R8w fw 2026.3.19.1]** È la via per far uscire
dal dispositivo una frequenza già calcolata, senza PC e senza FFT lato client.
Struttura a contenitore: `dev.add_function_block("DSExactFrequency")` crea
*«Exact frequency math 1»*, poi serve l'istanza annidata
`add_function_block("ExactFrequencyInstance")`. **Le proprietà stanno sul
contenitore, l'istanza ha solo la porta `Input`.**

| Proprietà | Valore osservato | Cosa fa |
|---|---|---|
| `FrequencyRange` | oggetto con `Enable`, `StartFrequency`, `StopFrequency` | **banda di ricerca** |
| `BlockSize` | 0.1 (secondi) | 10 valori al secondo |
| `TrackFirstHarmonic` | False | |
| `AmplitudeThreshold` | oggetto | soglia di ampiezza |

**LA COSA DA SAPERE, e da dire sempre a un cliente**: fuori dalla banda di
ricerca il blocco **non segnala nulla** — non ha un equivalente del flag di
validità — e pubblica un numero **sbagliato e stabile**. Misurato con
`FrequencyRange` 400–600 Hz e un tono vero a 300, 600, 610, 700 e 1000 Hz:
l'uscita dava sempre **431–442 Hz con dispersione 36–53 Hz**, numeri che non
dipendono affatto dal segnale applicato. Dentro banda l'errore era **sotto
0,01 Hz** su cinque frequenze. Il **bordo superiore non è utilizzabile**: già
esattamente a 600 Hz sbagliava.

Conseguenze pratiche:

1. la banda va **letta e impostata** prima di fidarsi del valore, e allargarla
   espone il blocco al rumore di fondo — sceglierla sopra il rumore, non «il più
   larga possibile»;
2. chi consuma il valore (PLC, SCADA) deve avere una **soglia di plausibilità**
   propria: frequenza fuori da un intervallo atteso, o che salta oltre una soglia
   fra due cicli, va trattata come non valida;
3. i nodi `FrequencyRange/StartFrequency` e `/StopFrequency` sono **scrivibili
   via OPC UA**, e il cambio si perde al riavvio se non si salva la
   configurazione del dispositivo.

Gli altri due FB della stessa famiglia: `DSFft` (contenitore *«FFT math 1»*,
proprietà `AmplitudeFormat`, `Lines`, `OverlapInPercent`, `AmplitudeFunction`,
`OutputOperation`, `Window`, `Averaging`, `OutputScalarsFullRange`; uscite
`<canale>/AmplFFT` più gli scalari Rms/Peak/PeakToPeak) e `DSTrackingFilter`
(`ExtractedOrder`, `FixedBandwidth`, `SidelobeFallOff`, `FrequencySource`,
`FixedFrequencyValue`).

### `DSTrdp` — TRDP (IEC 61375) su UDP, **bidirezionale**

L'unico canale a bordo che **trasmette e riceve**. Struttura annidata:

```
DSTrdp        IpAddress, DomainSource[System|DomainReader|SoftSync], input port DomainInput
              GetAvailableIpAddresses / GetStatistics / GetSubscriptionStatistics / GetPublishStatistics
 └ TrdpFrame  ComId, IpAddress, Timeout, ByteCount, Direction[RX|TX]
              TxSchedule{TxActive, ScheduleType[Periodic], Frequency}
    └ SignalPdu  PduType[Undefined|Static|Multiplexed|MultiplexedCase|Dynamic|DynamicItem], StartByte, ByteCount
       └ PduSignal  Unit, StartBit, BitLength, SampleType[uint|int|float|boolean],
                    ByteOrder[little|big-endian], Scale, Offset, Minimum, Maximum, Direction[RX|TX]
                    TxInput{InputType[const|signal|hex|counter], ConstValue,
                            Type[Value|Evaluation|Range], Evaluation{Operator[<,≤,=,≠,≥,>], Value},
                            Range{FirstBound, SecondBound, Mode[Inside|Outside]},
                            HexValue, CounterMin, CounterMax, GetLastOutputValue}
```

**Prova di trasmissione [VERIFICATO 03/09/2026]**: ComId 1000, dataset 16 byte,
10 Hz, destinazione un host della LAN. Un client UDP indipendente ha ricevuto
**300 pacchetti in 30 s (10,0 Hz esatti)** su **UDP 17224**, 56 byte ciascuno =
header TRDP PD 40 byte + dataset 16, `protocolVersion=0x0100`,
`msgType=0x5064` ("Pd", process data), `sequenceCounter` incrementale. Le
statistiche del dispositivo confermano: `Interval/cycle 100000 us`,
`Number of packets sent 450` in 45 s, stack TRDP `0x03000000`.

Note di configurazione: `PduType` è già `Static` per default e la riscrittura
viene rifiutata; `PduSignal.Direction` eredita dal frame; i vari `TxActive` sono
derivati e rifiutano la scrittura, ma la TX parte comunque impostando
`Direction=TX` e `Frequency` sul frame.

**Perché conta**: `TxInput.InputType = signal` permette di pubblicare un segnale
calcolato a bordo (`DSFft`, `DSFirFilter`, `DSStatistics`), e i comparatori
`Evaluation`/`Range` trasformano una soglia in un booleano. È l'unico modo di
far uscire dati e decisioni dal dispositivo **senza PC**.

*Da verificare prima di un deliverable*: il layout dell'header TRDP è stato
decodificato empiricamente (40+16 byte), non confrontato con IEC 61375-2-3; la
mappatura del payload sul singolo signal e la direzione **RX** non sono state
dimostrate.

### `DSXcpSlave` — XCP su TCP, **sola lettura**

Server XCP sul dispositivo, `TransportLayers.TcpTransportLayer{IpAddress, Port}`
(default **5555**). Espone `GenerateMeasurements`, `ClearMeasurements`,
`GenerateA2L`, `GetConnectionStatus`, più `Clocks{LocalClock, AbsoluteClock}`,
`TimeShift` e `CompatibilityMode[Normal|Not packed]`. Si aggiungono FB annidati
`XcpMeasurement` con `Address`, `SampleType[Unknown…Float64]` e un **input port**
in cui instradare il segnale.

**[VERIFICATO 03/09/2026]** Handshake con un master XCP reale (socket stdlib):

```
CONNECT (0xFF)                 OK  ff0400ffbc050101
GET_STATUS (0xFD)              OK  ff4000000000
GET_DAQ_PROCESSOR_INFO (0xDA)  OK  ff13ffff07000080
GET_DAQ_RESOLUTION_INFO (0xD9) OK  ff01ff01ff2c0100
```

`RESOURCE = 0x04` → **DAQ sì, STIM no**: il master **legge e non scrive**. Byte
order Intel, `MAX_CTO 255`, `MAX_DTO 1468`, protocollo v1, transport v1, DAQ
dinamico con prescaler e timestamp a 4 byte, `MAX_DAQ 65535`,
`MAX_EVENT_CHANNEL 7`. `GenerateA2L` ha prodotto un A2L di **43 751 caratteri**
(`ASAP2_VERSION 1 70`, `PROJECT XCP_SLAVE_PLUGIN`, `MODULE XCP_DEVICE`).

Uso: telemetria verso strumenti XCP (CANape, INCA). **Non** come canale di
comando da un PLC, perché manca STIM.

### `DSEthernet` — cattura pacchetti, **sola ricezione**

`NetworkAdapters` (selection su `[eth1, eth0]`), un `Filter chain` annidato
creato automaticamente che emette un signal `Ethernet`, e dentro FB `FilterFb`
con `SourceIP`, `DestinationIP` e `Protocol{ProtocolType[None|UDP], SourcePort,
DestinationPort}`.

**Nessun input port → non trasmette. Il protocollo è None o UDP: niente TCP.**
Quindi **non si può implementare Modbus TCP a mano** con questo FB. Si abbina a
`DSStructureToSignal` per decodificare il byte stream in signal tipizzati.

### `DSSerial` — seriale, **sola ricezione**

`RefreshPorts` più FB annidati `SerialPort` con `AvailablePorts`, `Port`,
`SignalName`, `SerialPortsFound`, `BaudRate[4800…921600]`,
`ParsingMode[Delimiter|FixedLength]`, `Delimiter` (default `\CR\LF`),
`FixedLength`, `PreviewData`, `RefreshPreview`; un signal per porta.

**Solo ricezione: nessun Tx, nessun CRC, nessun Modbus** — molto più povero del
plugin DewesoftX *Serial Com*. Sull'unità 8xLVe DSUB37
`SerialPortsFound = False`: **nessuna porta seriale fisica**, quindi il FB è
inutilizzabile su quel modulo.

---

## 6. Il server openDAQ OPC UA sul dispositivo

**Non usa internet.** È un server TCP in ascolto sulla **porta 4840** del
dispositivo, protocollo **OPC UA binario** (`opc.tcp://`), raggiunto in LAN sullo
stesso segmento Ethernet. Nessun cloud, nessun broker, nessun DNS pubblico: la
scoperta avviene via **mDNS** in multicast locale e il traffico è client→device
diretto. Il server è costruito su **open62541** (namespace
`urn:open62541.server.application`).

Namespace esposti **[VERIFICATO]**:

```
[0] http://opcfoundation.org/UA/
[1] urn:open62541.server.application
[2] http://opcfoundation.org/UA/DI/
[3..6] https://docs.opendaq.io/specifications/opc-ua/daq/{bt,bsp,device,esp}
[7] https://docs.opendaq.io/specifications/opc-ua/daq/vendor/hbk
```

L'address space segue **OPC UA DI**: `DeviceSet` → `Dewesoft_<serial>` con
identità, proprietà di configurazione e un `MethodSet`.

### Cosa trasporta, per firmware **[VERIFICATO]**

| Firmware | Nodi valore dei canali |
|---|---|
| 2026.2.x | il ramo `IO`/`Sig` espone **solo metadati** di componente; nessun valore misurato |
| **2026.3.0.8** | i canali sono esposti: `/<device>/IO/1/AI1/Sig/AI/Value` (con figlio `DataDescriptor`) e `AnalogValue`, più un ramo `/Sig/` con i signal di device (`CPUTemperature`, `TotalSamples`, `ClockFrequency`, `VCXOValue`, `SyncError`, `PhaseError`, `TimeLock`, `RealtimeCoreUsage`, `AcqLoopTime`, `DeviceDomain`) |

### Ma non è streaming — il tetto è 10 Hz **[VERIFICATO 03/09/2026]**

Con acquisizione attiva, una subscription su `AI1/…/Value` consegna dati veri.
Misura del rate reale al variare del publishing interval richiesto:

| Publishing interval richiesto | Rate reale |
|---|---|
| 1 ms | **10,0 Hz** |
| 10 ms | **10,0 Hz** |
| 100 ms | **10,0 Hz** |
| 200 ms | 5,0 Hz |

**Il tetto di ~10 Hz non dipende dall'acquisition rate**: verificato con
`SampleRate` da 1 kHz **e** da 200 kHz, con native streaming misurato a
203 000 Hz. Rapporto di decimazione fino a **~20 000×**. Ogni notifica porta un
**singolo scalare** (`is_array: False`), senza timestamp per campione né
garanzia di continuità del record. `AcqLoopRate` non è una leva: rifiuta la
scrittura.

Coerentemente, il dispositivo **dichiara** la capability come
`ProtocolType.Configuration`, non `ConfigurationAndStreaming`.

**Come presentarlo**: OPC UA sul dispositivo è un piano di **supervisione** —
valori istantanei, stati, soglie, allarmi a ~10 Hz. Non è un trasporto dati di
misura. Per la forma d'onda servono native streaming o LT.

### Tre trappole che bloccano un cliente PLC **[VERIFICATO 13–14/09/2026, OBSIDIAN-R8w e device openDAQ custom]**

**1. `ValueRank = -2` — è quella che ferma TwinCAT.** I nodi valore sono
dichiarati con `ValueRank -2` ("Any": scalare oppure array di rango qualsiasi).
È legale, ma un PLC deve allocare un'immagine di processo di **dimensione
fissa**, e "Any" non gli dice quanti byte servono: il client OPC UA di TwinCAT
non lo digerisce. Cambiarlo alla sorgente vorrebbe dire patchare il modulo OPC UA
di openDAQ e ricompilarlo per il target. La via praticabile è una **passerella**
(vedi §7).

**2. I nodi sotto `/FB/` non sono browsabili.** `get_children()` non enumera la
cartella intermedia, quindi un percorso di browse **non risolve** e si conclude
erroneamente che il valore non sia esposto. Vanno indirizzati **per NodeId
esplicito**, che contiene il numero di serie del dispositivo:

```
ns=4;s=/Dewesoft_<serial>/FB/DSExactFrequency_1/FB/ExactFrequencyInstance_1/Sig/Frequency/Value
```

**3. I metodi vanno chiamati passando il NODO, non la stringa.** Con
`call_method("4:Save", ...)` il server risponde **`BadNoMatch`**. Corretto:

```python
cfg = client.get_node("ns=4;s=/Dewesoft_<serial>/Configuration")
for m in await cfg.get_methods():
    if (await m.read_browse_name()).Name == "Save":
        await cfg.call_method(m, "<nome-configurazione>")
```

Il nodo `Configuration` espone `Save`, `Load`, `New`, `Delete` e
`GetCurrentConfiguration`: **senza `Save` ogni modifica scritta via OPC UA si
perde al riavvio**.

### Sicurezza — attenzione **[VERIFICATO]**

Endpoint di default: **`SecurityPolicy None`, `SecurityMode None`,
`UserTokenType Anonymous`**. Il server logga *"Unconfigured AccessControl. Users
have all permissions"* e *"AcceptAll Certificate Verification"*. I nodi di
configurazione sono **scrivibili** (AccessLevel read+write): un client OPC UA
qualsiasi in LAN può leggere e **modificare** la configurazione del dispositivo.
Da segnalare sempre quando si propone questa strada in un contesto industriale.

### Limite noto: il client OPC UA di openDAQ non si collega

**[VERIFICATO 02–03/09/2026]** `daq.opcua://<ip>` verso questo dispositivo
falisce con **`BadDecodingError`** dopo aver aperto il secure channel e attivato
la sessione. Provato con client 3.20.1 e 3.40.3, e con SDK a bordo sia 3.20.1.34
sia 3.40.0.10: **non è un disallineamento di versione**. Il canale OPC UA è
quindi usabile **solo da client OPC UA generici** (es. `asyncua`, UaExpert, un
client PLC), non dall'SDK openDAQ. `daq://<mdns-name>` funziona perché ricade sul
native. **Da aprire come segnalazione con l'R&D.**

---

## 7. Dialogo con un PLC — opzioni e confronto

### Interamente a bordo, senza PC

| | Direzione | Trasporto | Stato verifica |
|---|---|---|---|
| **`DSTrdp`** | **RX + TX** | UDP, TRDP PD, porta 17224 | **TX verificata**, 10 Hz, 450 pacchetti |
| `DSXcpSlave` | solo device → master | TCP 5555 | **verificato**, ma `STIM=0`: sola lettura |
| server OPC UA | lettura + scrittura config | TCP 4840 | **verificato**, valori a ~10 Hz |
| `DSEthernet` | solo RX | UDP / Ethernet raw | struttura verificata, **no TCP** |
| `DSSerial` | solo RX | RS-232/485 | nessuna porta su 8xLVe |

### Il pattern «passerella» quando il PLC non digerisce il server nativo

**[VERIFICATO 14/09/2026]** Soluzione applicata in campo quando TwinCAT non
riesce ad allocare l'immagine di processo per via del `ValueRank -2` (§6): un
piccolo server OPC UA intermedio che **legge da client** i server dei
dispositivi e **ripubblica gli stessi valori** come scalari dichiarati
(`ValueRank -1`, `ArrayDimensions` vuoto), con nomi leggibili e su un unico
endpoint. Non calcola e non converte niente.

Cosa aggiungere perché sia utile al PLC, imparato sul campo:

- un **`Heartbeat`** che avanza a ritmo noto: un server vivo con dati fermi è il
  guasto più insidioso, e la sola presenza dell'endpoint non lo rivela;
- per **ogni sorgente** un `Online` (booleano, vero se ha risposto entro una
  scadenza dichiarata) e un `AgeSeconds`;
- le bandiere di validità convertite in **Boolean veri**: i dispositivi le
  pubblicano spesso come Float64 0.0/1.0, che un PLC non vuole leggere così.

La passerella può anche ospitare **nodi scrivibili dal PLC** (`set_writable()`
in `asyncua`), utili per far tornare indietro lo stato dell'automazione e
mostrarlo all'operatore. Due avvertenze misurate: TwinCAT **non compila
`SourceTimestamp`**, quindi per sapere da quanto il PLC non scrive si usa
`ServerTimestamp`, che il server registra e conserva a ogni scrittura; e quel
timbro va confrontato con un **altro timbro dello stesso server** (per esempio
quello dell'`Heartbeat`, letto nella stessa risposta), mai con l'orologio del PC
che guarda, che può stare su una scala diversa.

Costo da dichiarare sempre: è un anello in più. Se il processo si ferma, il PLC
non vede nulla anche con i dispositivi perfettamente funzionanti.

### Con DewesoftX su PC **[DOC]**

| Plugin | Manuale | Capacità chiave |
|---|---|---|
| OPC UA Client | V25-1 (06/02/2025) | legge da qualsiasi server terzo, subscription, **scrive** su nodi RW, metodi senza argomenti; canali asincroni, publishing interval consigliato 100 ms; licenza `DEWESOFT-PLUGIN-OPC-UA-CLIENT` |
| OPC UA Server | V24-2 (13/08/2024) | pubblica canali analog/math/metadata "used"; anonimo o user/password; None / Sign / Sign&Encrypt; scrittura esterna su Input control e Data header da v4.1; licenza `DEWESOFT-PLUGIN-OPC-UA-SERVER` |
| Modbus Client TCP/IP | V23-1 (06/01/2023) | Coils RW, Discrete Inputs RO, Input Registers RO, Holding Registers RW; Int16/Int16s/Int32/Int32s/Float32; Word Swap; **scrittura** su coils e holding registers; avviso oltre 100 Hz; **solo TCP, no RTU** |
| Modbus Server TCP/IP | V23-1 (06/01/2023) | mappatura manuale canale→indirizzo, range 0–65535; Int16/32 signed/unsigned, Float32, word swap; porta default **502**, Unit ID 0–255 o All; legge i canali a ogni ciclo (default 20 ms) → *"only for relatively slow sampling rates in the range of some Hz"*, **max teorico 50 Hz** |
| Serial Com | V26-1 | RS-232/RS-485, 1200–115200 e rate custom; **bidirezionale** con trigger On Start/On Stop/polling/canale utente; **protocolli NMEA-0183, Modbus**, ASCII/binario custom; delimitatori o lunghezza fissa; IEEE 754; big/little endian; **CRC**; ciclo ~33 ms |
| Ethernet Receiver | manuale online | **solo ricezione**; UDP e Ethernet frame; filter chain per MAC/IP/tipo; Intel/Motorola/ASCII; signed, unsigned, IEEE float, MIL-STD 1750A; scaling lineare o polinomiale fino al 7° ordine; header IENA; canali asincroni; **Dewesoft Ethernet License** |
| Ethernet Transmitter | manuale online | **solo invio, solo UDP**, unicast/multicast/broadcast; canali analogici, digitali e calcolati + tempo assoluto UTC; config esportabile in **XML**; dichiarato per *"low-speed statistical parameters (1 to 100 Hz)"* |

**Nota importante**: la tabella dei function code nel manuale Modbus Client
associa 0x03 a Input Registers e 0x04 a Holding Registers, **invertito rispetto
allo standard Modbus** (0x03 = Read Holding Registers, 0x04 = Read Input
Registers). Probabile errore editoriale: verificare sul banco al primo
collegamento e segnalare a HQ.

### Lato Beckhoff / TwinCAT **[DOC]**

| Prodotto | Cosa dà |
|---|---|
| [TF6100 OPC UA Client](https://infosys.beckhoff.com/content/1033/tf6100_tc3_opcua_client/index.html) (man. v1.3.0, 08/04/2026) | FB PLCopen: `UA_Connect`, `UA_Disconnect`, `UA_GetNamespaceIndex`, `UA_NodeGetHandle`, `UA_NodeReleaseHandle`, `UA_Read`, `UA_Write`, `UA_MethodGetHandle`, `UA_MethodCall`, `UA_MethodReleaseHandle` |
| [TF6250 Modbus TCP](https://www.beckhoff.com/en-en/products/automation/twincat/tfxxxx-twincat-3-functions/tf6xxx-connectivity/tf6250.html) | **server e client**; libreria PLC `FB_MBReadCoils`(1), `FB_MBReadInputs`(2), `FB_MBReadRegs`(3), `FB_MBReadInputRegs`(4), `FB_MBWriteSingleCoil`(5), `FB_MBWriteSingleReg`(6), `FB_MBWriteCoils`(15), `FB_MBWriteRegs`(16), `FB_MBReadWriteRegs`(23), `FB_MBDiagnose`(8); licenza TC1200 |
| [TF6310 TCP/IP](https://infosys.beckhoff.com/content/1033/tf6310_tc3_tcpip/84134027.html) (man. v1.5.2, 02/12/2025) | socket TCP e UDP nel PLC: `FB_SocketUdpCreate`, `FB_SocketUdpSendTo`, `FB_SocketUdpReceiveFrom`, `FB_ConnectionlessSocket` — la via per ricevere/inviare frame TRDP o UDP grezzo |

### Criterio di scelta

- Anello di controllo **veloce e deterministico** → EtherCAT su un dispositivo
  che lo supporta (IOLITE Rack/Modular, SIRIUS, KRYPTON), **non** IOLITE X.
- Scambio **bidirezionale a bordo, senza PC**, con latenza minima → `DSTrdp` +
  TF6310. Prezzo: UDP non garantisce la consegna, servono contatore di sequenza
  e watchdog nel PLC, e l'endianness si gestisce a mano.
- **Supervisione** con metadati di canale → OPC UA (a bordo a ~10 Hz, oppure
  plugin DewesoftX se serve di più).
- Poche grandezze a pochi Hz, con un PC nella catena → Modbus TCP, il più
  semplice da cablare ma senza metadati e con le trappole di word order e
  indirizzamento 0-based/1-based.

---

## 8. Troubleshooting verificato

| Sintomo | Causa e rimedio |
|---|---|
| DewesoftX: *"device already taken"*; openDAQ: **`Connection rejected - too many control clients`** | il dispositivo limita i client di **configurazione**. Lo streaming (`daq.ns://`) resta disponibile. Cercare **altri PC o VM in LAN** collegati: il caso reale era un altro PC, non il server OPC UA e non le sessioni locali. Il device **non espone** `ActiveClientConnections` via OPC UA e ha le diagnostiche di sessione OPC UA disabilitate, quindi **non si può sapere chi occupa gli slot né forzarne la chiusura**: unico rimedio è spegnere i client e riavviare. Attenzione alle VM: una DewesoftX dentro Parallels in rete *shared* non compare in `lsof`/`netstat` dell'host macOS. |
| `StreamReader` restituisce 0 campioni | `operation_mode` è `Idle` (tipico dopo un reboot o un update firmware). Impostare `daq.OperationModeType.Operation`. |
| Nodi OPC UA a `None` | stessa causa: dispositivo non in acquisizione. Verificare **prima** via native streaming. |
| Errore generico *"Failed to create device from connection string"* | usare un client openDAQ della stessa minor dell'SDK a bordo per vedere l'errore reale. |
| `daq.opcua://` → `BadDecodingError` | limite noto (§6): usare un client OPC UA generico, o il native. |
| Porta 4840 chiusa con capability annunciata | `StartupServers['OpenDAQOPCUA'] = False`, oppure abilitato ma non ancora riavviato. |
| Discovery non trova il device via IPv4 | sui firmware ≤ 2026.2.5.0 le capability sono annunciate **solo su IPv6** ULA. Connettersi con la stringa IPv4 esplicita o aggiornare il firmware. |
| Il client OPC UA del PLC non riesce a mappare i nodi | i valori sono dichiarati `ValueRank -2` ("Any") e TwinCAT non alloca l'immagine di processo. Passerella che ripubblica come scalari (§6, §7). |
| Un nodo che «non esiste»: il browse non lo trova | i nodi sotto `/FB/` non sono enumerabili. Indirizzarli per NodeId esplicito (§6). |
| `BadNoMatch` chiamando un metodo | il metodo è stato passato come stringa `"4:Nome"`. Va passato l'oggetto nodo (§6). |
| Una modifica scritta via OPC UA sparisce al riavvio | manca la chiamata a `Configuration/Save` con il nome della configurazione attiva. |
| Il secondo client openDAQ viene rifiutato | il primo ha preso il controllo. Aprire il secondo come `ClientType` **ViewOnly** (§3). |
| Le impostazioni tornano ai default da sole | è successo alla disconnessione dell'ultimo client di **configurazione**. Usare client di sola lettura per visualizzare. |
| Un FB creato dopo l'avvio non si vede in OPC UA | il server espone solo i FB presenti al **proprio** avvio, e ciclare `Srv/OpenDAQOPCUA/Active` non ricostruisce l'address space: prima la configurazione, poi il server. |
| I timestamp dei due dispositivi divergono benché siano sincronizzati PTP | l'asse dei tempi è una **regola** `origin + n × delta` (§2). Offset costante → latenza o `origin`; offset che **cresce** → `delta` sbagliato o campioni persi. |

Porte utili sull'IOLITE X: **22** (SSH, OpenSSH 10.3 con publickey/password —
credenziali non pubbliche, chiederle a Dewesoft), **4840** (OPC UA, se
abilitato), **7420** (native config e streaming).

---

## 9. Metodo consigliato per rispondere in questa area

1. **Non citare a memoria** un function block o una sua proprietà: enumerarli
   sul dispositivo reale, perché cambiano con il firmware.

   ```python
   inst = daq.Instance(); dev = inst.add_device("daq.nd://<ip>")
   print(dev.info.software_revision, dev.info.sdk_version)
   print(sorted(dev.available_function_block_types.keys()))
   ```

2. **Distinguere sempre** il piano dispositivo (FB) dal piano PC (plugin).
3. **Verificare l'acquisizione** prima di dichiarare che qualcosa non funziona.
4. **Dichiarare la provenienza**: per i FB `DS*` e per il server OPC UA del
   dispositivo non esiste documentazione ufficiale. Ogni dato va accompagnato da
   firmware, dispositivo e data della misura, e indirizzato a
   support.dewesoft.com per conferma.
5. **Lasciare il dispositivo come l'hai trovato**: rimuovere i FB istanziati per
   prova, ripristinare `StartupServers`, `SampleRate` e `OperationMode`.
6. **Su qualsiasi domanda di sincronizzazione, separare tre cose** che i clienti
   (e chi risponde) confondono di continuo: gli **orologi** allineati dal PTP;
   il **clock di campionamento**, che il PTP non tocca a meno che il dispositivo
   non lo derivi dalla base dei tempi; e i **timestamp**, che sono calcolati da
   una regola e possono sbagliare per entrambi i motivi più la perdita di
   campioni. Una risposta che dice solo «sono sincronizzati PTP» non è una
   risposta.

## Fonti

**Documentazione pubblica**: [openDAQ docs](https://docs.opendaq.com/manual/opendaq/3.30/howto_guides/howto_connect_to_device.html) ·
[openDAQ/openDAQ](https://github.com/openDAQ/openDAQ) e PR [#1049](https://github.com/openDAQ/openDAQ/pull/1049) ·
[opc-ua-companion-spec](https://github.com/openDAQ/opc-ua-companion-spec) ·
[SimpleFBModule](https://github.com/openDAQ/SimpleFBModule) ·
[IOLITE X](https://dewesoft.com/products/iolite-x) e [tech specs](https://dewesoft.com/products/iolite-x/tech-specs) ·
[Third Party EtherCAT Masters V26-3](https://downloads.dewesoft.com/manuals/dewesoft-3rd-party-ethercat-masters-manual.pdf) ·
manuali plugin: [OPC UA Client V25-1](https://downloads.dewesoft.com/manuals/dewesoft-opc-ua-client-manual-en.pdf),
[OPC UA Server V24-2](https://downloads.dewesoft.com/manuals/dewesoft-opc-ua-server-manual-en.pdf),
[Modbus Client TCP/IP V23-1](https://downloads.dewesoft.com/manuals/dewesoft-modbus-client-tcp-ip-manual-en.pdf),
[Modbus Server TCP/IP V23-1](https://downloads.dewesoft.com/manuals/dewesoft-modbus-server-tcp-ip-manual-en.pdf),
[Serial Com V26-1](https://downloads.dewesoft.com/manuals/dewesoft-serialcom-plugin-manual-en.pdf),
[Ethernet Receiver](https://manual.dewesoft.com/x/setupmodule/extensions/ethernet-receiver),
[Ethernet Transmitter](https://manual.dewesoft.com/x/setupmodule/devices/ethernet-transmitter) ·
Beckhoff [TF6100](https://infosys.beckhoff.com/content/1033/tf6100_tc3_opcua_client/index.html),
[TF6250](https://www.beckhoff.com/en-en/products/automation/twincat/tfxxxx-twincat-3-functions/tf6xxx-connectivity/tf6250.html),
[TF6310](https://infosys.beckhoff.com/content/1033/tf6310_tc3_tcpip/84134027.html).

**Evidenza sperimentale**: sessioni Cowork del 02–03/09/2026 su IOLITE-X
S/N DB24032498 (firmware 2026.2.0.15 → 2026.2.5.0 → 2026.3.0.8), script e log in
`~/Developer/DEWESOFT/opendaq-opcua-probe` sulla macchina di Alberto Boffi
(`recheck_fw.py`, `fb_tree.py`, `test_trdp_tx.py`, `client_trdp_listen.py`,
`test_xcp_server.py`, `client_xcp.py`, `client_opcua_ai_sub.py`,
`client_opcua_rate.py`, `plot_ai1_opcua.py`, `max_rate.py`). Esempi openDAQ di
riferimento in `~/Developer/DEWESOFT/opendaq-example-codes` (trattini, non
underscore).

Sessioni del **13–14/09/2026** sul banco della demo CNR-INM (OBSIDIAN-R8w
S/N DB24049506 firmware 2026.3.19.1 + device openDAQ custom su BeagleBone Black):
`DSExactFrequency` e la sua banda di ricerca, `ValueRank -2` verso TwinCAT e il
pattern passerella, `ClientType` ViewOnly, regola del dominio e diagnosi delle
derive di timestamp. Repo `~/Developer/DEWESOFT/opendaq-bbb-bookworm`
(`opendaq-device/banda_obsidian.py`, `dstrack/plc/gateway_opcua.py`,
`dstrack/sources/opendaq_raw.py`, `dstrack/transport/plc_stato.py`).
