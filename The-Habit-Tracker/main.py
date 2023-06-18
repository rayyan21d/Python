import requests

USER_NAME = "rayyan"
TOKEN = "jdihih80w9i#i*&jhjk844H"


pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

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
    


# response = requests.post(pixela_endpoint,json=USER_PARAMS,)
# print(response.json())

graph = requests.post(graph_endpoint,json=graph_config, headers=headers)
print(graph.text)