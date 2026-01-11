<div align="center">

# 🎤 EitherAssistant

**Offline-first, cross-platform voice automation framework for OS-level desktop control**

A modular system enabling real-time speech recognition, intent-driven command execution, and deterministic automation across desktop operating systems — with no mandatory cloud dependency.

[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue)](https://github.com)
[![Backend](https://img.shields.io/badge/Backend-Python%203.8%2B-blue)](https://python.org)
[![Frontend](https://img.shields.io/badge/Frontend-.NET%208.0%20%7C%20Avalonia-purple)](https://dotnet.microsoft.com)
[![Architecture](https://img.shields.io/badge/Architecture-Offline--First%20%7C%20Modular-green)](#)

</div>

---

<div align="center">

**Enable OS-level desktop control through real-time voice-driven automation — fully functional offline.**

EitherAssistant provides an offline-first, accessibility-focused voice interface for deterministic control of applications, browsers, and system resources, designed for users with motor impairments, low-connectivity environments, and hands-free interaction workflows.

• [🚀 Deployment Guide](#-quick-start) • [💬 Command Grammar](#-voice-commands) • [📊 System Architecture](#-how-it-works) • [🔮 Feature Roadmap](#-planned-improvements-for-round-2)

</div>

---

## See It In Action...

<div align="center">

### Complete Setup & Demo Video



https://github.com/user-attachments/assets/73fca6bc-e572-49d3-8705-ef38e2a9dea6



</div>

---

## Why EitherAssistant?

<div align="center">

### The Problem
> Most existing voice assistants are architected as cloud-dependent, application-restricted systems, resulting in high latency, limited control scope, reduced reliability in low-connectivity environments, and insufficient support for accessibility-focused use cases.

### The Solution
> EitherAssistant introduces an offline-first, OS-level voice automation architecture that enables deterministic control over applications and system resources, with accessibility and privacy as first-class design constraints.

</div>

<table>
<tr>
<td width="50%">

#### Conventional Voice Assistants
- Cloud-centric STT and NLP pipelines  
- Mandatory continuous internet connectivity  
- Restricted to vendor-supported applications  
- Variable latency due to network round-trips  
- Audio and commands processed off-device  
- Designed primarily for general convenience  

</td>
<td width="55%">

#### EitherAssistant
- Offline-first local speech inference  
- Fully functional without network access  
- OS- and browser-level control of any application  
- Predictable low-latency local execution  
- On-device audio and command processing  
- Accessibility-driven and privacy-first design  

</td>
</tr>
</table>

---

## What It Does

<table>
<tr>
<td width="33%" align="center">

### 🎤 Voice Control  
**Low-latency speech-to-action pipeline**

- Continuous microphone sampling at 16 kHz with real-time processing  
- Streaming speech-to-text inference with average transcription latency < 300 ms  
- Natural language command parsing and intent classification  
- Supports compound and multi-step command execution  
- Deterministic mapping of voice intents to system-level actions  

</td>
<td width="33%" align="center">

### 🌐 Browser Automation  
**Voice-driven browser control and interaction**

- Browser automation across Chrome, Firefox, Brave, Edge, and Chromium  
- Voice-initiated web search, URL navigation, and page traversal  
- Programmatic DOM interaction (click, type, submit)  
- Automated file downloads with execution feedback  
- No reliance on website-specific APIs or extensions  

</td>
<td width="33%" align="center">

### 💻 System Control  
**Operating system–level command execution**

- Voice-based file system operations (create, move, delete, list)  
- Application lifecycle management (launch, focus, terminate)  
- System configuration controls (volume, brightness, settings access)  
- OS-specific command routing with safety validation  
- Unified abstraction for Windows, macOS, and Linux  

</td>
</tr>
<tr>
<td width="33%" align="center">

### 📱 App Management  
**Context-aware multi-application workflows**

- Voice-driven application switching and focus control  
- Maintains execution context across sequential commands  
- Supports multi-application task flows (e.g., open → edit → save)  
- Application-agnostic control without internal API dependencies  
- State-aware command routing to the active application  

</td>
<td width="33%" align="center">

### 🔇 Offline Mode  
**Offline-first execution and inference**

- Fully local speech recognition using Vosk models (~50–180 MB)  
- Zero network dependency for core system functionality  
- Predictable performance and latency in offline environments  
- On-device audio processing ensuring data privacy  
- Optional online inference fallback for higher transcription accuracy  

</td>
<td width="33%" align="center">

### ♿ Accessibility  
**Assistive computing–optimized design**

- Enables 100% hands-free system interaction  
- Eliminates dependency on keyboard and pointing devices  
- Compatible with platform-native screen readers  
- Reduces cognitive and physical input load  
- Designed for users with motor  impairments  

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

### ⚡ Precompiled Distribution

Use the pre-built executables for immediate deployment without manual setup.

👉 **[Detailed Installation Guide](INSTALLATION.md#-option-1-pre-built-binaries-recommended)**

1. Download the appropriate binary from the `FinalApp/` directory  
2. Execute the platform-specific binary  
3. Grant microphone permissions and begin issuing voice commands  

> Includes frontend, backend, runtime dependencies, and default configuration

</details>

<details>
<summary><b>🔧 Option 2: Build from Source</b></summary>

### 🧱 Source-Based Build

Compile and run the system manually for development, customization, or contribution.

👉 **[Detailed Build Instructions](INSTALLATION.md#-option-2-build-from-source)**

- Requires .NET 8.0 SDK and Python 3.8+  
- Enables full access to source code and configuration  
- Recommended for developers and contributors  


</details>

### Quick Commands
Use the given Commands to compile and run Either Assistant Locally 
**Frontend:**
```bash
cd EitherAssistant
dotnet restore && dotnet build
dotnet run
```

**Backend:**
```bash
cd Python
python3 -m venv venv # Building the Virtual Environment 
source venv/bin/activate  # Windows: venv\Scripts\activate 
pip install -r requirements.txt
python3 api_server.py
```

</details>

---

### 💬 Voice Commands

<table>
<tr>
<td>

### 📱 Applications
```bash
"Open VS Code"
"Switch to Firefox"
"Open VS Code and create file test.py"
```
-Application launch and context switching

-Supports compound commands (2–3 actions per utterance)
</td>
<td>

### 🌐 Web
```bash
"Search for Python tutorials"
"Open youtube.com"
"Download Discord"
```
-Voice-driven browser navigation and search

-Works across Chrome, Firefox, Brave, and Edge

-Automated downloads with execution feedback
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
-File system operations via OS-level automation

-Supports relative and absolute paths

-Safe execution with validation before destructive actions
</td>
<td>

### ⚙️ System
```bash
"System info"
"Install git"
"Volume up"
```
-System information and utility commands

-Package installation via native package managers

-Real-time control of system settings (volume, brightness)
</td>
</tr>
</table>

> 💡 **Tip:** Speak naturally! EitherAssistant understands conversational commands It's build just for you .

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
**Frontend Layer**  
C# • .NET 8.0  
Cross-platform desktop UI using MVVM architecture and native accessibility APIs

</td>
<td align="center" width="20%">

![FastAPI](https://img.shields.io/badge/FASTAPI-009688?style=for-the-badge&logo=fastapi)
**Backend Services**  
Python 3.8+  
ASGI-based REST and WebSocket server for low-latency command processing

</td>
<td align="center" width="20%">

![Whisper](https://img.shields.io/badge/WHISPER-STT-brightgreen?style=for-the-badge)
**Speech Recognition**  
Whisper + Vosk  
Hybrid STT pipeline with offline-first inference and optional high-accuracy mode

</td>
<td align="center" width="20%">

![Selenium](https://img.shields.io/badge/SELENIUM-AUTOMATION-orange?style=for-the-badge&logo=selenium)
**Automation Layer**  
Selenium WebDriver  
Browser and DOM-level automation independent of website-specific APIs

</td>
<td align="center" width="20%">

![AI](https://img.shields.io/badge/AI-GEMINI-purple?style=for-the-badge)
**Command Interpretation**  
Gemini API (Optional)  
Natural language intent extraction with offline rule-based fallback

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



**[Download PDF →](https://drive.google.com/file/d/1qbPEpS_Y8iXaXrO0hxCbSktXBzcpGdYI/view?usp=share_link)**

*Comprehensive technical documentation covering architecture, implementation, and design decisions*

</div>

---

<div align="center">

[⬆ Back to Top](#-eitherassistant)

Made with ❤️ for accessibility and digital inclusion

</div>

</div>
