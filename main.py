"""Voice-Controlled PC Agent - Main Entry Point"""
import os
import sys
import logging
from dotenv import load_dotenv
from voice_capture import VoiceCapture
from ai_engine import AIEngine
from pc_controller import PCController
from memory_manager import MemoryManager

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'INFO'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PCVoiceAgent:
    """Main AI agent that controls PC via voice commands"""
    
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")
        
        self.voice = VoiceCapture()
        self.ai_engine = AIEngine(self.api_key)
        self.pc_controller = PCController()
        self.memory = MemoryManager()
        
        logger.info(f"Initialized {os.getenv('AGENT_NAME', 'PC Agent')}")
    
    def run_once(self):
        """Run a single voice command cycle"""
        try:
            logger.info("Listening for voice input...")
            command_text = self.voice.listen_for_command()
            
            if not command_text:
                logger.warning("No speech detected")
                return False
            
            logger.info(f"Heard: {command_text}")
            self.memory.add_user_message(command_text)
            
            # Get AI decision with context
            ai_response = self.ai_engine.process_command(
                command_text, 
                conversation_history=self.memory.get_history()
            )
            
            logger.info(f"AI Decision: {ai_response}")
            self.memory.add_assistant_message(ai_response)
            
            # Execute the command
            if ai_response.get('action') and ai_response['action'] != 'none':
                result = self.pc_controller.execute_action(ai_response)
                logger.info(f"Execution Result: {result}")
                self.memory.add_system_message(f"Action executed: {result}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error in command cycle: {e}")
            return False
    
    def run_interactive(self):
        """Run in interactive mode - listen for hotkey"""
        logger.info(f"PC Voice Agent started. Press {os.getenv('LISTEN_HOTKEY', 'CTRL+ALT+V')} to command...")
        
        try:
            while True:
                self.run_once()
                input("Press Enter for next command (or Ctrl+C to exit)...")
        except KeyboardInterrupt:
            logger.info("Agent stopped by user")
    
    def run_continuous(self):
        """Continuous listening mode"""
        logger.info("Continuous mode started...")
        try:
            while True:
                self.run_once()
        except KeyboardInterrupt:
            logger.info("Agent stopped")


if __name__ == "__main__":
    try:
        agent = PCVoiceAgent()
        agent.run_interactive()
    except Exception as e:
        logger.error(f"Failed to start agent: {e}")
        sys.exit(1)
