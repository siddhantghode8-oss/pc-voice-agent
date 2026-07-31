"""Demo mode - Test the agent without a microphone"""
import os
import sys
import logging
from dotenv import load_dotenv
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


class PCVoiceAgentDemo:
    """Demo AI agent - test without microphone"""
    
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")
        
        self.ai_engine = AIEngine(self.api_key)
        self.pc_controller = PCController()
        self.memory = MemoryManager()
        
        logger.info(f"Demo mode initialized - {os.getenv('AGENT_NAME', 'PC Agent')}")
    
    def process_command(self, command_text: str):
        """Process a command from text input"""
        try:
            logger.info(f"Processing: {command_text}")
            self.memory.add_user_message(command_text)
            
            # Get AI decision with context
            ai_response = self.ai_engine.process_command(
                command_text, 
                conversation_history=self.memory.get_history()
            )
            
            logger.info(f"AI Decision: {ai_response}")
            self.memory.add_assistant_message(str(ai_response))
            
            # Execute the command
            if ai_response.get('action') and ai_response['action'] != 'none':
                result = self.pc_controller.execute_action(ai_response)
                logger.info(f"Execution Result: {result}")
                self.memory.add_system_message(f"Action executed: {result}")
                print(f"\n[ACTION EXECUTED] {ai_response.get('action')}: {result}")
            else:
                print(f"\n[INFO] {ai_response.get('response_text', 'No action needed')}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error processing command: {e}")
            return False
    
    def run_demo(self):
        """Run interactive demo mode"""
        print("\n" + "="*60)
        print("PC VOICE AGENT - DEMO MODE")
        print("="*60)
        print("\nTesting without microphone...")
        print("Type commands to test the AI agent")
        print("Type 'exit' or 'quit' to stop\n")
        
        try:
            while True:
                user_input = input("You: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'q']:
                    print("\nExiting demo mode...")
                    break
                
                if not user_input:
                    continue
                
                print("\nAgent processing...")
                self.process_command(user_input)
                print("-" * 60)
                
        except KeyboardInterrupt:
            print("\n\nDemo stopped")


if __name__ == "__main__":
    try:
        agent = PCVoiceAgentDemo()
        agent.run_demo()
    except Exception as e:
        logger.error(f"Failed to start demo: {e}")
        sys.exit(1)
