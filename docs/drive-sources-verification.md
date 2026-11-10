# Drive sources: register and verification

Folder: **Google Drive → Automotive Electronics Guide Website Sources** (checked 10 Nov 2026).
Purpose: record what each source is used for on the site, and every correction made when cross-checking it against primary sources.

Rule for the site: sources supply facts and structure. Diagrams are redrawn. No text, figures or tables from copyrighted books, papers or ISO documents are copied.

## 1. What is in the folder

| Group | Contents | Authority | Status |
|---|---|---|---|
| Textbooks (root) | Bosch *Automotive Electrics and Automotive Electronics* 5th ed. (2007/2014); Denton *Automobile Electrical and Electronic Systems* 5th ed. (2017); Ribbens *Understanding Automotive Electronics* 7th ed. (2012); Hillier *Fundamentals of Motor Vehicle Technology – Powertrain Electronics* 5th ed. | High (published references) | Good for principles; pre-date zonal/SDV/CAN XL |
| MTech Notes / Advanced Communication Systems | Course slides 1.1–1.6 (in-vehicle networking, CAN, CAN FD, fault types, oscillator tolerance, automotive environment/EMC); Bosch iCC papers (Mutter 2013 robustness, Mutter & Hartwich 2015 error detection); ISO 11898-1…-5 (2003–2007 editions); Matheus & Königseder *Automotive Ethernet* (Cambridge); DDS and Protobuf papers | Papers: high. Slides: secondary, need checking. ISO copies: **superseded** | See corrections below |
| MTech Notes / SDV | SDV e-books (Vector, Infineon, Arrow), zonal white papers, slide decks on E/E architecture, zonal controllers, SOA, SOME/IP, Protobuf | Vendor material: good for trends, check claims | Used for Chapter 07 |
| MTech Notes / SOMEIP, AUTOSAR | AUTOSAR PRS SOME/IP, TR SOME/IP example, EXP layered architecture, AP platform design, manifest spec | High (official AUTOSAR) | Used for SOME/IP header and SD content |
| MTech Notes / Advanced Embedded Systems | Infineon AURIX training decks (TC27x/TC3xx), RTOS, JTAG, DMA, 10BASE-T1S eval kit brief | Vendor: high for that device | Candidate for a future MCU section |

## 2. Corrections found while cross-checking

