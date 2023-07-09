import requests
from datetime import datetime

USER = "fouzan"
TOKEN = "869giguyg838dg2vi8272ug"
day = datetime(year=2023, month=6, day=7).strftime("%Y%m%d")
pixela_endpoint =  "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"
user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_params = {
    "id": "graph2",
    "name": "Swimmin Graph",
    "unit": "M",
    "type": "float",
    "color": "ajisai"     
}

request_body_update = {
    "date": day,
    "quantity": "500"
}

header = {
    "X-USER-TOKEN": TOKEN
}

response = requests.put(url=f"{graph_endpoint}/graph2/{day}", json=request_body_update, headers=header)
print(response.text)