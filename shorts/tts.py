import gtts
from pydub import AudioSegment
import slow
import os

#read text from file text.txt
def get_input():
    with open('text.txt', 'r') as f:
        text = f.read()
    return text

#convert text to speech
def text_to_speech(text):
    tts = gtts.gTTS(text , lang='en', tld='com.au')
    tts.save('text.mp3')

#convert mp3 to wav file
def mp3_to_wav(file_name, name):
    file = str(file_name)
    sound = AudioSegment.from_mp3(file)
    sound.export(name, format="wav")
    os.remove(file)
    return name


#run functions
text_to_speech(get_input())
text = mp3_to_wav('text.mp3', "output.wav")
slow.stretch('output.wav', 0.85)
