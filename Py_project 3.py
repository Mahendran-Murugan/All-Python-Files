import pyttsx3
import speech_recognition as sr
import pandas as pd

dataset = pd.read_csv('/Users/mahendran/Documents/Data sets for ML/diabetes.csv')


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=3)
        speak("Listening..")
        print("Listening..")
        audio = recognizer.listen(source)
    try:
        speak("Recognizing...")
        print("Recognizing...")
        query1 = recognizer.recognize_google(audio, language="en-in")
        if query1[0:6] == "glands":
            query1 = "glance" + query1[6:]
        print(f'User said:{query1.lower()}')
    except:
        speak("Say that again...")
        print("Say that again...")
        return "None"
    return query1


def tell_col_name():
    col_name = list(dataset.columns)
    print(col_name)
    for i in col_name:
        speak(i)


def chk_null_val():
    chk_null = dataset.isnull().sum()
    print(chk_null)
    if chk_null.sum() == 0:
        print("No null values")
        speak("No null values")
    else:
        null = f"There {chk_null} null values."
        print(null)
        speak(null)


def shape_of_ds():
    shape = tuple(dataset.shape)
    print(shape)
    sh_of_ds = f"There are {shape[0]} rows and {shape[1]} columns"
    print(sh_of_ds)
    speak(sh_of_ds)


def glance_of_ds():
    print(dataset.head())


speak("I'm Your virtual assistant Jarvis, How can i help you sir")
while True:
    query2 = take_command().lower()
    if "tell me the column names" in query2:
        print("Processing...")
        speak("Processing...")
        tell_col_name()
    elif "check for null values" in query2:
        print("Processing...")
        speak("Processing...")
        chk_null_val()
    elif "shape of the data set" in query2:
        print("Processing...")
        speak("Processing...")
        shape_of_ds()
    elif "glance about the data set" in query2:
        print("Processing...")
        speak("Processing...")
        glance_of_ds()
    elif "sleep jarvis" in query2:
        print("Exiting...")
        speak("Thank you")
        break
    else:
        print("Try again...")
        speak("Try again sir.")
        
