# Electrical Wiring Guide

## Overview

The Raspberry Pi 5 is the central controller for all subsystems.
<img width="1200" height="947" alt="Untitled design" src="https://github.com/user-attachments/assets/0610a6e8-64a0-4861-9612-4731745a02c2" />

## Raspberry Pi GPIO Assignments

| GPIO Pin | Connected To | Function |
|----------|-------------|---------|
| 18 | TB6612FNG PWMA | Motor A speed |
| 23 | TB6612FNG AIN1 | Motor A direction |
| 24 | TB6612FNG AIN2 | Motor A direction |
| 19 | TB6612FNG PWMB | Motor B speed |
| 26 | TB6612FNG BIN1 | Motor B direction |
| 21 | TB6612FNG BIN2 | Motor B direction |
| 2 (SDA) | OLED SDA | I2C eye display |
| 3 (SCL) | OLED SCL | I2C eye display |
| USB | Microphone | Voice input |
| USB | Speakers | Audio output |
| CSI | Pi Camera | Face recognition |

## TB6612FNG Motor Driver Connections

```
LiPo Battery (+) ──→ VM (motor voltage)
Buck Converter 5V ─→ VCC (logic voltage)
GND ───────────────→ GND

Motor A ← AO1, AO2
Motor B ← BO1, BO2
```

## Power System

```
LiPo Battery
    │
    ├──→ Buck Converter (5V output) ──→ Raspberry Pi 5 (USB-C power)
    │
    └──→ TB6612FNG VM pin (motor voltage, 6–12V)
```

## Audio

- **Microphone**: USB connection to Raspberry Pi, device index `plughw:2,0`
- **Speakers**: USB connection to Raspberry Pi, device index `plughw:3,0`
- Update indices in `voice_input.py` and `voice_output.py` if your system differs (run `arecord -l` and `aplay -l` to list devices)

## OLED Eye Display

- Protocol: I2C
- SDA → GPIO 2 (Pin 3)
- SCL → GPIO 3 (Pin 5)
- VCC → 3.3V
- GND → GND

## Notes

- Always power off before making wiring changes
- The buck converter should be set to **5.1V** before connecting to the Pi
- Verify mic/speaker ALSA device IDs with `arecord -l` / `aplay -l` before first run
