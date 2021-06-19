import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as web
import os
import pyautogui
import pywhatkit


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate=170
engine.setProperty('rate',newVoiceRate)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I :%M :%S")
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("Today's date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Yash")
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("GOOD MORNING")
    elif hour>=12 and hour<16:
        speak("GOOD AFTERNOON")
    elif hour>=16 and hour<=24:
        speak("GOOD EVENING")
    else:
        speak("GOOD NIGHT")

    speak("ALEXA AT YOUR SERVICE,HOW CAN I HELP YOU")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio ,language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("CAN U SAY THAT AGAIN PLEASE.....")

        return "None"

    return query 
def screenshot():
    img=pyautogui.screenshot()
    img.save("E:\lapt\sa.png")         

if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        print(query)
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "sleep" in query:
            quit()  
        elif "wikipedia" in query:
            speak("searching")
            query = query.replace("wikipedia"," ")
            result=wikipedia.summary(query, sentences=2)
            speak(result)
        elif "search in youtube" in query:
            speak("what should I search?")
            search = takeCommand().lower()
            pywhatkit.playonyt(search)      
        
        elif "remember that" in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("u said me to remember " +data)
            remember = open("rem.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open("rem.txt","r")
            speak("u said me to remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("took the screenshot")
