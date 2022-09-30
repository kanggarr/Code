from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("tenten Clock")


def time():
    string = strftime("%Y-%m-%d %H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80),
            background="black", foreground="#FFFFCC")
label.pack(anchor='center')
time()
mainloop()
