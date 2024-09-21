from gtts import gTTS
import os

def audio_book(text_file, audio_file):
    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()
        
    tts = gTTS(text=text, lang='en')
    tts.save(audio_file)
    print(f'audio_file save as {audio_file}')
text_file = 'C:/Users/user/Documents/Python2024/PythonOOP/poem.txt'
audio_file = 'C:/Users/user/Documents/Python2024/PythonOOP/poem.mp3'

audio_book(text_file, audio_file)
os.system(f'start{audio_file}')
        
        
    
