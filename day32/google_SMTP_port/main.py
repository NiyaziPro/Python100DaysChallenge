import smtplib

my_email = "test@gmail.com"
password = "apppasswords"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="email@gmail.com",
        msg="Subject:Hello from Python :)\n\nThis is the body of my email!")
    connection.close()
