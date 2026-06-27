# PCB Design — 20251GTY35

Custom PCB for motor driver connections and power distribution on the Personal AI Robot.

---

## Overview

The custom PCB (76×68×2 mm) houses the TB6612FNG motor driver and manages connections between:
- Raspberry Pi 5 GPIO pins
- LiPo battery power rail
- TT motors (left/right)
- Buck converter output

---

## PCB Schematics

### Schematic View
<img width="362" height="193" alt="Screenshot 2025-10-27 at 11 16 57 PM" src="https://github.com/user-attachments/assets/cb042998-2179-4cec-9109-23d90681215f" />

Motor driver connections with all signal lines and power rails labeled.

---

## PCB Layouts

### 3D view
<img width="535" height="406" alt="Screenshot 2025-10-27 at 11 12 57 PM" src="https://github.com/user-attachments/assets/22dcbcb2-acb4-4bf5-90a2-1513b5ef60b3" />

Component placement showing connectors and motor driver positioning.

---

### 2D view
<img width="500" height="445" alt="20251GTY35_Om" src="https://github.com/user-attachments/assets/ff1226bb-1d69-4216-9b21-763e48568d99" />

Copper traces routing power and signals between motor driver, battery, and Raspberry Pi headers.

---

## Key Features

- **Motor Driver Breakout:** TB6612FNG with all control pins accessible
- **Power Rails:** Dedicated VM (motor voltage) and VCC (logic voltage) planes
- **Pin Headers:**
  - Raspberry Pi GPIO header (5V, GND, PWM pins)
  - Motor connectors (M1, M2)
  - Battery input (VM, GND)
  - Buck converter input/output

---

## Manufacturing Notes

- **Dimensions:** 76 × 68 × 2 mm
- **Material:** FR-4 (1.6 mm thickness)
- **Layers:** 2-layer PCB
- **Trace Width:** 20 mil (motor power), 10 mil (signals)
- **Via Size:** 8 mil (0.2 mm)

Mount with M2 standoffs at corners (2 mount holes).

---

## Assembly Instructions

1. Solder TB6612FNG IC to PCB
2. Add 100 nF decoupling capacitors near IC pins
3. Solder pin headers for Raspberry Pi connection
4. Connect motor and battery terminals
5. Verify continuity between power rails before powering up

