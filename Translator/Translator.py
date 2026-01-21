import speech_recognition as sr
from deep_translator import GoogleTranslator

# Initialize recognizer and translator
r = sr.Recognizer()
translator = GoogleTranslator(source='en', target='es')  # English to Spanish

# Use microphone as source
with sr.Microphone() as source:
    print("Please speak in English...")
    r.adjust_for_ambient_noise(source, duration=1)

    try:
        audio = r.listen(source, timeout=5, phrase_time_limit=10)

        # Speech to text (English - India accent supported)
        english_text = r.recognize_google(audio, language="en-IN")
        print("English Text:", english_text)

        # Translate English to Spanish
        spanish_text = translator.translate(english_text)
        print("Spanish Translation:", spanish_text)

    except sr.WaitTimeoutError:
        print("You did not speak. Please try again.")

    except sr.UnknownValueError:
        print("Could not understand the speech.")

    except sr.RequestError as e:
        print("Speech recognition service error:", e)
