"""
PC VOICE AGENT - QUICK START GUIDE
===================================

This guide shows you how to run your PC Voice Agent
"""

# ============================================================================
# STEP 1: VERIFY INSTALLATION
# ============================================================================
print("""
STEP 1: Verify Installation
============================
Run this command to check if everything is installed correctly:

    python verify_install.py

Expected output:
    - All 6 packages should show [OK]
    - API key status message
""")

# ============================================================================
# STEP 2: SETUP OPENAI API KEY
# ============================================================================
print("""
STEP 2: Setup OpenAI API Key (IMPORTANT!)
==========================================

1. Go to: https://platform.openai.com/api-keys
2. Log in or create an account
3. Click "Create new secret key"
4. Copy the key (it starts with "sk-...")
5. Edit the .env file in your project folder:
   - Find the line: OPENAI_API_KEY=sk_your_api_key_here
   - Replace it with: OPENAI_API_KEY=sk_xxxxxxxxxxxxx

⚠️  IMPORTANT: Add billing to your OpenAI account!
   - Visit: https://platform.openai.com/account/billing/overview
   - Add a payment method
   - Check your usage and limits

Once you have:
  ✓ Valid API key
  ✓ Billing enabled
  ✓ Credits or payment method
  
Then you can run the agent!
""")

# ============================================================================
# STEP 3: RUN THE AGENT
# ============================================================================
print("""
STEP 3: Run the PC Voice Agent
==============================

There are 3 ways to run:

1. DEMO MODE (Recommended for testing):
   ====================================
   python demo.py
   
   - No microphone needed
   - Type commands directly
   - Test the AI engine
   - Example commands:
     * "Open Notepad"
     * "Create a folder on Desktop"
     * "Take a screenshot"
     * "Launch Chrome"
   
   Type 'exit' or 'quit' to stop

2. INTERACTIVE MODE (With microphone):
   =====================================
   python main.py
   
   - Listens to your microphone
   - Converts speech to text
   - Executes AI commands
   - Press Enter for next command
   
3. DEMO WITH SAFETY MODE:
   =======================
   The system has safety mode ON by default
   - Dangerous actions require confirmation
   - File deletions are simulated
   - Shutdown/restart are blocked
   
   To disable, edit pc_controller.py:
   Change: self.safety_mode = True
   To:     self.safety_mode = False
""")

# ============================================================================
# STEP 4: EXAMPLE COMMANDS
# ============================================================================
print("""
STEP 4: Try These Commands
==========================

Text Commands (in demo.py):
  - "Open Notepad"
  - "Launch Chrome"
  - "Take a screenshot"
  - "Create folder called test"
  - "Open documents folder"
  - "Type hello world"
  - "Press Ctrl+C"
  - "Click at position 100 200"

Voice Commands (in main.py):
  - Just speak naturally
  - The AI will understand
  - Microphone listens continuously

Each command is processed through OpenAI GPT
and executed on your PC!
""")

# ============================================================================
# STEP 5: TROUBLESHOOTING
# ============================================================================
print("""
STEP 5: Troubleshooting
=======================

Issue: "OPENAI_API_KEY not found"
Fix:   - Check .env file exists in same folder as main.py
       - Verify API key is set correctly
       - No spaces around the equals sign

Issue: "Exceeded your current quota"
Fix:   - Add payment method to OpenAI account
       - Check https://platform.openai.com/account/billing/overview
       - Wait a few minutes if just added payment

Issue: "The model gpt-4 does not exist"
Fix:   - This is fixed! We use gpt-3.5-turbo now
       - Run: python test_quick.py

Issue: "Could not find PyAudio"
Fix:   - Not needed! We fixed this
       - Microphone will still work with speech_recognition

Issue: Microphone not detected
Fix:   - Check system audio settings
       - Run: python demo.py (text mode, no mic needed)
       - Test mic in Windows Settings

Issue: Speech not recognized
Fix:   - Speak clearly and slowly
       - Ensure good audio quality
       - Check microphone isn't muted
       - Internet connection required (uses Google Speech-to-Text)
""")

# ============================================================================
# STEP 6: PROJECT FILES
# ============================================================================
print("""
STEP 6: Project Files
=====================

main.py              - Start voice agent (with microphone)
demo.py              - Test agent (text input, no mic)
verify_install.py    - Check installation
test_quick.py        - Test AI engine

voice_capture.py     - Microphone handling
ai_engine.py         - OpenAI GPT integration
pc_controller.py     - Execute system actions
memory_manager.py    - Conversation history

.env                 - Configuration (your API key)
.env.example         - Template
README.md            - Full documentation
requirements.txt     - Dependencies
""")

# ============================================================================
# QUICK START
# ============================================================================
print("""
QUICK START SUMMARY
===================

1. Open terminal in: c:\\Users\\Admiin\\New folder\\pc_voice_agent

2. Check your .env file has your API key

3. Choose and run:
   - python demo.py       (easiest, no mic needed)
   - python main.py       (with microphone)

4. Give commands and watch it work!

That's it! 🚀
""")
