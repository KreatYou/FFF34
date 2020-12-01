from tkinter import Tk, Frame, Label, Text, \
    Scrollbar, Button, PhotoImage, END, W, E
import translators as ts
import pyttsx3
from datetime import datetime, date, time


def translate(get_text):
    output = ts.google(get_text, to_language='ru', if_use_cn_host=True)
    text2.delete(1.0, END)
    text2.insert(END, output)


def window():
    win_text = text1.get(1.0, END)
    if len(win_text) < 4:
        win_text = 'Enter text more than two characters'
        text1.delete(1.0, END)
        text1.insert(END, win_text)
    translate(win_text)


def clipboard():
    try:
        clip_text = root.clipboard_get()
    except BaseException:
        clip_text = 'Буфер обмена пуст'
    text1.delete(1.0, clip_text)
    text1.inssert(END, clip_text)
    trancelate(clip_text)


root = Tk()
root.title('Translate')

lab0 = Label(root, font='arial 11 bold', fg='Pink', bg='Pink')
lab0.grid(row=0, column=0, sticky=W + E, columnspan=2, pady=2)

f1 = Frame(root)
f1.grid(row=1, column=0)
text1 = Text(f1, font='arial 12', wrap='word', width=50, height=12, bg="Pink", padx=10, pady=10)
text1.pack(side='left')
scroll1 = Scrollbar(f1, command=text1.yview)
scroll1.pack(side='right', fill='y')
text1['yscroll'] = scroll1.set
lab1 = Label(text1, fg='Pink', bg='Pink')
root.update()
x, y = text1.winfo_width(), text1.winfo_height()
lab1.place(x=x - 35, y=y - 35)

f2 = Frame(root)
f2.grid(row=1, column=1)
text2 = Text(f2, font='arial 12', wrap='word', width=50, height=12, bg='Pink', padx=10, pady=10)
text2.pack(side='left')
scroll2 = Scrollbar(f2, command=text2.yview)
scroll2.pack(side='right', fill='y')
text2['yscroll'] = scroll2.set
lab2 = Label(text2, fg='Pink', bg='Pink')
lab2.place(x=x - 35, y=y - 35)

bt1 = Button(root, text='Translate window', font='aril 12', fg='Pink', command=window)
bt1.grid(row=2, column=0, stick=W + E)

bt2 = Button(root, text='Translate clipboard', font='aril 12', fg='Pink', command=clipboard)
bt2.grid(row=2, column=1, stick=W + E)

bt3 = Button(root, text='vs', font='aril 12', fg='Pink', command=window)
bt3.grid(row=2, column=1, stick=W + E)

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

root.mainloop()