| # | Source (Drive) | Claim in source | Correct statement | Checked against |
|---|---|---|---|---|
| 1 | 1.2 CAN slides | Interframe space is 7 bits | Intermission is **3** recessive bits (EOF is the 7-bit field) | ISO 11898-1 frame definition |
| 2 | 1.2 CAN slides | In an extended frame, SRR is "the bit immediately after IDE" | Order is base ID (11) → **SRR → IDE** → ID extension (18) → RTR → r1 → r0 → DLC. SRR comes *before* IDE | ISO 11898-1; CiA |
| 3 | 1.2 CAN slides | "16-bit CRC" for classical CAN | CRC **sequence is 15 bits** plus a 1-bit delimiter (16-bit CRC *field*) | ISO 11898-1 |
| 4 | 1.2 CAN slides | LLC "requests retransmission (ARQ)" | Automatic retransmission is done by the MAC; LLC does acceptance filtering, overload notification and recovery management | ISO 11898-1 |
| 5 | 1.3 CAN FD slides | RRS is "reserved bit for the bit rate switch"; RRS = 1 requests the fast data phase | RRS = **Remote Request Substitution**, always dominant (CAN FD has no remote frames). The bit-rate switch is controlled by **BRS** | CiA "CAN FD – the basic idea"; Vector e-learning |
| 6 | 1.3 CAN FD slides | Stuff count = stuff bits inside the CRC sequence, sent as 4-bit binary | Stuff count = number of **dynamic stuff bits before the CRC field, modulo 8**, sent as a **3-bit Gray code + parity bit**. The CRC field itself uses **fixed** stuff bits | CiA; ISO 11898-1:2015/2024 |
| 7 | 1.3 CAN FD slides | DLC compatible with classical CAN only for lengths ≤ 7 | DLC 0–8 are identical in both; DLC 9–15 encode 12, 16, 20, 24, 32, 48, 64 bytes in CAN FD | CiA |
| 8 | 1.2 / 1.3 slides, ISO copies in folder | ISO 11898-1:2003 as the CAN standard | Current edition is **ISO 11898-1:2024** (adds CAN XL, replaces the 2015 edition). Physical layer is ISO 11898-2:2024; the separate parts 3/4/5 of 2004–2007 are superseded | ISO catalogue |
| 9 | 1.6 Automotive environment | ECU emissions measured by stripline ISO 11452-5 and ALSE ISO 11451-2 | ISO 11452 (component) and ISO 11451 (vehicle) are **immunity** standards. Emissions: **CISPR 25** (component and on-board receivers), **CISPR 12/36** (vehicle, off-board receivers) | CISPR/ISO scope statements |
| 10 | 1.6 Automotive environment | Stripline ISO 11452-5 exposes the whole vehicle | ISO 11452-5 is a **component** stripline test; whole-vehicle radiated immunity is ISO 11451-2 | ISO 11451/11452 |
| 11 | 1.6 Automotive environment | Machine Model is one of four ESD models | MM is no longer recommended by JEDEC/ESDA; HBM and CDM are the current device-level models | JEDEC/ESDA joint publications |
| 12 | SOME.pptx | Client requests use TCP, notifications use UDP | Transport is **configured per service** (UDP or TCP for any method/event). SOME/IP-SD always uses **UDP**, default port **30490** | AUTOSAR PRS SOME/IP-SD |
| 13 | SOME.pptx | SOME/IP is a "network layer protocol" with "bandwidth up to 100 Mbps" | Application-layer middleware; it is independent of the Ethernet PHY speed (100M, 1G, 10G…) | AUTOSAR PRS SOME/IP |
| 14 | SOME.pptx | Enumeration = values indicated by its bits | Enumeration is an unsigned integer value; bitfields are the type where each bit is a flag | AUTOSAR PRS SOME/IP |
| 15 | Zonal controllers.pptx | Zone controllers do ADAS sensor fusion and infotainment and need fans/liquid cooling | In production designs zone controllers are mainly **I/O aggregation, power distribution (eFuses) and gateway** MCUs; ADAS and infotainment run on the **central/high-performance computers** | Vendor zonal white papers in the same folder (Arrow, Infineon) |
| 16 | 1.1 Introduction | 1000BASE-T1 ≈ 2019 | IEEE 802.3bp (1000BASE-T1) was published in **2016**; 100BASE-T1 (802.3bw) in 2015 | IEEE 802.3 |
| 17 | Service-Oriented Architecture.pptx | Services should be stateless | That is an IT/web guideline. Automotive services often hold state (SOME/IP **fields** with getters, setters and notifiers) | AUTOSAR PRS SOME/IP |

Items confirmed correct (sample): CAN FD CRC-17 for ≤ 16 bytes and CRC-21 above; CAN FD introduced by Bosch 2012; active error flag 6 dominant / passive 6 recessive; ESI semantics; SOME/IP header layout (Message ID, Length, Request ID, versions, type, return code); SOME/IP introduced by BMW in 2011; CAN FD oscillator-tolerance conditions (Mutter, iCC 2013).

## 3. Where this is used on the site

- **Ch 06 Networks:** CAN FD frame and error-detection table, CAN error-confinement simulator, CAN FD bit-timing and oscillator-tolerance calculator (Mutter iCC 2013 conditions 1–5), EMC test-standard table.
- **Ch 07 Software-defined vehicle (new):** E/E architecture stages, signal vs service communication, SOME/IP header builder, SOME/IP-SD sequence simulator, DDS vs SOME/IP, COVESA VSS, AUTOSAR Classic vs Adaptive.

