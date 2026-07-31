"""Voice input handler using Speech Recognition"""
import speech_recognition as sr
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class VoiceCapture:
    """Handles audio input and transcription"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        
        # Try to get microphone, but don't fail if unavailable
        try:
            self.microphone = sr.Microphone()
            logger.info("Microphone initialized successfully")
        except Exception as e:
            logger.warning(f"Microphone not available: {e}")
            self.microphone = None
        
        # Adjust recognizer settings for better accuracy
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.energy_threshold = 4000
    
    def listen_for_command(self, timeout: int = 10) -> Optional[str]:
        """
        Listen to microphone and convert speech to text
        
        Args:
            timeout: Maximum seconds to listen
            
        Returns:
            Transcribed text or None if failed
        """
        try:
            if self.microphone is None:
                logger.error("Microphone not available")
                return None
                
            with self.microphone as source:
                logger.info("Recording audio...")
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=10)
            
            logger.info("Converting speech to text...")
            # Use Google Speech Recognition (free tier)
            text = self.recognizer.recognize_google(audio)
            logger.info(f"Transcribed: {text}")
            return text.lower()
            
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            return None
        except sr.RequestError as e:
            logger.error(f"Speech recognition service error: {e}")
            return None
        except sr.WaitTimeoutError:
            logger.warning("No speech detected within timeout")
            return None
        except Exception as e:
            logger.error(f"Voice capture error: {e}")
            return None
    
    def speak_feedback(self, text: str):
        """
        Optional: Text-to-speech feedback
        Could be implemented with pyttsx3 or gTTS
        """
        try:
            # Placeholder for TTS implementation
            logger.info(f"[AGENT WOULD SAY]: {text}")
        except Exception as e:
            logger.error(f"TTS error: {e}")
