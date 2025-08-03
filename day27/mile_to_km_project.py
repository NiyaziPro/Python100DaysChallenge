from tkinter import *


def calculate_mile_to_km():
    try:
        km = float(input_miles.get()) * 1.60934
        label_result.config(text=f"{km:.2f}")
    except ValueError:
        label_result.config(text="Invalid number!")


window = Tk()
window.minsize(width=300, height=50)
window.title("Mile to Km Converter")
window.config(padx=50, pady=20)

input_miles = Entry()
input_miles.grid(column=1, row=0)
input_miles.config(width=10)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

label_equals = Label(text="is equal to")
label_equals.grid(column=0, row=1)

label_result = Label(text=0)
label_result.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

calculate = Button(text="Calculate", command=calculate_mile_to_km)
calculate.grid(column=1, row=2)

exit_button = Button(text="Exit", command=window.quit)
exit_button.grid(column=1, row=3)

window.mainloop()
