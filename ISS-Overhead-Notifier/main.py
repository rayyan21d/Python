import requests

with requests.get(url="http://api.open-notify.org/iss-now.json") as response:
    print(response.json)
    