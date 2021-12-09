import tkinter as tk
from tkinter import ttk

def click_me():
    action.configure(text='**i have been clicked!**')
    hello.configure(foreground='red')
    hello.configure(text='a red label')

def enter_name():
    action2.configure(text='hello ' + name.get())
    
win = tk.Tk()
win.title('python gui')
win.geometry('300x300')

hello = ttk.Label(win, text='a label', relief='ridge')
hello.grid(column=0, row=0)

action = ttk.Button(win, text='click me!', command=click_me)
action.grid(column=1, row=0)

ttk.Label(win, text='enter a name:').grid(column=0, row=1)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=2)

action2 = ttk.Button(win, text='click me!', command=enter_name)
action2.grid(column=1, row=2)

win.mainloop()
