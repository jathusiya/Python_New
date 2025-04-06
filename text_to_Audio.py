from gtts import gTTS #text to speech
import os

abc = open('sample.txt')
text = abc.read() #text that you want to convert

language = 'en' 

obj = gTTS(text, lang=language,slow=False)

obj.save("sample.mp3")

os.system(sample.mp3)