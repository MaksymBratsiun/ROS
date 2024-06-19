import os
import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv()

WIT_KEY = str(os.environ.get('WIT_KEY'))

recognizer = sr.Recognizer()
with sr.Microphone() as source:
  print("Speak something...")
  audio_data = recognizer.listen(source)
try:
   text = recognizer.recognize_wit(audio_data, key=WIT_KEY)
   print("You said:", text)
except sr.UnknownValueError as e:
   print("Sorry, could not understand audio.")
   print(e)
except sr.RequestError as e:
   print("Error: Could not request results")
   print(e)
