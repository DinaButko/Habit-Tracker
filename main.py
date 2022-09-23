import requests
from  datetime  import datetime

# URL for graph https://pixe.la/v1/users/dina/graphs/graph1.html

# 1. Create a user

USERNAME = "XXXXX"
TOKEN = "XXXXXX"
pixela_endpoint = "https://pixe.la/v1/users"
today = datetime.now()

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"

graph_params = {

    "id": graph_id,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(graph_response.text)

#3 Post a day



post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"

post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "30",
}

post_response = requests.post(url=post_endpoint, json=post_params, headers=headers)
print(post_response.text)