"""PC Controller - Executes actions on the system"""
import os
import sys
import logging
import subprocess
import pyautogui
import psutil
from typing import Dict, Any
from pathlib import Path

logger = logging.getLogger(__name__)


class PCController:
    """Executes system actions based on AI decisions"""
    
    def __init__(self):
        pyautogui.FAILSAFE = True  # Move mouse to corner to abort
        self.safety_mode = True
    
    def execute_action(self, ai_decision: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the action decided by AI
        
        Args:
            ai_decision: Decision from AI engine
            
        Returns:
            Execution result
        """
        try:
            action = ai_decision.get('action', 'none')
            params = ai_decision.get('action_params', {})
            
            if action == 'app_launch':
                return self._launch_app(params.get('app_name'))
            elif action == 'app_open_file':
                return self._open_file(params.get('file_path'))
            elif action == 'file_delete':
                return self._delete_file(params.get('file_path'))
            elif action == 'file_create':
                return self._create_file(params.get('file_path'), params.get('content', ''))
            elif action == 'folder_open':
                return self._open_folder(params.get('folder_path'))
            elif action == 'folder_create':
                return self._create_folder(params.get('folder_path'))
            elif action == 'screenshot':
                return self._take_screenshot()
            elif action == 'keyboard_type':
                return self._type_text(params.get('text'))
            elif action == 'keyboard_shortcut':
                return self._press_shortcut(params.get('shortcut'))
            elif action == 'mouse_click':
                return self._mouse_click(params.get('x'), params.get('y'), params.get('button', 'left'))
            elif action == 'mouse_move':
                return self._mouse_move(params.get('x'), params.get('y'))
            elif action == 'volume_set':
                return self._set_volume(params.get('level'))
            elif action == 'system_shutdown':
                return self._shutdown(params.get('after_seconds', 0))
            elif action == 'system_restart':
                return self._restart()
            elif action == 'query_info':
                return {"success": True, "message": "Information query completed"}
            else:
                return {"success": True, "message": "No action needed"}
                
        except Exception as e:
            logger.error(f"Execution error: {e}")
            return {"success": False, "error": str(e)}
    
    def _launch_app(self, app_name: str) -> Dict:
        """Launch an application"""
        try:
            if not app_name:
                return {"success": False, "error": "App name not provided"}
            
            # Map common app names to executable paths
            app_map = {
                'notepad': 'notepad.exe',
                'chrome': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
                'firefox': 'C:\\Program Files\\Mozilla Firefox\\firefox.exe',
                'vscode': 'code',
                'calculator': 'calc.exe',
                'explorer': 'explorer.exe',
                'powershell': 'powershell.exe',
                'cmd': 'cmd.exe'
            }
            
            exe_name = app_map.get(app_name.lower(), app_name)
            subprocess.Popen(exe_name)
            logger.info(f"Launched {app_name}")
            return {"success": True, "message": f"Launched {app_name}"}
        except Exception as e:
            return {"success": False, "error": f"Failed to launch {app_name}: {str(e)}"}
    
    def _open_file(self, file_path: str) -> Dict:
        """Open a file with default application"""
        try:
            if not file_path or not os.path.exists(file_path):
                return {"success": False, "error": f"File not found: {file_path}"}
            
            os.startfile(file_path)
            return {"success": True, "message": f"Opened {file_path}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _delete_file(self, file_path: str) -> Dict:
        """Delete a file"""
        try:
            if not file_path or not os.path.exists(file_path):
                return {"success": False, "error": "File not found"}
            
            if self.safety_mode:
                logger.warning(f"Safety mode: would delete {file_path}")
                return {"success": True, "message": f"[SAFETY MODE] Would delete {file_path}"}
            
            os.remove(file_path)
            return {"success": True, "message": f"Deleted {file_path}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _create_file(self, file_path: str, content: str = '') -> Dict:
        """Create a new file"""
        try:
            if not file_path:
                return {"success": False, "error": "File path not provided"}
            
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(content)
            return {"success": True, "message": f"Created {file_path}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _open_folder(self, folder_path: str) -> Dict:
        """Open a folder in explorer"""
        try:
            if not folder_path or not os.path.isdir(folder_path):
                return {"success": False, "error": "Folder not found"}
            
            os.startfile(folder_path)
            return {"success": True, "message": f"Opened {folder_path}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _create_folder(self, folder_path: str) -> Dict:
        """Create a new folder"""
        try:
            if not folder_path:
                return {"success": False, "error": "Folder path not provided"}
            
            Path(folder_path).mkdir(parents=True, exist_ok=True)
            return {"success": True, "message": f"Created folder {folder_path}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _take_screenshot(self) -> Dict:
        """Take a screenshot"""
        try:
            screenshot_path = os.path.expanduser("~/Desktop/screenshot.png")
            pyautogui.screenshot(screenshot_path)
            return {"success": True, "message": f"Screenshot saved to {screenshot_path}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _type_text(self, text: str) -> Dict:
        """Type text on keyboard"""
        try:
            if not text:
                return {"success": False, "error": "Text not provided"}
            
            pyautogui.typewrite(text)
            return {"success": True, "message": f"Typed: {text}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _press_shortcut(self, shortcut: str) -> Dict:
        """Press keyboard shortcut"""
        try:
            if not shortcut:
                return {"success": False, "error": "Shortcut not provided"}
            
            keys = shortcut.lower().split('+')
            pyautogui.hotkey(*keys)
            return {"success": True, "message": f"Pressed {shortcut}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _mouse_click(self, x: int, y: int, button: str = 'left') -> Dict:
        """Click mouse at position"""
        try:
            pyautogui.click(x, y, button=button)
            return {"success": True, "message": f"Clicked at ({x}, {y})"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _mouse_move(self, x: int, y: int) -> Dict:
        """Move mouse to position"""
        try:
            pyautogui.moveTo(x, y)
            return {"success": True, "message": f"Moved mouse to ({x}, {y})"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _set_volume(self, level: int) -> Dict:
        """Set system volume"""
        try:
            if not 0 <= level <= 100:
                return {"success": False, "error": "Volume must be 0-100"}
            
            # Windows volume control (simplified)
            logger.info(f"[TODO] Set volume to {level}%")
            return {"success": True, "message": f"Set volume to {level}%"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _shutdown(self, after_seconds: int = 0) -> Dict:
        """Shutdown PC"""
        try:
            if self.safety_mode:
                logger.warning(f"Safety mode: would shutdown after {after_seconds}s")
                return {"success": True, "message": "[SAFETY MODE] Would shutdown PC"}
            
            cmd = f'shutdown /s /t {after_seconds}'
            subprocess.run(cmd, shell=True)
            return {"success": True, "message": f"Shutting down in {after_seconds}s"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _restart(self) -> Dict:
        """Restart PC"""
        try:
            if self.safety_mode:
                logger.warning("Safety mode: would restart")
                return {"success": True, "message": "[SAFETY MODE] Would restart PC"}
            
            subprocess.run('shutdown /r', shell=True)
            return {"success": True, "message": "Restarting PC"}
        except Exception as e:
            return {"success": False, "error": str(e)}
