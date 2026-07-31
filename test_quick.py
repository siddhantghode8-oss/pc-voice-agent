"""Quick test script"""
import sys
sys.path.insert(0, '.')

from ai_engine import AIEngine
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("ERROR: OPENAI_API_KEY not found in .env")
    sys.exit(1)

print("Initializing AI Engine...")
ai = AIEngine(api_key)

print("\nTesting command: 'Open Notepad'")
result = ai.process_command("Open Notepad")
print("\nAI Response:")
import json
print(json.dumps(result, indent=2))
