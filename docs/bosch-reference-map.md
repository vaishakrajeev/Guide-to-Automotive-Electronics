# Reference map: Bosch book → website chapters

**Reference book:** *Bosch Automotive Electrics and Automotive Electronics*, 5th ed. (Robert Bosch GmbH, 2007; Springer Vieweg reprint 2014), 530 pages. PDF page number = printed page number.

**How the book is used on the site**
- The book is the reference for **concepts and diagram structure**. Every diagram on the site is **redrawn** as original SVG/canvas in the site's own style. No scanned figures or copied text go on the site, because the book is copyrighted (Springer). Each chapter carries a one-line "Reference" note with page ranges.
- The book's content dates from 2007. Every chapter also covers **what has changed by 2026** ("Then → now").

## Chapter mapping

| Site chapter | Book pages (key figures) | What the book gives | 2026 additions on the site |
|---|---|---|---|
| 01 IC engine vehicles | 13–23 Motronic, 24–31 EDC; sensors 310–353 | ME/DI-Motronic system overview, EDC common rail, torque-based control | GPF on GDI, 350 bar GDI, 2,500 bar common rail, SCR/AdBlue, OBD on-board monitoring |
| 02 Electric vehicles | 360–365 electrical machines; **366–383 hybrid drives** (Fig. p.366 serial, p.367 parallel & split-power, p.369 micro/mild/strong classification, p.377 cooperative braking, p.381–382 energy storage) | Serial / parallel / split-power hybrids, operating strategies, recuperative braking, NiMH/supercaps | BEV architecture, 800 V, SiC inverters, PMSM + FOC, LFP/NMC, P0–P4 positions, 48 V mild hybrid, brake-by-wire blending, CCS/ISO 15118 |
| 03 Electronic control units | 152–161 architecture; 162–167 mechatronics; 168–195 semiconductors; **196–207 control units** | ECU operating conditions, design, digital modules, ECU software | AUTOSAR Classic/Adaptive, lockstep MCUs (AURIX TC3xx/TC4x), HSM, zonal + central compute |
| **04 Sensors & actuators (new)** | 208–231 sensor basics (p.213 sensor in control loop, p.217 integration levels / output signals); 232–309 measuring principles; **310–353 sensor types** (p.316–319 wheel-speed passive/active, p.320–323 yaw rate, p.336–338 hot-film air-mass meter, p.348–353 two-step and LSU4 wide-band lambda); 354–359 actuators | Sensor classification, integration levels, inductive/Hall/MR speed sensing, MEMS, lambda sensors, actuator types | SENT/PSI5 sensor interfaces, TMR sensors, 6-axis IMUs, 4D imaging radar (8Tx8Rx MMICs in production), lidar, 8 MP cameras, driver monitoring, smart power switches, brake/steer-by-wire |
| **05 Vehicle electrical system (new)** | **384–399** energy supply, charge balance, EEM (p.388 EEM structure), two-battery systems, harness, connectors; 400–433 starter battery; **434–461 alternators** (p.452 current/power characteristic: n0 ≈ 1,000 rpm, rated at 6,000 rpm); **462–485 starting systems** (p.463–467 starter + engagement relay); **521–523 DIN 72552 terminal designations** | 12 V board net, battery, alternator, voltage regulation, starter, energy management, terminals 15/30/31/50 | AGM/EFB, intelligent battery sensor, LFP 12 V, DC-DC replacing alternator, 48 V low-voltage networks, zonal power distribution with eFuses, redundant power for automated driving |
| 06 Networks & diagnostics | **70–151**: topology 70, OSI 76, CAN 92–105, LIN 106–111, MOST 112–121, Bluetooth 122–131, FlexRay 132–143, diagnosis interfaces 144–151 | Bus fundamentals, CAN arbitration, LIN schedule, FlexRay TDMA, K-line/OBD | CAN FD, CAN XL, 10BASE-T1S multidrop Ethernet, 100/1000BASE-T1 backbone, TSN, SOME/IP, DoIP, SerDes for cameras, MOST → Ethernet |
| 07 Development process | 162–167 mechatronic development methods (light coverage) | Simulation-based mechatronic development | V-model, ASPICE 4.0, ISO 26262, XiL |
| 08 Cybersecurity | Not in the book | — | ISO/SAE 21434, UN R155/R156, SecOC, 0x27/0x29, HSM |
| 09 Engineering calculators | 452 alternator curve, 418–422 battery characteristics, 366–383 hybrid | Numbers for sizing | EV pack, range, charging |

## Not yet used (candidates for later modules)
- 32–45 Lighting technology (now: matrix LED, digital light)
- 46–53 ESP, 54–61 ACC, 62–69 occupant protection (good candidates for a "Chassis & safety systems" chapter with an ESP control-loop sim)
- 486–499 EMC (now: CISPR 25, ISO 11452)
- 500–520 circuit symbols and circuit diagrams
