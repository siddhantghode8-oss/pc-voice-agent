"""AI Engine - OpenAI GPT integration for command understanding"""
import logging
import json
from typing import Dict, List, Optional
from openai import OpenAI

logger = logging.getLogger(__name__)


class AIEngine:
    """Processes voice commands using OpenAI GPT"""
    
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-3.5-turbo"  # Fast and reliable model
        
        self.system_prompt = """You are a PC control assistant. Your job is to understand user voice commands 
and convert them into executable actions on their computer.

Available actions:
- 'app_launch': Launch an application (provide app_name)
- 'app_open_file': Open a file with default app (provide file_path)
- 'file_delete': Delete a file (provide file_path, confirm_dangerous=true for important files)
- 'file_create': Create a new file (provide file_path, content)
- 'folder_open': Open a folder in explorer (provide folder_path)
- 'folder_create': Create new folder (provide folder_path)
- 'screenshot': Take a screenshot
- 'keyboard_type': Type text on keyboard (provide text)
- 'keyboard_shortcut': Press keyboard shortcut (provide shortcut like 'ctrl+c')
- 'mouse_move': Move mouse to coordinates (provide x, y)
- 'mouse_click': Click mouse (provide button: 'left'/'right', x, y)
- 'system_shutdown': Shutdown PC (provide after_seconds for delay)
- 'system_restart': Restart PC
- 'volume_set': Set volume level (provide level 0-100)
- 'query_info': Just provide information (no action needed)
- 'none': No action needed

IMPORTANT RULES:
1. Always respond with valid JSON
2. For dangerous actions (delete, shutdown), ask for confirmation first by setting needs_confirmation=true
3. Include reasoning for your decision
4. Consider context from conversation history
5. If command is ambiguous, ask clarification via 'needs_clarification=true'

Example response format:
{
    "action": "app_launch",
    "action_params": {"app_name": "notepad"},
    "reasoning": "User wants to open text editor",
    "confidence": 0.95,
    "needs_confirmation": false,
    "needs_clarification": false,
    "response_text": "Launching Notepad for you"
}
"""
    
    def process_command(
        self, 
        command: str, 
        conversation_history: Optional[List[Dict]] = None
    ) -> Dict:
        """
        Process a voice command through GPT
        
        Args:
            command: User's voice command
            conversation_history: Previous conversation turns
            
        Returns:
            Decision dict with action and parameters
        """
        try:
            messages = [
                {"role": "system", "content": self.system_prompt}
            ]
            
            # Add conversation history for context
            if conversation_history:
                messages.extend(conversation_history[-6:])  # Last 6 messages for context
            
            # Add current command
            messages.append({"role": "user", "content": command})
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.3,  # Low temperature for consistent decisions
                max_tokens=500
            )
            
            response_text = response.choices[0].message.content
            logger.info(f"GPT Response: {response_text}")
            
            # Parse JSON response
            decision = json.loads(response_text)
            
            # Validate response structure
            if 'action' not in decision:
                decision['action'] = 'none'
            
            return decision
            
        except json.JSONDecodeError:
            logger.error("Failed to parse GPT response as JSON")
            return {
                "action": "none",
                "reasoning": "Failed to parse AI response",
                "confidence": 0,
                "response_text": "I couldn't understand that properly"
            }
        except Exception as e:
            logger.error(f"AI engine error: {e}")
            return {
                "action": "none",
                "reasoning": f"Error: {str(e)}",
                "confidence": 0,
                "response_text": "I encountered an error processing that"
            }
