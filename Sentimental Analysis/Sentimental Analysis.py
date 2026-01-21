import speech_recognition as sr
from textblob import TextBlob

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Please speak...")
    try:
        audio = r.listen(source, timeout=5)
        
        # Convert speech to text
        text = r.recognize_google(audio)
        print("You said:", text)

        # Sentiment Analysis
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            sentiment = "Positive 😊"
        elif polarity < 0:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

        print("Sentiment:", sentiment)
        print("Polarity Score:", polarity)

    except sr.WaitTimeoutError:
        print("You did not speak. Please try again.")

    except sr.UnknownValueError:
        print("I heard something, but could not understand. Please speak clearly.")

    except sr.RequestError:
        print("Could not request results from Google Speech Recognition.")