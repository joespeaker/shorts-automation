
# Python program to show 
# how to convert text to speech 
import pyttsx4

# Initialize the converter 
engine = pyttsx4.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 190)
engine.setProperty('volume', 0.9)
engine.setProperty('pitch', 1.1)
engine.setProperty('voice', 'com.apple.voice.compact.en-GB.Daniel')

# get input from text.txt
def get_input():
    with open('text.txt', 'r') as f:
        text = f.read()
    return text

# Converts the text into audio
engine.say(get_input())
engine.runAndWait()

#Daniel
#