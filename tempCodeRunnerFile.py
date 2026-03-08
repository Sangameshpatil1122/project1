import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        
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
                audio = r.listen(source , timeout=3, phrase_time_limit=3)
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
        