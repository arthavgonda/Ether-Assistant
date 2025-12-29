<div align="center">

# 🎤 EitherAssistant

**Voice control for your computer. Works offline. Built for everyone.**

[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue)](https://github.com)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![.NET](https://img.shields.io/badge/.NET-8.0-purple)](https://dotnet.microsoft.com)

</div>

---

<div align="center">

**Control your entire computer with just your voice—no internet required.**

EitherAssistant brings hands-free computing to users with disabilities, low connectivity, or anyone who prefers voice commands.

• [🚀 Quick Start](#-quick-start) • [💬 Voice Commands](#-voice-commands) • [📊 Architecture](#-how-it-works) • [🔮 Roadmap](#-planned-improvements-for-round-2)

</div>

---

## 🎥 See It In Action

<div align="center">

### Complete Setup & Demo Video

<video width="800" controls>
  <source src="Videos/setup.mp4" type="video/mp4">
  Your browser does not support the video tag. [Download the video](Videos/setup.mp4) to watch it.
</video>

</div>

---

## Why EitherAssistant?

<div align="center">

### The Problem
> Most voice assistants need constant internet, work only with specific apps, and aren't designed for people with disabilities.

### The Solution
> EitherAssistant works offline, controls any application, and is built specifically for accessibility and digital inclusion.

</div>

<table>
<tr>
<td width="50%">

#### Conventional Assistants
- Requires constant cloud connection
- Limited to specific apps
- General convenience focus
- Privacy concerns

</td>
<td width="55%">

#### EitherAssistant
- Works completely offline
- Controls any app or website
- Built for accessibility
- Privacy-first design

</td>
</tr>
</table>

---

## What It Does

<table>
<tr>
<td width="33%" align="center">

### 🎤 Voice Control
**Speak naturally, control everything**
- Natural language commands
- Real-time transcription
- Multi-step operations

</td>
<td width="33%" align="center">

### 🌐 Browser Automation
**Search, navigate, download—all by voice**
- Web search & navigation
- Form filling & clicking
- File downloads

</td>
<td width="33%" align="center">

### 💻 System Control
**Files, apps, settings—hands-free**
- File management
- App launching
- System configuration

</td>
</tr>
<tr>
<td width="33%" align="center">

### 📱 App Management
**Launch, switch, control any application**
- Context switching
- App control
- Multi-app workflows

</td>
<td width="33%" align="center">

### 🔇 Offline Mode
**Works without internet using local AI**
- Vosk offline STT
- No cloud dependency
- Privacy guaranteed

</td>
<td width="33%" align="center">

### ♿ Accessible
**Designed for users with disabilities**
- Motor impairment support
- Visual impairment support
- Screen reader compatible

</td>
</tr>
</table>

---

## How It Works


### System Flow

![Voice Command Flow](Diagrams/FlowChart.png)

### System Architecture

**Level 0 - System Overview**

![System DFD](Diagrams/Level_0DFD.png)

**Level 1 - Detailed Data Flow**

![Detailed DFD](Diagrams/Level_1DFD.png)

---

## 🚀 Quick Start

<details>
<summary><b>📦 Option 1: Pre-built Binaries (Recommended)</b></summary>

### ⚡ Fastest Way to Get Started

👉 **[View Detailed Installation Guide](INSTALLATION.md#-option-1-pre-built-binaries-recommended)**

1. **Download** from `FinalApp/` directory
2. **Run** the executable
3. **Start speaking!**

> ✅ No installation required • ✅ Works immediately • ✅ All dependencies included

</details>

<details>
<summary><b>🔧 Option 2: Build from Source</b></summary>

👉 **[View Detailed Build Instructions](INSTALLATION.md#-option-2-build-from-source)**

### Quick Commands

**Frontend:**
```bash
cd EitherAssistant
dotnet restore && dotnet build
dotnet run
```

**Backend:**
```bash
cd Python
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 api_server.py
```

</details>

---

## 💬 Voice Commands

<table>
<tr>
<td>

### 📱 Applications
```bash
"Open VS Code"
"Switch to Firefox"
"Open VS Code and create file test.py"
```

</td>
<td>

### 🌐 Web
```bash
"Search for Python tutorials"
"Open youtube.com"
"Download Discord"
```

</td>
</tr>
<tr>
<td>

### 📁 Files
```bash
"Create file notes.txt"
"List files in Documents"
"Move file to Downloads"
```

</td>
<td>

### ⚙️ System
```bash
"System info"
"Install git"
"Volume up"
```

</td>
</tr>
</table>

> 💡 **Tip:** Speak naturally! EitherAssistant understands conversational commands.

---

## 🛠️ System Requirements

<table>
<tr>
<td align="center">

### Operating System
- Windows 10+
- macOS 10.15+
- Linux (Ubuntu 20.04+)

</td>
<td align="center">

### Hardware
- 4GB RAM (8GB recommended)
- Microphone (required)
- Internet (optional)

</td>
<td align="center">

### Software
- Python 3.8+
- .NET 8.0 SDK
- Browser (Chrome/Firefox)

</td>
</tr>
</table>

---

## Tech Stack

<table>
<tr>
<td align="center" width="20%">

![Avalonia](https://img.shields.io/badge/AVALONIA-UI-blue?style=for-the-badge&logo=avalonia)
**Frontend**  
C# .NET 8.0

</td>
<td align="center" width="20%">

![FastAPI](https://img.shields.io/badge/FASTAPI-009688?style=for-the-badge&logo=fastapi)
**Backend**  
Python 3.8+

</td>
<td align="center" width="20%">

![Whisper](https://img.shields.io/badge/WHISPER-STT-brightgreen?style=for-the-badge)
**Speech Recognition**  
Whisper + Vosk

</td>
<td align="center" width="20%">

![Selenium](https://img.shields.io/badge/SELENIUM-AUTOMATION-orange?style=for-the-badge&logo=selenium)
**Automation**  
Browser Control

</td>
<td align="center" width="20%">

![AI](https://img.shields.io/badge/AI-GEMINI-purple?style=for-the-badge)
**Command Parsing**
Gemini Api

</td>
</tr>
</table>

---

## 🌍 Accessibility Features

<div align="center">

| 🦽 Motor Disabilities | 👁️ Visual Impairments | 📡 Low Connectivity | 💰 Cost-Free | 🔄 Cross-Platform |
|:---------------------:|:---------------------:|:-------------------:|:------------:|:----------------:|
| ✅ Complete hands-free control | ✅ Screen reader compatible | ✅ Full offline functionality | ✅ Open source | ✅ Works on any device |
| No keyboard/mouse needed | Voice feedback | No internet required | No subscriptions | Windows, macOS, Linux |

</div>

---

## Planned Improvements for Round 2

<table>
<tr>
<td width="50%">

### 1. Context Memory
- Remember previous commands
- Follow-up commands: "open it again"
- Conversation history

**Status:** 🟡 In Planning

</td>
<td width="50%">

### 2. Multilingual Support
- Hindi STT models
- Regional languages
- Auto language detection

**Status:** 🟡 In Planning

</td>
</tr>
<tr>
<td width="50%">

### 3. Custom Commands
- Personal shortcuts
- "Start work mode" workflows
- Command templates

**Status:** 🟡 In Planning

</td>
<td width="50%">

### 4. Enhanced Accessibility
- Better screen reader support
- Voice confirmations
- Accessibility mode toggle

**Status:** 🟡 In Planning

</td>
</tr>
<tr>
<td colspan="2" align="center">

### 5. Lightweight Edge Mode

<div align="left" style="display: inline-block;">

- Lower CPU usage
- Optimized offline mode
- Performance profiles

</div>

**Status:** 🟡 In Planning

</td>
</tr>
</table>

---

## Troubleshooting

<details>
<summary><b>Audio not detected?</b></summary>

- Check microphone permissions in system settings
- Adjust sensitivity in application settings
- Test microphone: `python -m sounddevice`

</details>

<details>
<summary><b>Browser not working?</b></summary>

- Ensure Chrome, Firefox, or Brave is installed
- Check browser can run normally
- Linux: `sudo apt install chromium-browser firefox`

</details>

<details>
<summary><b>Port 8000 in use?</b></summary>

- Stop other services using port 8000
- Change port in config: `export API_PORT=8001`
- Kill process: `lsof -ti:8000 | xargs kill -9`

</details>

<details>
<summary><b>Need more help?</b></summary>

- API Documentation: `http://localhost:8000/docs`
- Create an issue on GitHub
- Check troubleshooting section above

</details>

---

## Acknowledgments

<div align="center">

### Built with open-source technologies

<table>
<tr>
<td align="center">

**Avalonia UI**  
Cross-platform framework

</td>
<td align="center">

**FastAPI**  
Modern Python web framework

</td>
<td align="center">

**Whisper**  
OpenAI speech recognition

</td>
<td align="center">

**Vosk**  
Offline speech recognition

</td>
<td align="center">

**Selenium**  
Browser automation

</td>
</tr>
</table>

---

## Documentation

<div align="center">

### Complete Project Documentation

[![PDF Documentation](https://img.shields.io/badge/_View_Full_Documentation-FF0000?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)](Project%20Documentation%20-%20EitherAssistant.pdf)

**[Download PDF →](Project%20Documentation%20-%20EitherAssistant.pdf)**

*Comprehensive technical documentation covering architecture, implementation, and design decisions*

</div>

---

<div align="center">

[⬆ Back to Top](#-eitherassistant)

Made with ❤️ for accessibility and digital inclusion

</div>

</div>
