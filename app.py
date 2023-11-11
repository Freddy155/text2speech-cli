from gtts import gTTS
import os

mytext = input("Enter the text you want to convert to audio: ")
language = input("Enter the language (e.g., 'en' for English): ")
myobj = gTTS(text=mytext, lang=language, slow=False)
filename = input("Enter the filename to save the audio (e.g., 'welcome.mp3'): ")
myobj.save(filename)
os.system(f"mpg321 {filename}")
