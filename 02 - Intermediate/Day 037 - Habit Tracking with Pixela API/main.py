from datetime import datetime

import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "alaknsdrn2h5n4jklna"
USERNAME = "nikko90"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph1"

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT,json=graph_params, headers=headers)
# print(response.text)

PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15",
}

# response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data,headers=headers)
# print(response.text)

UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_data = {
    "quantity": "4.5"
}

# response = requests.put(url=UPDATE_ENDPOINT, json=update_data,headers=headers)
# print(response.text)

DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

response = requests.delete(url=DELETE_ENDPOINT,headers=headers)
print(response.text)