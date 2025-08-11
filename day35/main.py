import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

API_KEY = "Your Api Key"

MY_LAT = 53.865467
MY_LONG = 10.686559

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url=BASE_URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")