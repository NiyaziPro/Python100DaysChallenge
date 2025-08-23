import datetime as dt
import os
import random
import smtplib

import pandas
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
email_to_send = os.getenv("EMAILTOSEND")

now = dt.datetime.now()
month = now.month
day = now.day
print(day, month)

birthdays = pandas.read_csv("birthdays.csv")
todays_birthdays = birthdays[(birthdays.month == month) & (birthdays.day == day)]

if not todays_birthdays.empty:
    folder = "letter_templates"
    letter_templates = [os.path.join(folder, f"letter_{i}.txt") for i in range(1, 4)]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)

        for index, birthday_person in todays_birthdays.iterrows():
            chosen_letter = random.choice(letter_templates)
            with open(chosen_letter, 'r') as file:
                letter_content = file.read()

            personalized_letter = letter_content.replace("[NAME]", birthday_person["name"])

            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
            )
            print(f"E-posta gönderildi: {birthday_person['name']} - {birthday_person['email']}")
