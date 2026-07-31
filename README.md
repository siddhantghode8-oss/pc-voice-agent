# PC Voice Agent - Quick Start Guide

## Setup Instructions

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key
- Get your OpenAI API key from: https://platform.openai.com/api-keys
- Copy `.env.example` to `.env`
- Edit `.env` and add your API key:
```
OPENAI_API_KEY=sk_your_actual_key_here
```

### 3. Run the Agent
```bash
python main.py
```

## Features

✅ **Voice Commands** - Speak naturally to control your PC  
✅ **AI Understanding** - Uses OpenAI GPT to understand intent  
✅ **Smart Actions** - Launches apps, manages files, controls system  
✅ **Context Awareness** - Remembers conversation history  
✅ **Safety Mode** - Prevents accidental dangerous actions  

## Example Voice Commands

- "Open Notepad"
- "Create a new folder on Desktop called Projects"
- "Take a screenshot"
- "Type hello world"
- "Launch Chrome"
- "Open my documents folder"
- "Delete the file at C:\\temp\\test.txt" (requests confirmation)

## Architecture

```
main.py              → Entry point, orchestrates all components
├── voice_capture.py → Speech-to-text (Google Speech Recognition)
├── ai_engine.py     → OpenAI GPT integration for decision making
├── pc_controller.py → System action execution
├── memory_manager.py → Conversation history & context
└── .env             → Configuration (API keys)
```

## How It Works

1. **Listen** - Microphone captures your voice
2. **Transcribe** - Converts speech to text
3. **Understand** - AI analyzes intent and decides action
4. **Execute** - System performs the action
5. **Remember** - Conversation stored for context

## Advanced Features

### Conversation Memory
- Maintains last 20 messages
- Saves history to `conversation_history.json`
- Provides context for multi-step commands

### Safety Mode
- Dangerous actions require confirmation
- File deletions are prevented in safety mode
- System shutdown/restart are blocked

### Extensible Design
- Easy to add new action types
- Pluggable voice recognition
- Multiple AI backends supported

## Troubleshooting

**"No microphone detected"**
- Check system audio settings
- Run: `python -c "import pyaudio; print(pyaudio.PyAudio().get_device_count())"`

**"API key not found"**
- Ensure `.env` file exists in same directory as `main.py`
- Check OPENAI_API_KEY is set correctly

**"Speech not recognized"**
- Speak clearly and slowly
- Ensure good audio quality
- Check microphone isn't muted

**Dangerous actions not executing**
- Safety mode is ON by default
- Edit `pc_controller.py` and set `self.safety_mode = False` to disable

## Future Enhancements

- [ ] Local speech recognition (no Google API calls)
- [ ] Custom voice commands file
- [ ] Multi-language support
- [ ] GUI dashboard
- [ ] Command recording & playback
- [ ] Integration with IFTTT/Automation
- [ ] Scheduled tasks support
- [ ] Smart home control (Philips Hue, etc.)

## License

MIT

## Support

For issues or features, check the code comments or contact the developer.
