import requests
from datetime import datetime

USER = "user"
TOKEN = "token"

MY_PROFILE = "https://pixe.la/@i0ana"

user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

pixela_endpoint= "https://pixe.la/v1/users"


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

GRAPH_ID= "graph1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling123",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

today = datetime.now()
FORMATTED_DATE = today.strftime("%Y%m%d")
print(FORMATTED_DATE)

headers = {
    "X-USER-TOKEN": TOKEN
}
# response1 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response1.text)

pixel_config = {
    "date": FORMATTED_DATE,
    "quantity": "5",
}
pixel_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"
# response3 = requests.put(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response3.text)

pixel_update_ep = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}/{FORMATTED_DATE}"
# response4 = requests.put(url=pixel_update_ep, json=pixel_config, headers=headers)
# print(response4.text)


del_pixel_ep = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}/{FORMATTED_DATE}"
# response5 = requests.delete(url=del_pixel_ep, headers=headers)
# print(response5.text)