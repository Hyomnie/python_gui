import tkinter
from tkinter import *

def font_control(ev):
    label.config(font="HY헤드라인M %d bold"%v.get())
    
win = tkinter.Tk()
win.geometry('350x150')
v = IntVar()

label = Label(win, text='hello')
label.pack(fill=Y, expand=1)
sc = Scale(win, from_=10, to=40, orient=HORIZONTAL, variable=v, command=font_control())
v.set(14)
sc.pack(fill=X, expand=1)
qbtn = Button(win, text="exit", command=win.quit)
qbtn.pack()

win.mainloop()

##안돌아가지만 일단올려...
