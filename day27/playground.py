from tkinter import *

window = Tk()

# GUI - Graphical User Interface

window.title("My First GUI Program")
window.minsize(width=600, height=400)

# Label
my_label = Label(text="I'm a Label", font=("Courier", 15, "bold"))
my_label.pack()  # pack(side="left")

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Entry

input_entry = Entry(width=10)
input_entry.pack()

# Button
click = 0

def button_clicked():
    global  click
    user = input_entry.get()
    click += 1
    my_label.config(text=f"{user} clicked the button {click} times!")

button = Button(text="Click me!", command=button_clicked)
button.pack()



window.mainloop()
