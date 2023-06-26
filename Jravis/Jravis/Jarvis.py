import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import cv2
import random
import speech_recognition as sr
import smtplib
import sys
import pywhatkit as kit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
 

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    elif hour>=18 and hour<21:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("I am Jarvis sir Please tell me how can I help you.")



def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:   
        print("Listening....")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        speak(f"Performing: {query}\n")
    except Exception as e:
        speak("Please repeat the sentence said....")
        return "None"
    return query



if __name__ == '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()

        #Logic for executing command
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)



        elif'open youtube' in query:
            speak("sir waht you would like to watch on youtube")
            cm = takeCommand().lower()
            kit.playonyt(f"{cm}")
            

        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")      

        elif 'open stack overflow' in query:
            webbrowser.open("stack overflow.com")

        elif 'play music' in query:
            music_dir='D:\\Music\\'
            songs=os.listdir(music_dir)
            d=random.choice(songs)
            print(songs)
            os.startfile('D:\\Music\\'+d)

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}")
        
        elif 'open code' in query:
            vscodePath="C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(vscodePath)  

        elif 'open notepad' in query:
            notepadPath="C:\\Program Files\\Notepad++\\Notepad++.exe"
            os.startfile(notepadPath)

        elif 'open command prompt' in query:
            os.system("start cmd")  

        elif "send whatsapp message" in query:
            speak("sir, what message you want to send")
            cm = takeCommand().lower()
            kit.sendwhatmsg("+919096404657",f"{cm}",6,48)
        
            
        elif 'open camera' in query: 
            cap = cv2.VideoCapture(0)
            while True:
                ret, img= cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
                cap.release()
                cv2.destoryAllWindows()


        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        speak("sir, do you have any other work")    





                  
    
