import requests

with requests.get(url="http://api.open-notify.org/iss-now.json") as response:
    response.raise_for_status() # Raise exception if error
    
    data = response.json()
    print(data)
    
    latitiude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    
    iss_position = (latitiude, longitude)
    print(iss_position)