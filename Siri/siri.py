import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from deep_translator import GoogleTranslator

# Text to speech
engine = pyttsx3.init()
engine.setProperty("rate", 160)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Speech recognizer
recognizer = sr.Recognizer()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="en-IN")
        print("You said:", command)
        return command.lower().strip()
    except:
        return ""

def process_command(command):
    if command == "":
        speak("I did not hear anything")
        return False   # ❌ not successful

    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
        return True    # ✅ success

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")
        return True

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        return True

    elif "translate" in command:
        speak("What should I translate?")
        text = take_command()
        translator = GoogleTranslator(source='en', target='es')
        translated = translator.translate(text)
        speak(translated)
        return True

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        return True

    else:
        speak("Sorry, I did not understand the command")
        return False

# MAIN (Stops after success)
speak("Voice assistant started")
while True:
    command = take_command()
    success = process_command(command)
    if success:
        break

