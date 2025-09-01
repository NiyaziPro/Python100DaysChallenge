from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = (
            [choice(letters) for _ in range(0, nr_letters)] +
            [choice(symbols) for _ in range(0, nr_symbols)] +
            [choice(numbers) for _ in range(0, nr_numbers)]
    )
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- COPY TO CLIPBOARD PASSWORD ------------------------------- #
def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        # messagebox.showinfo(title="Copied", message="Password copied to clipboard!")
    else:
        messagebox.showwarning(title="No Password", message="There is no password to copy!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) <= 0 or len(email) <= 0 or len(password) <= 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.txt", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password} \n")
                    website_entry.delete(0, END)
                    # email_entry.delete(0,END)
                    password_entry.delete(0, END)
            except IOError:
                messagebox.showerror(title="Error", message="Could not write to file!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
try:
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
except TclError:
    messagebox.showwarning(title="Warning", message="Logo image not found!")
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry's
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "abc@xyz.com")
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Buttons
generate_pass_button = Button(text="Generate Password", width=44, command=generate_password)
generate_pass_button.grid(column=1, row=4, columnspan=2)

copy_button = Button(text="Copy to Clipboard", command=copy_password)
copy_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, columnspan=2, row=5)

exit_button = Button(text="Exit", width=44, command=window.quit)
exit_button.grid(column=1, row=6, columnspan=2)

window.mainloop()
