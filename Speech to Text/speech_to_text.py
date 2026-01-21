import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("please speak..")
    try:
        audio=r.listen(source,timeout=5)
        print(r.recognize_google(audio))
    except sr.WaitTimeoutError:
        print("you did not speak.please speak.")
    except sr.UnknownValueError:
        print("i heard something, but could not understand.please speak clearly.")