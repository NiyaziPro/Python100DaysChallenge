import os
import smtplib

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
EMAILTOSEND = os.getenv("EMAILTOSEND")

URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.select_one("span.aok-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

################# Send an Email ####################
title = soup.find(id="productTitle").getText().strip()
BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAILTOSEND,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
