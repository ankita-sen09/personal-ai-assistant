import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import datetime

r = sr.Recognizer()
email = "senankita408@gmail.com"

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.say(command)
    engine.runAndWait()

def play_song(song_name):
    try:
        speak(f"Playing {song_name}.")
        # Open the YouTube video in the default web browser
        webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
    except Exception as e:
        print(f"Error playing song: {e}")

def commands():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            my_text = r.recognize_google(audio)
            my_text = my_text.lower()
            print(my_text)
            speak(my_text)

            if 'play' in my_text:
                my_text = my_text.replace('play', '').strip()
                speak('Playing ' + my_text)
                pywhatkit.playonyt(my_text)

            elif "date" in my_text:
                today = datetime.date.today()
                speak(str(today))

            elif "time" in my_text:
                current_time = datetime.datetime.now().strftime("%H:%M")
                speak("The current time is " + current_time)

            elif "who is" in my_text:
                search_query = my_text.replace("who is", "").strip()
                info = wikipedia.summary(search_query, 1)
                speak(info)

            elif "email" in my_text:
                speak("Your email address is " + email)

            else:
                print("Please ask correct questions!")

    except Exception as e:
        print(f"Error in capturing microphone: {e}")

text_to_speak = "This is my project"

# Detect voice and activate commands
try:
    speak(text_to_speak)
except Exception as e:
    print(f"Error: {e}")

'while True:'
    commands()
