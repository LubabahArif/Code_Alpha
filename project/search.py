import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchgoogle(query):
    if "google" in query:
        query = query.replace("google search","").replace("google","")
        speak("this is what i found in google")
        pywhatkit.search(query)
        try:
            result = wikipedia.summary(query, sentence=1)
            speak(result)
        except:
            speak("no speakable output available")

def searchYoutube(query):
    if "youtube"  in query:
        query = query.replace("youtube search", "").replace("youtube","")
        speak("this is what I foud for your search!")      
        web = f"https://www.youtube.com/results?search_query= {query}"
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("done, sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        query = query.replace("search wikipedia", "").replace("wikipedia","")
        speak("searching wikipedia...")
        results = wikipedia.summary(query,sentences = 2)
        speak("according to wikipedia...")
        speak(results)
        print(results)