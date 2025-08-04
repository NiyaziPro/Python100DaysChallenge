from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100 , image=logo_img)
canvas.grid(column=1,row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

# Entry's
website_entry = Entry(width=52)
website_entry.grid(column=1,row=1,columnspan=2)
email_entry = Entry(width=52)
email_entry.grid(column=1,row=2, columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(column=1,row=3)

# Buttons
generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(column=2,row=3, columnspan=2)

add_button = Button(text="Add", width=44)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()