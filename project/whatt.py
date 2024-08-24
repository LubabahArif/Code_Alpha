import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("understanding...")
        query = r.recognize_google(audio,language="en-in")
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendmessage():
    speak("Who do you want to message")
    a = int(input('''person 1 - 1
              person 2 - 2'''))
    if a == 1:
        speak("whats the message")
        message = str(input("Enter the message-"))
        pywhatkit.sendwhatmsg("+9200000000000",message,time_hour=strTime,time_min=update)
        web = f"https://web.whatsapp.com/"
        webbrowser.open(web)
    elif a == 1:
        speak("whats the message")
        message = str(input("Enter the message-"))
        pywhatkit.sendwhatmsg("+9299999999999",message,time_hour=strTime,time_min=update)

    
