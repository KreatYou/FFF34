from tkinter import Tk, Frame, Label, Text, Scrollbar , \
    Button, PhotoImage, END, W, E



def winow():
    pass


def clipboard():
    pass



root = Tk()
root.title('Translate')

lab0 = Label(root, font='arial 11 bold', fg='white',  bg='pink')
lab0.grid(row=0, column=0, sticky=W + E, columnspan=2 )
f1 = Frame(root)
f1.grid(row=1, column=0)
text1 = Text(f1, font='arial 12', wrap='word', width=50, height=12, padx=10, pady=10)
text1.pack()

f2 = Frame(root)
f2.grid(row=1, column=1)
text2 = Text(f2, font='arial 12', wrap='word', width=50, height=12, padx=10, pady=10)
text2.pack()

bt1 = Button(root, text='Translite window', font='aril 12', fg='pink', )
bt1.grid(row=2, column=0, stick=W + E)

bt2 = Button(root, text='Translite clipboard', font='aril 12', fg='pink', )
bt2.grid(row=2, column=1, stick=W + E)
root.mainloop()
