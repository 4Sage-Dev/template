# Voice Interactive Setup Guide

> This document helps an LLM walk a user through setting up speech-to-text
> (STT) and text-to-speech (TTS) for a voice-interactive 4SAGE session.

---

## Overview

The voice-interactive tier lets the user have a verbal conversation with
their AI game design consultant. This requires:

1. **Speech-to-Text (STT)** — converts the user's voice to text input
2. **Text-to-Speech (TTS)** — converts the AI's text responses to spoken audio
3. **An AI coding tool** that supports hooks or extensions (e.g., Claude Code)

## Before Starting

Ask the user:
- What operating system are you on? (Windows, macOS, Linux)
- What AI tool are you using? (Claude Code, Cursor, etc.)
- Do you have a microphone? (built-in laptop mic is fine)
- Do you have speakers or headphones?

---

## Platform-Specific Setup

### Windows

#### STT Options
| Option | Pros | Cons | Install |
|--------|------|------|---------|
| **Windows Speech Recognition** | Built-in, no install | Lower accuracy | Settings → Speech |
| **Whisper (OpenAI)** | High accuracy, offline | Requires Python + GPU recommended | `pip install openai-whisper` |
| **faster-whisper** | Fast, accurate, lower VRAM | Requires Python | `pip install faster-whisper` |
| **Google Chrome Speech API** | Good accuracy, easy | Requires Chrome, internet | Built into Chrome |

#### TTS Options
| Option | Pros | Cons | Install |
|--------|------|------|---------|
| **Windows SAPI** | Built-in | Robotic voice | Built-in |
| **Piper TTS** | Fast, good quality, offline | Setup required | Download from GitHub |
| **Kokoro TTS** | Best quality, small model | Requires Python + GPU | `pip install kokoro` |
| **Edge TTS** | Good quality, easy | Requires internet | `pip install edge-tts` |

#### Recommended Windows Setup (Easiest)
1. Install Python from python.org if not already installed
2. `pip install edge-tts` for TTS (good quality, minimal setup)
3. For STT, use faster-whisper if you have a GPU, or Windows built-in if not

### macOS

#### STT Options
| Option | Pros | Cons | Install |
|--------|------|------|---------|
| **macOS Dictation** | Built-in, good accuracy | May send audio to Apple | System Preferences → Keyboard → Dictation |
| **Whisper / faster-whisper** | High accuracy, offline, private | Requires Python | `pip install faster-whisper` |

#### TTS Options
| Option | Pros | Cons | Install |
|--------|------|------|---------|
| **macOS `say` command** | Built-in, decent quality | Limited voices | Built-in |
| **Piper TTS** | Good quality, offline | Setup required | `brew install piper-tts` or download |
| **Kokoro TTS** | Best quality | Requires Python | `pip install kokoro` |
| **Edge TTS** | Good quality, easy | Requires internet | `pip install edge-tts` |

#### Recommended macOS Setup (Easiest)
1. Enable macOS Dictation (System Preferences → Keyboard → Dictation)
2. `pip install edge-tts` for TTS
3. Or use the built-in `say` command for zero-install TTS

### Linux

#### STT Options
| Option | Pros | Cons | Install |
|--------|------|------|---------|
| **faster-whisper** | Fast, accurate, best option | Requires Python + GPU recommended | `pip install faster-whisper` |
| **Whisper (OpenAI)** | High accuracy | Slower than faster-whisper | `pip install openai-whisper` |
| **Vosk** | Lightweight, offline | Lower accuracy | `pip install vosk` |

#### TTS Options
| Option | Pros | Cons | Install |
|--------|------|------|---------|
| **Piper TTS** | Fast, good quality, offline | Setup required | `pip install piper-tts` |
| **Kokoro TTS** | Best quality, small model | GPU recommended | `pip install kokoro` |
| **espeak-ng** | Everywhere, tiny | Robotic | `apt install espeak-ng` |
| **Edge TTS** | Good quality, easy | Requires internet | `pip install edge-tts` |

#### Recommended Linux Setup
1. `pip install faster-whisper` for STT
2. `pip install piper-tts` or `pip install kokoro` for TTS (depending on GPU availability)

---

## Integration with Claude Code

Claude Code supports hooks that can trigger TTS on responses and STT for
input. The setup involves:

1. **STT daemon** — a background service that listens for a hotkey
   (e.g., push-to-talk), records audio, transcribes it, and types the
   result into the terminal.

2. **TTS hook** — a Claude Code "Stop" hook that pipes the AI's response
   through TTS and plays it through speakers.

### Example Claude Code Hook Configuration

In `~/.claude/settings.json`:
```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "command": "echo \"$CLAUDE_RESPONSE\" | your-tts-command"
      }
    ]
  }
}
```

The specific command depends on the TTS tool chosen. The LLM should help
the user configure this based on their platform and chosen tools.

---

## Troubleshooting

### STT not picking up audio
- Check microphone permissions in OS settings
- Test the mic in another app first
- Try `arecord -l` (Linux) or check Sound settings (Windows/macOS)

### TTS not producing sound
- Check speaker/headphone volume
- Test with a simple command: `say "hello"` (macOS) or `espeak "hello"` (Linux)
- Check that the TTS process isn't being blocked by permissions

### High latency
- Use faster-whisper instead of original Whisper for STT
- Use Piper instead of Kokoro if GPU is unavailable for TTS
- Reduce Whisper model size (use "base" or "small" instead of "large")

### GPU memory issues
- STT and TTS can share GPU but may compete for VRAM
- If VRAM is limited (<4GB), use CPU-based options
- faster-whisper "small" model needs ~1GB VRAM
- Kokoro TTS needs ~0.5GB VRAM
