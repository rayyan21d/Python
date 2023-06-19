import requests
from datetime import datetime

USER_NAME = "rayyan"
TOKEN = "jdihih80w9i#i*&jhjk844H"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime(year=2023, month=6, day=15)
date = today.strftime("%Y%m%d")

pixel_data ={
    "date":date,
    "quantity":"50",
}

USER_PARAMS = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_config = {
    "id":"graph1",
    "name":"Coding Graph",
    "unit":"minutes",
    "type":"int",
    "color":"ajisai"
    
}

headers = {
    "X-USER-TOKEN":TOKEN
}    
    
# Create a user
# response = requests.post(pixela_endpoint,json=USER_PARAMS,)
# print(response.json())

# Create a graph
# graph = requests.post(graph_endpoint,json=graph_config, headers=headers)
# print(graph.text)

# Create a pixel
response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)

print(response.text)

