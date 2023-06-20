import random
import webbrowser

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import wolframalpha
import os
import playsound
from playsound import playsound

WAKE_WORD = "alexa"

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def hello():
    talk("Hello Mam i am your Personal Alexa... what can i help to to finding something .tell me that.")


def tellDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        talk("The day is " + day_of_the_week)


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if WAKE_WORD in command:
                command = command.replace(WAKE_WORD, '')
                print(command)



    except sr.RequestError:
        print('Could not connect to the internet')
        return ""


    except sr.UnknownValueError:
        print('Sorry, I did not understand what you said')
        return ""


    except sr.WaitTimeoutError:
        print('Sorry, I timed out while waiting for you to speak')
        return ""

    return command.strip()


def run_alexa():
    command = take_command()
    if not command:
        return

    if 'playing' in command.split()[0]:
        song = command.replace('playing', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'send message on whatsapp' in command:
        talk("yes i can send message on whatsapp.")
        pywhatkit.sendwhatmsg("+919822611110", "Hi Mam....", 13,8)

        # pywhatkit.sendwhatmsg("+919309580344","Hi"12,30,15,True,2)

    elif 'how are you' in command:
        talk(' I am fine, Thank you')
        talk('How are you ,sir/madam')

    elif 'fine' in command:
        talk('It is good to know that your fine')


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)


    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'from wikipedia' in command:
        talk("Checking the wikipedia ")
        command = command.replace("wikipedia", " ")
        result = wikipedia.summary(command, sentences=5)
        talk('According to wikipedia')
        print(result)
        talk(result)

    elif 'date' in command:
        tellDay()
    elif 'restart' in command:
        subprocess.call(["shutdown", "/r"])

    #elif 'sleep' or 'off' in command:
       # talk('switching off system')
        #subprocess.call(["shutdown / h "])

    #elif 'show notes' in command:
      #  talk('Showing notes')
        #file = open("upsc.txt","r")
       # print(file.read)
       # talk(file.read(6))



    elif 'open google' in command:
        talk('Google is open now')
        webbrowser.open("www.google.com")


    elif 'open gmail' in command:
        talk(" Gmail is open now ")
        webbrowser.open_new_tab("www.gmail.com")

    elif 'news' in command:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        talk('here are some headlines from the Times of India.Happy reading')

    elif 'search' in command:
        command = command.replace("search", "")
        webbrowser.open_new_tab(command)

    elif 'Which day it is' in command:
        tellDay()


    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'love you' in command:
        talk('Love you too...')

    elif 'can you entertain me' in command:
        talk('I can entertained you. Just tell me what i can do that.. for example play some song, telling a comedy jokes any thing you want.')



    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'play mp3 song' in command:
        music_dir = 'C:\Music'
        songs = os.listdir(music_dir)
        song = random.randint(0, len(songs) - 1)
        print(songs[song])
        talk("play{songs[song]}")
        os.startfile(os.path.join(music_dir, songs[0]))


    elif 'Calculate' in command:
        app_id = 'P668LL-EY8LLWXL3T'
        client = wolframalpha.Client('P668LL-EY8LLWXL3T')
        index = command.lower().split().index('Calculate')
        command = command.split()[index + 1:]
        res = client.command(' '.join(command))
        answer = next(res.results).text
        print('Answer is  ' + answer)
        talk('Answer is  ' + answer)



    elif 'stop' in command:
        talk('Goodbye')
        exit()


    else:
        talk('Sorry, I did not understand what you said')


talk('Starting up Alexa...')
while True:
    print('Listening for command...')
    run_alexa()




