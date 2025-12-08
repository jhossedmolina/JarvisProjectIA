#!/usr/bin/env python3
"""
JARVIS - Just A Rather Very Intelligent System
A simple voice assistant in Python
"""

import sys
import datetime
import webbrowser
import platform
from urllib.parse import quote

try:
    import pyttsx3
    import speech_recognition as sr
except ImportError:
    print("Error: Required libraries not installed.")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)


class Jarvis:
    def __init__(self):
        """Initialize the Jarvis voice assistant"""
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        
        # Configure voice properties
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 150)
        
    def speak(self, text):
        """Convert text to speech"""
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
        
    def listen(self):
        """Listen to user input via microphone"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio, language='es-ES')
                print(f"You: {text}")
                return text.lower()
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                self.speak("Lo siento, hay un problema con el servicio de reconocimiento de voz")
                return ""
            except Exception as e:
                print(f"Error: {e}")
                return ""
    
    def get_time(self):
        """Get current time"""
        now = datetime.datetime.now()
        return now.strftime("%H:%M")
    
    def get_date(self):
        """Get current date"""
        now = datetime.datetime.now()
        months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                  'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
        return f"{now.day} de {months[now.month-1]} de {now.year}"
    
    def search_web(self, query):
        """Search on the web"""
        encoded_query = quote(query)
        url = f"https://www.google.com/search?q={encoded_query}"
        webbrowser.open(url)
        self.speak(f"Aquí está lo que encontré sobre {query}")
    
    def process_command(self, command):
        """Process user commands"""
        if not command:
            return True
            
        # Greetings
        if any(word in command for word in ['hola', 'buenos días', 'buenas tardes', 'buenas noches']):
            self.speak("Hola! Soy Jarvis. ¿En qué puedo ayudarte?")
            
        # Time
        elif 'hora' in command:
            time = self.get_time()
            self.speak(f"Son las {time}")
            
        # Date
        elif 'fecha' in command or 'día' in command:
            date = self.get_date()
            self.speak(f"Hoy es {date}")
            
        # Search
        elif 'busca' in command or 'buscar' in command:
            self.speak("¿Qué quieres que busque?")
            query = self.listen()
            if query:
                self.search_web(query)
                
        # Open YouTube
        elif 'youtube' in command:
            webbrowser.open("https://www.youtube.com")
            self.speak("Abriendo YouTube")
            
        # Open Google
        elif 'google' in command:
            webbrowser.open("https://www.google.com")
            self.speak("Abriendo Google")
            
        # System info
        elif 'sistema' in command:
            self.speak(f"Estoy ejecutándome en {platform.system()} {platform.release()}")
            
        # Exit
        elif any(word in command for word in ['salir', 'adiós', 'cerrar', 'terminar']):
            self.speak("Hasta luego! Que tengas un buen día")
            return False
            
        # Help
        elif 'ayuda' in command:
            self.speak("Puedo ayudarte con: la hora, la fecha, buscar en internet, "
                      "abrir YouTube, abrir Google, o información del sistema. "
                      "Di 'salir' para terminar.")
        
        else:
            self.speak("No entendí el comando. Di 'ayuda' para ver lo que puedo hacer")
            
        return True
    
    def run(self):
        """Main loop for the assistant"""
        self.speak("Hola! Soy Jarvis, tu asistente virtual. ¿En qué puedo ayudarte?")
        self.speak("Di 'ayuda' para ver los comandos disponibles")
        
        running = True
        while running:
            try:
                command = self.listen()
                running = self.process_command(command)
            except KeyboardInterrupt:
                self.speak("Hasta luego!")
                break
            except Exception as e:
                print(f"Error: {e}")
                continue


def main():
    """Main entry point"""
    print("=" * 50)
    print("JARVIS - Just A Rather Very Intelligent System")
    print("=" * 50)
    
    # Check if running in text mode
    if '--text' in sys.argv or '-t' in sys.argv:
        print("Modo texto no implementado aún")
        print("Por favor ejecuta sin el parámetro --text")
        return
    
    try:
        jarvis = Jarvis()
        jarvis.run()
    except Exception as e:
        print(f"Error al iniciar Jarvis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