## 4. Second pass (10 Nov 2026): folders missed in the first listing

The first listing was paginated and missed five sub-folders and about 20 root-level books. Added on this pass: **Automotive Systems** (ABS, ESP, TCS, ACC, ADAS, occupant safety, steering, suspension, x-by-wire, engine management), **Electric Vehicles** (UNECE/AIS regulations, R100 tests, hybrids, BLDC, charging standards), **EE Architecture** (CAN, LIN/FlexRay, Ethernet, OBD, UDS, CAPL, AUTOSAR), **Automotive Control Systems** (modelling, state space, cruise-control assignment) and **Embedded Systems with STM32** (ARM, GPIO, ADC, timers, UART/SPI/I²C). Root also holds Hillier books 1 and 3, Held *Inter- and intra-vehicle communications*, control and maths textbooks.

| # | Source (Drive) | Claim in source | Correct statement | Checked against |
|---|---|---|---|---|
| 18 | 03_BBN_EV_Regulations | UN R136 = hydrogen fuel-cell vehicle safety | **R136** = electric-powertrain safety of **L-category** vehicles; hydrogen vehicles are **R134** | UNECE regulation list; AIS-156 states it is based on R136 |
| 19 | 03_BBN_EV_Regulations | R100 Rev. 3 applies to M, N and L | R100 Rev. 3 covers **M and N**; L-category moved to R136 (India: AIS-038 Rev. 2 for M/N, AIS-156 for L) | UNECE; ARAI |
| 20 | 05_BBN R100 tests | (omission) | Rev. 3 also requires a **thermal-propagation** warning to occupants | UN R100 Rev. 3 / GTR 20 |
| 21 | ael_assignment cruise control | √(30² + 4·0.6·250) ≈ 37.42 and v₀ ≈ 7.42 m/s | √1500 = **38.73**, and the root must be divided by 2c = 1.2: **v₀ ≈ 7.28 m/s**; b_eff ≈ **38.7 N·s/m**; DC gain ≈ **25.8** | Arithmetic |
| 22 | Antilock braking system (ABS) | Digital wheel-speed sensors use Hall or variable reluctance and output a square wave | Variable-reluctance (inductive) sensors are passive and give a sine-like AC voltage; square-wave/current outputs come from **active** Hall or magnetoresistive sensors | Bosch book pp. 316–319 |

Confirmed correct (sample): ABS build/hold/release valve logic; ESC brakes outer front for oversteer and inner rear for understeer; ESC mandatory in the EU for all new cars from Nov 2014; R100 Rev. 3 test parameters (vibration 7–50 Hz 3 h, thermal shock +60/−40 °C × 5, crush ≥ 100 kN, short ≤ 5 mΩ, overcharge to 2× capacity, over-discharge to 25 % voltage, new overcurrent test, LPG fire option, "no venting"); isolation ≥ 100 Ω/V DC / 500 Ω/V AC; IPXXB/IPXXD; airbag timing (≈10 ms sensing, ≈30 ms inflation; Bosch book p. 63).

### Used on the site (second pass)
- **Ch 06 Chassis & safety (new):** μ-slip curves and stopping-distance simulator (Burckhardt tyre model), ABS valve phases, TCS/ESC, ESC wheel-selection figure, ACC/ADAS and SAE levels, occupant protection timing, x-by-wire.
- **Ch 02 EV:** BLDC six-step commutation figure; EV type-approval table (R100, R136, GTR 20, R10/R85/R154, AIS-038 Rev. 2, AIS-156) and R100 Rev. 3 tests.
- **Ch 03 ECUs:** microcontroller peripherals table (from the STM32/ARM and AURIX material).
- **Ch 07 Networks:** OBD-II services, DTC decoder and PID calculator.
- **Ch 11 Calculators:** nonlinear cruise-control simulation with PI controller (model from the control-systems assignment, corrected).
