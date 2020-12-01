import pyttsx3
from datetime import datetime, date, time
tts = pyttsx3.init()
tts.setProperty('voice', 'ru')
tts.setProperty('rate', 150)
tts.setProperty('volume', 0.8)

voices = tts.getProperty('voices')
for voice in voices:
    print(voice.name)

for voice in voices:
    if 'Irina'in voice.name:
        tts.setProperty('voice', voice.id)

def say_time(text):
    tts.say(text)
    tts.runAndWait()

time_now = datetime.now()
say_time(f'{time_now.hour} часов {time_now.minute} минут')
