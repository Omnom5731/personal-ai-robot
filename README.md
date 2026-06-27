
# Personal AI Robot — 20251GTY35

A low-cost, open-source, Wall-E-style personal AI robot built on Raspberry Pi 5. It listens for a wake word, processes voice commands using Google Gemini AI, and responds with synthesized speech.
<img width="465" height="510" alt="Screenshot 2026-06-27 at 1 29 04 PM" src="https://github.com/user-attachments/assets/b3923246-430d-48e3-a101-908b97fda6f3" />
**Team GR-30 | MEP1001 Project**

| Name |
|------|
| Om Gaidhani |
| Tanvi Aggarwal |
| Nandani Porwal |
| Ankita Sahu |
| Prakash Lal |

---

## 📌 Features

- 🎙️ Wake-word detection ("Robot") via USB microphone
- 🧠 AI conversation powered by Google Gemini 2.0 Flash
- 🔊 Text-to-speech voice output via gTTS + USB speakers
- 👀 Animated OLED eyes (blink, emotions, look left/right)
- 📷 Face recognition via Pi Camera Module
- 🚗 Motorized movement (left/right TT motors via TB6612FNG)
- 💬 Conversation memory (last 5 exchanges)
- 📝 Conversation logging to file
- 🔌 Wi-Fi + Bluetooth via Raspberry Pi 5

---

## 🏗️ Project Structure

```
personal-ai-robot/
├── software/
│   ├── main.py           # Entry point — wake word loop + speech pipeline
│   ├── voice_input.py    # Wake word detection + speech recognition
│   ├── voice_output.py   # Text-to-speech output
│   ├── ai_response.py    # Gemini AI integration + conversation memory
│   └── logger.py         # Conversation logging
├── hardware/
│   ├── BOM.md            # Bill of Materials with costs
│   └── PCB_DESIGN.md     # PCB schematics and layouts
├── docs/
│   └── wiring.md         # Electrical connection notes
└── README.md
```

---

## 🔧 Hardware

### Component List (BOM)

| Part | Purpose | Cost (₹ INR) |
|------|---------|--------------|
| Raspberry Pi 5 4GB | Main computer | 6250 |
| MicroSD 64GB Class 10 | Pi storage | 400 |
| 4× Wheels (65mm) | Locomotion | 720 |
| 2× TT Motors | Locomotion | 200 |
| TB6612FNG Motor Driver | Drive left/right motors | 160 |
| Jumper Wires (MM/MF/FF) | Testing | 40 |
| USB Microphone | Voice input | 1500 |
| 2× USB Speakers | Voice output | 220 |
| 0.96″ OLED Display | Animated eyes | 340 |
| Pi Camera Module | Face recognition | 2000 |
| Custom PCB | Motor driver connections | — |
| LiPo Battery | Power for Pi + motors | 400 |
| Buck Converter | Voltage regulation | 40 |
| Standoffs, Screws, Acrylic | Mechanical parts | — |
| Hookup Wire + Switch | Connections | 310 |
| **Total** | | **~₹12,580** |

### Dimensions

| Measurement | Value |
|------------|-------|
| Footprint (base) | 220 × 240 mm |
| Overall height | ~260 mm |
| Wheelbase | 140–160 mm |
| Track width | 160–180 mm |
| Eye spacing | 100 mm (center-to-center) |

### Technical Specs

| Category | Specification |
|----------|--------------|
| Core Processing | Raspberry Pi 5 |
| Microphone | USB omnidirectional |
| Speakers | USB (2×1.5W) |
| Camera | Pi Camera Module |
| Display (Eyes) | OLED 0.96″ |
| Motor Driver | TB6612FNG |
| Mobility | 2× TT Gear Motors (200–300 RPM, 6–12V) + 65mm wheels |
| Connectivity | Wi-Fi + Bluetooth (via Pi 5) |
| Body | FDM 3D-printed, Wall-E style |

---

## ⚡ Electrical Design

The Raspberry Pi 5 handles all tasks centrally:

- Drives TT motors via TB6612FNG (GPIO PWM pins)
- Handles OLED eye animations via `luma.oled`
- Powers speakers and microphone via USB
- Runs speech recognition, TTS, and AI processing in Python

**Power:** LiPo battery → Buck converter (5V regulation) → Raspberry Pi 5 + Motor VM rail

See `/docs/wiring.md` for the full connection diagram.

---

## 🎛️ PCB Design

Custom PCB (76×68×2 mm) for motor driver integration and power distribution.

### Overview

The PCB features:
- **TB6612FNG Motor Driver IC** with all GPIO control lines
- **Power Rails:** Separate VM (motor) and VCC (logic) planes
- **Connectors:** Raspberry Pi GPIO header, motor terminals, battery input
- **2-Layer PCB** with optimized trace routing for motor power

### Schematics & Layouts

The PCB includes detailed schematics showing the motor driver connections, power distribution, and GPIO pin mappings. See `/hardware/PCB_DESIGN.md` for full schematics, board layouts, and assembly instructions.

---

## 💻 Software Setup

### Prerequisites

- Raspberry Pi 5 running Raspberry Pi OS (64-bit)
- Python 3.10+
- USB microphone at `plughw:2,0`
- USB speakers at `plughw:3,0`

### Installation

```bash
git clone https://github.com/Omnom5731/personal-ai-robot.git
cd personal-ai-robot
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file at `/home/pi/robot/.env`:

```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

Get your API key from [Google AI Studio](https://aistudio.google.com/).

### Running the Robot

```bash
cd software
python main.py
```

The robot will print `System initialized. Waiting for wake word...` and begin listening.

---

## 🗣️ How It Works

1. **Wake word** — The robot continuously records 5-second audio chunks and listens for the word **"Robot"**
2. **Command capture** — On detection, it records a 6-second command
3. **AI processing** — The command is sent to Gemini 2.0 Flash with the last 5 exchanges as context
4. **Voice response** — The reply is cleaned, converted to speech via gTTS, and played through speakers
5. **Logging** — Every exchange is appended to `conversation_log.txt`

---

## 📦 Dependencies

```
SpeechRecognition
google-generativeai
gtts
pydub
python-dotenv
luma.oled
pygame
pyaudio
```

Install all with:
```bash
pip install SpeechRecognition google-generativeai gtts pydub python-dotenv luma.oled pygame pyaudio
```

Also install system audio tools:
```bash
sudo apt install alsa-utils ffmpeg
```

---

## 🆚 Why Build This vs. Buying Commercial

| | Commercial Robots | This Robot |
|--|--|--|
| Cost | ₹30,000–₹1,70,000 | ~₹12,000 |
| Customization | Closed hardware/software | Fully open-source & modifiable |
| Repair | Sealed, becomes e-waste | 3D-printed body, replaceable battery |
| AI | Fixed/proprietary | Swap in any LLM (Gemini, OpenAI, etc.) |
| Design | Factory Plastic | Fun Wall-E style |


## 📄 License

free to use, modify, and build upon.
