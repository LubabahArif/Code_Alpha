import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui
from greet import greetMe
from search import searchgoogle,searchYoutube,searchWikipedia
import os
from plyer import notification


for i in range(3):
    a = input("enter passward to open jarvis:-")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        print("welcome sir! plz speak[wake up] to load me up")
        break
    elif (i == 2 and a!=pw):
        exit()
    elif (a!=pw):
        print("try again")

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

if __name__ =="__main__":
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue
        if "wake up" in query:
              greetMe()

              while True:
                  query = takeCommand().lower()
                  if query == "none":
                      continue
                  if "go to sleep" in query:
                      speak("Ok sir, You can call me anytime")
                      break
                  
                 ################## ##j jarvis the trilogy 2.0#################

                  elif "change password" in query:
                      speak("whats the new password")
                      new_pw = input("enter the new password\n")
                      new_password = open("password.txt","w")
                      new_password.write(new_pw)
                      new_password.close()
                      speak("done,sir")
                      speak(f"your new password is{new_pw}")

                  elif "schedule my day" in query:
                      tasks = []#empty list
                      speak("do you want to clear old tasks(plz speak yes or no)")
                      query = takeCommand().lower()
                      if "yes" in query:
                          file = open("tasks.txt","w")
                          file.write(f"")
                          file.close()
                          no_task = int(input("enter the number of tasks:-"))
                          i = 0
                          for i in range(no_task):
                              tasks.append(input("enter the tasks :-"))
                              file = open("tasks.txt","a")
                              file.write(f"{i}.{tasks[i]}\n")
                              file.close()
                      elif "no" in query:
                           i = 0
                           no_task = int(input("enter the number of tasks:-"))
                           for i in range(no_task):
                              tasks.append(input("enter the tasks :-"))
                              file = open("tasks.txt","a")
                              file.write(f"{i}.{tasks[i]}\n")
                              file.close()
                    
                  elif "show my schedule" in query:
                      file = open("tasks.txt","r")
                      content = file.read()
                      file.close()
                       
                      notification.notify(
                          title = "my schedule:-",
                          message = content,
                          timeout = 15
                      )

                  elif "open" in query:
                      query = query.replace("open","")
                      query = query.replace("jervis","")
                      pyautogui.press("super")
                      pyautogui.typewrite(query)
                      pyautogui.sleep(2)
                      pyautogui.press("enter")

                      
                          
                  ############################################################
                  elif "hello" in query:
                      speak("hello sir , how are you?")
                  elif " i am fine" in query:
                      speak("that's great sir")
                  elif "how are you" in query:
                      speak("perfect sir")
                  elif "thank you" in query:
                      speak("you are welcome, sir")

                  elif "pause" in query:
                      pyautogui.press("k")
                      speak("video paused")
                  elif "play" in query:
                      pyautogui.press("k")
                      speak("video played")
                  elif "mute" in query:
                      pyautogui.press("m")
                      speak("video muted")

                  elif "volume up" in query:
                      from board import volumeup
                      speak("turning volume up,sir")
                      volumeup()
                  elif "volume dowm" in query:
                      from board import volumedown
                      speak("turning volume down,sir")
                      volumedown()
                  
                  elif "google" in query:
                      searchgoogle(query)
                  elif "youtube" in query:
                      searchYoutube(query)
                  elif "wikipedia" in query:
                      searchWikipedia(query)

                  elif "whatsapp" in query:
                      from whatt import sendmessage
                      sendmessage()

                  elif "temperature" in query or "weather" in query:
                      search = "temperature in karachi"
                      url= f"https://www.google.com/search?q={search}"
                      r = requests.get(url)
                      data = BeautifulSoup(r.text,"html.parser")
                      temp = data.find("div", class_="BNeawe" ).text
                      speak(f"current{search} is {temp}")

                  elif "the time" in query:
                      strTime = datetime.datetime.now().strftime("%H:%M")
                      speak(f"sir, the time is {strTime}")

                  elif "finally sleep" in query:
                      speak("going to sleep")
                      exit()

                  elif "remember that" in query:
                      remembermessage = query.replace("remembar that","")
                      remembermessage = query.replace("jarvis","")
                      speak("tou told me" +remembermessage)
                      remember =open("remember.txt","a")
                      remember.write(remembermessage)
                      remember.close()
                  elif "what do you remember" in query:
                      remember = open("remember.txt","r")
                      speak("you told me" + remember.read())

                  elif "shutdown system" in query:
                      speak("are you shure you want to shutdown")
                      shutdown = input("do you wish to shutdown your laptop?(yes/no)")
                      if shutdown ==  "yes":
                          os.system("shutdown /s /t 1")

                      break