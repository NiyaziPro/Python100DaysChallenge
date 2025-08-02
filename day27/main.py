# https://docs.python.org/3/library/tkinter.html#the-packer
# https://www.tcl-lang.org/man/tcl8.6/TkCmd/pack.htm

import tkinter
from turtle import Turtle

window = tkinter.Tk()

# GUI - Graphical User Interface

window.title("My First GUI Program")
window.minsize(width=600, height=400)

# Label
my_label = tkinter.Label(text="I'm a Label", font=("Courier", 24, "bold"))
my_label.pack()

t = Turtle()
t.write()

window.mainloop()
