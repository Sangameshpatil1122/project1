import speech_recognition as sr
import webbrowser
import pyttsx3
import client
import musiclibrary
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def aiprocess(command):
    client = OpenAI(api_key="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")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis, skilled in general tasks like alexa and google cloud "},
        {"role": "user", "content": command}
    ]
)
    return completion.choices[0].message


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link=musiclibrary.music[song] 
        webbrowser.open(link)
    elif "show news" in c.lower():
        news=webbrowser.open("https://news.google.com") 

    else:
        #let openai handle the request
        output=aiprocess(c)
        speak(output)

if __name__ == "__main__":
    speak("initializing jarvis....")
    while True:
        #listen for the wake word "jarvis"
        #obtain audio from the microphone
        r=sr.Recognizer()
        

        print("Recognizing...")

        #recognize speech using google speech recognition
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout=3, phrase_time_limit=1)
            word=r.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("yesss sir, how can i help you?")
                #listen for the command
                with sr.Microphone() as source:
                    print("jarvis active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        
        except Exception as e:
            print(" error {0}".format(e))
        