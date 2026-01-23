#libraries
import pyttsx3

#vairables
engine = pyttsx3.init()


#functions
def audio(text, speed):
    engine.setProperty('rate', speed)
    engine.say(text)
    engine.runAndWait()
