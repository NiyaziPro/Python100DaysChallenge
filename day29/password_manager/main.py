from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, END


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password} \n")
        website_entry.delete(0, END)
        #email_entry.delete(0,END)
        password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
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
generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(column=2, row=3, columnspan=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, columnspan=2, row=4)

exit_button = Button(text="Exit", width=44,command=window.quit)
exit_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
