from tkinter import *

CLICK = 0


def button_clicked():
    global CLICK
    user = input_entry.get()
    CLICK += 1
    my_label.config(text=f"{user} clicked the button {CLICK} times!")


# GUI - Graphical User Interface
window = Tk()
window.title("My First GUI Program")
window.minsize(width=600, height=400)
window.config(padx=20,pady=20)

# Label
my_label = Label(text="I'm a Label", font=("Courier", 15, "bold"))
my_label.config(text="New Text")
# my_label.pack()  # pack(side="left")
# my_label.place(x=200,y=200)  place
my_label.grid(column=0, row=0)

# Button

button = Button(text="Click me!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2,row=0)

# Entry

input_entry = Entry(width=10)
# input_entry.pack()
input_entry.grid(column=3, row=2)

window.mainloop()
