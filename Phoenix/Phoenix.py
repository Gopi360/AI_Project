#install pyaudio, pyttsx3, SpeechRecognition, setuptools, opencv-python, wikipedia, pywhatkit

import pyttsx3
import speech_recognition as sr
# import datetime
import os
import cv2
import random
import wikipedia
import webbrowser
import pywhatkit as kit
import pyautogui as agu
import time
from requests import get
from datetime import datetime, timedelta

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}")
    except Exception as e:
        speak("I didn't understand what did you say... \nSo please Say that again!!!")
        return take_command()
        # return "none"
    return query

def extract_name(user_name):
    words = user_name.lower().split()
    name = "User"

    if "name" in words and "is" in words:
        name_index = words.index("is") + 1
        if name_index < len(words):
            name = words[name_index]
    elif "i" in words and "am" in words:
        name_index = words.index("am") + 1
        if name_index < len(words):
            name = words[name_index]
    else:
        name = words[-1] if words else "User"

    return name.capitalize()

def wish(name):
    hour = int(datetime.now().hour)

    if hour >= 0 and hour <=  12:
        speak(f"Good Morning {name}!!!")
    elif hour > 12 and hour <= 18:
        speak(f"Good Afternoon {name}!!!")
    else:
        speak(f"Good Evening {name}!!!")

    speak("You must be one of the friend of my Boss.")
    speak("I'm Phoenix... tell me what can I do for you??")

def wish_boss():
    hour = int(datetime.now().hour)

    if hour >= 0 and hour <=  12:
        speak(f"Good Morning BOSS!!!")
    elif hour > 12 and hour <= 18:
        speak(f"Good Afternoon BOSS!!!")
    else:
        speak(f"Good Evening BOSS!!!")
    speak("Tell me what can I do for you today??")

def wish_sree():
    hour = int(datetime.now().hour)

    speak("Oohh!! hello Sree!")

    if hour >= 0 and hour <=  12:
        speak(f"Good Morning!!!")
    elif hour > 12 and hour <= 18:
        speak(f"Good Atfernoon!!!")
    else:
        speak(f"Good Evening!!!")

    speak("I heard about many things about you from my BOSS. He really speak alot about you!!")
    speak("Tell me what can I do for you today??")

def extract_topic_from_query(query):
    query = query.replace("according to wikipedia", "").replace("tell me about", "").replace("who is", "").replace("what is", "")
    topic = query.strip()
    print(f"Extracted topic for Wikipedia search: {topic}")
    return topic

# def wp_msg()

