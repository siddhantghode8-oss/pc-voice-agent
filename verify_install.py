"""Quick test to verify PC Voice Agent installation"""
import sys
import os


def test_imports():
    """Test all required imports"""
    print("\n" + "="*60)
    print("PC VOICE AGENT - INSTALLATION VERIFICATION")
    print("="*60 + "\n")
    
    tests_passed = 0
    tests_failed = 0
    
    packages = [
        ('openai', 'OpenAI API'),
        ('dotenv', 'Environment Variables'),
        ('speech_recognition', 'Speech Recognition'),
        ('pyautogui', 'Auto GUI Control'),
        ('psutil', 'System Utilities'),
        ('requests', 'HTTP Requests'),
    ]
    
    for package, description in packages:
        try:
            __import__(package)
            print(f"[OK] {description:.<40} {package}")
            tests_passed += 1
        except ImportError as e:
            print(f"[FAIL] {description:.<40} {package}")
            print(f"       Error: {e}")
            tests_failed += 1
    
    print(f"\n{'='*60}")
    print(f"Results: {tests_passed} passed, {tests_failed} failed")
    print(f"{'='*60}\n")
    
    if tests_failed == 0:
        print("[SUCCESS] All dependencies installed correctly!")
        print("\nNext steps:")
        print("1. Get your OpenAI API key from: https://platform.openai.com/api-keys")
        print("2. Edit .env file and add your API key")
        print("3. Run: python main.py")
        return 0
    else:
        print("[ERROR] Some packages failed to import")
        return 1


def check_env_file():
    """Check if .env file exists"""
    print("\nEnvironment Configuration:")
    if os.path.exists('.env'):
        print("[OK] .env file found")
        with open('.env', 'r') as f:
            content = f.read()
            if 'sk_your_api_key_here' in content:
                print("[WARNING] API key not configured yet")
                print("          Edit .env and replace 'sk_your_api_key_here' with your actual key")
            else:
                print("[OK] API key appears to be configured")
    else:
        print("[WARNING] .env file not found")
        print("          Copy .env.example to .env first")


if __name__ == "__main__":
    result = test_imports()
    check_env_file()
    sys.exit(result)
