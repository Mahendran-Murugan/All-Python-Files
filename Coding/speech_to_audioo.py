import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Wait for callibration")
    recognizer.adjust_for_ambient_noise(source, duration=3)
    print("Start Speaking")
    audio = recognizer.listen(source)
    print("Recording Sucessful")
    speech = recognizer.recognize_google(audio)
    speech = speech.lower()
    print(speech)

import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate",170)
engine.say(speech)
engine.runAndWait()