import tkinter as tk
from tkinter import *
    
win = tk.Tk()
win.geometry('300x300')

colors = ['blue', 'gold', 'red']

def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background = colors[0])
    elif radSel == 1:
        win.configure(background = colors[1])
    elif radSel == 2:
        win.configure(background = colors[2])

radVar = tk.IntVar()
radVar.set(99)

for col in range(3):
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)

win.mainloop()
