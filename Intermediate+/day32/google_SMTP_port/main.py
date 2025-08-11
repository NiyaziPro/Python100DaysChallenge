import os
import smtplib

from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="emailtosend@gmail.com",
        msg="Subject:Hello from Python :)\n\nThis is the body of email!")
    connection.close()