if __name__ == "__main__":
    speak("Hi!! \nCan you tell me your name?")

    user_name = take_command().upper()
    name = extract_name(user_name)

    if name == "Gopi" or name == "Supriyo":
        wish_boss()
    elif name == "Srijita" or name == "Sreejita":
        wish_sree()
    else:
        # speak("Do you have the permission to access my boss's laptop?")
        # yes_no = take_command().upper()
        # if yes_no == "YES":
        #     wish(name)
        # else:
        #     speak("Sorry you can't access me or the laptop without my BOSS'S permission!")
        wish(name)
        
    while True:
    # if 1:
        query = take_command().lower()
        # query = queries.split()
        
        if ("open" in query and "notepad" in query) or ("on" in query and "notepad" in query): #Open Notpad
            speak("Sure...")
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif ("open" in query and "ms ward" in query) or ("on" in query and "ms word" in query) or ("open" in query and "microsoft word" in query) or ("on" in query and "microsoft word" in query): #Open Microsoft Word
            speak("Sure...")
            os.system("start winword")

        elif("open" in query and "command" in query and "prompt" in query) or ("on" in query and "command" in query and "prompt" in query): #Open CMD
            os.system("start cmd")

        elif("open" in query and "camera" in query) or ("on" in query and "camera" in query): #Webcam On
            speak("Sure")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif("play" in query and "music" in query) or ("play" in query and "song" in query): #Playing Music
            music_dir = "E:\\AI_Project\\Phoenix\\Music"
            speak("Sure")
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        
        elif("ip" in query and "address" in query): #Checking IP Address
            speak("Sure... Give me a moment")
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")

        elif("who" in query and "is" in query) or ("what" in query and "is" in query) or ("tell" in query and "about" in query): #Searching Something from wikipedia
            speak("Searching Wikipedia...")
            topic = extract_topic_from_query(query)
            try:
                results = wikipedia.summary(topic, sentences=5)
                speak("According to Wikipedia")
                speak(results)
                # print(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"Your query is too broad. Please be more specific. Suggestions include: {e.options[:5]}")
            except wikipedia.exceptions.PageError:
                speak("I couldn't find any results for your query on Wikipedia.")

        elif("open" in query and "youtube" in query) or ("on" in query and "youtube" in query): #Open Youtube
            speak("Sure...")
            webbrowser.open("www.youtube.com")
        
        elif("open" in query and "facebook" in query) or ("on" in query and "facebook" in query): #Open Facebook
            speak("Sure...")
            webbrowser.open("www.facebook.com")
        
        elif("open" in query and "insta" in query) or ("on" in query and "insta" in query) or ("open" in query and "instagram" in query) or ("on" in query and "instagram" in query): #Open Instagram
            speak("Sure...")
            webbrowser.open("www.instagram.com")

        elif("open" in query and "whatsapp" in query): #Open whatsapp
            speak("Sure...")
            # webbrowser.open("www.whatsapp.com")
            os.system("start chrome https://web.whatsapp.com/")

        elif("open" in query and "google" in query) or ("on" in query and "google" in query): #Google Search
            speak("What should I search on google for you?")
            search = take_command().lower()
            search = search.replace(" ","+")
            search = "https://www.google.com/search?q="+search
            os.system(f"start chrome {search}")

        elif("download" in query and "movie" in query) : #Download Movie
            speak("Which type of movie you want to download?\nHollywood or Bollywood")
            movie = take_command().lower()
            if("hollywood" in movie):
                speak("Here you Go!!!")
                webbrowser.open("https://moviesmod.cash/")
            elif("bollywood" in movie):
                speak("Here you Go!!!")
                webbrowser.open("https://topmovies.beer/")
            else:
                ("I dont have the link to download this type of movie!!")
        
        elif("message" in query and "whatsapp" in query):
            speak("Who do you want to message?")
            name = take_command().lower()
            contact = {
                "Raja" : "+916291069387",
                "Sanu" : "+916289042064",
                "Gopal" : "+918582820252",
                "Arindam" : "+918479908149",
                "Adhikari" : "+916290518309",
                "Sree" : "+919064245289"
            }

            if("raja" in name):
                speak("What do I message?")
                msg = take_command().lower()

                try:
                    now = datetime.now()
                    send_time = now + timedelta(minutes=1)
                    hour = send_time.hour
                    minute = send_time.minute
                    kit.sendwhatmsg(contact["Raja"], msg, hour, minute)    
                    time.sleep(20)
                    agu.press("enter")
                    time.sleep(5)
                    agu.hotkey('ctrl', 'w')
                    agu.press("enter")

                except Exception as e:
                    speak("There is a time error... please try again")

            elif("shanu" in name):
                speak("What do I message?")
                msg = take_command().lower()

                try:
                    now = datetime.now()
                    send_time = now + timedelta(minutes=1)
                    hour = send_time.hour
                    minute = send_time.minute
                    kit.sendwhatmsg(contact["Sanu"], msg, hour, minute)    
                    time.sleep(20)
                    agu.press("enter")
                    time.sleep(5)
                    agu.hotkey('ctrl', 'w')
                    agu.press("enter")

                except Exception as e:
                    print("There is a time error... please try again")

            elif("gopal" in name):
                speak("What do I message?")
                msg = take_command().lower()

                try:
                    now = datetime.now()
                    send_time = now + timedelta(minutes=1)
                    hour = send_time.hour
                    minute = send_time.minute
                    kit.sendwhatmsg(contact["Gopal"], msg, hour, minute)    
                    time.sleep(20)
                    agu.press("enter")
                    time.sleep(5)
                    agu.hotkey('ctrl', 'w')
                    agu.press("enter")

                except Exception as e:
                    print("There is a time error... please try again")

            elif("arindam" in name):
                speak("What do I message?")
                msg = take_command().lower()

                try:
                    now = datetime.now()
                    send_time = now + timedelta(minutes=1)
                    hour = send_time.hour
                    minute = send_time.minute
                    kit.sendwhatmsg(contact["Arindam"], msg, hour, minute)    
                    time.sleep(20)
                    agu.press("enter")
                    time.sleep(5)
                    agu.hotkey('ctrl', 'w')
                    agu.press("enter")

                except Exception as e:
                    print("There is a time error... please try again")

            elif("adhikari" in name) or ("soham" in name) or ("adhi" in name):
                speak("What do I message?")
                msg = take_command().lower()

                try:
                    now = datetime.now()
                    send_time = now + timedelta(minutes=1)
                    hour = send_time.hour
                    minute = send_time.minute
                    kit.sendwhatmsg(contact["Adhikari"], msg, hour, minute)    
                    time.sleep(20)
                    agu.press("enter")
                    time.sleep(5)
                    agu.hotkey('ctrl', 'w')
                    agu.press("enter")

                except Exception as e:
                    print("There is a time error... please try again")

            elif("shri" in name) or ("sreejita" in name):
                speak("What do I message?")
                msg = take_command().lower()

                try:
                    now = datetime.now()
                    send_time = now + timedelta(minutes=1)
                    hour = send_time.hour
                    minute = send_time.minute
                    kit.sendwhatmsg(contact["Sree"], msg, hour, minute)    
                    time.sleep(20)
                    agu.press("enter")
                    time.sleep(5)
                    agu.hotkey('ctrl', 'w')
                    agu.press("enter")

                except Exception as e:
                    print("There is a time error... please try again")

            else:
                speak(f"Sorry I don't have the number of {name}")

        elif("rest" in query):
            speak("Thank You!")
            break

        elif("shut down" in query):
            speak("Ok sir!!")
            os.system("shutdown /s /t 0")

        elif("restart" in query):
            speak("Ok sir...\nGood Bye!!")
            os.system("shutdown /r /t 1")
        
        elif("sleep" in query):
            speak("Putting the system to sleep mode...")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        else:
            sorry = ["Sorry, I'm not function to do that!!","I'm Sorry I'm not able to do that.","I'm upgreading myself... \nSo right now I can't do that!! but after some times I'll be able to do that."]
            speak(random.choice(sorry))


