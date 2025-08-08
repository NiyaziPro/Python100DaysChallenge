import datetime as dt
import os
import random
import smtplib

from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
email_to_send = os.getenv("EMAILTOSEND")

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)

if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_to_send,
            msg=f"Subject:Monday Motivation :)\n\n{quote}")
    connection.close()
