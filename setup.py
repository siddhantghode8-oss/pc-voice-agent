"""Setup script for PC Voice Agent"""
import os
import sys
import shutil
from pathlib import Path


def setup():
    """Setup the PC Voice Agent"""
    print("🤖 PC Voice Agent - Setup")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        return False
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Check .env file
    if not Path('.env').exists():
        if Path('.env.example').exists():
            shutil.copy('.env.example', '.env')
            print("✅ Created .env from template")
        else:
            print("❌ .env.example not found")
            return False
    
    # Read API key from user
    api_key = input("\n📝 Enter your OpenAI API key (or press Enter to skip): ").strip()
    if api_key:
        with open('.env', 'r') as f:
            content = f.read()
        content = content.replace('sk_your_api_key_here', api_key)
        with open('.env', 'w') as f:
            f.write(content)
        print("✅ API key configured")
    else:
        print("⚠️  Skipped API key setup - update .env manually")
    
    print("\n📦 Installation Instructions:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Run the agent: python main.py")
    print("\n✅ Setup complete! Ready to use PC Voice Agent")
    return True


if __name__ == "__main__":
    setup()
