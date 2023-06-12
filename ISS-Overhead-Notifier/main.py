import requests
from datetime import datetime;
import smtplib;
from env import vault;

MY_LAT = 51.507351
MY_LONG = -0.127758

with requests.get(url="http://api.open-notify.org/iss-now.json") as response:
    response.raise_for_status() # Raise exception if error
    
    data = response.json()
    print(data)
    
    iss_latitiude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    iss_position = (latitiude, longitude)
    print(iss_position)
    
#Location of London    
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "formatted": 0
}

sun_response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
    
sun_response.raise_for_status()
sun_data = sun_response.json()

sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])


# If ISS is close to London and it is currently dark send me an email

def is_iss_overhead():
    if MY_LAT - 5 <= iss_latitiude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    
def is_night():
    if sunset <= time_now <= sunrise:
        return True
    
if true:
    
    with smptlib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=vault["email"], password=vault["password"])
        connection.sendmail(
            from_addr=vault["email"], 
            to_addrs=vault["reciever_email"], 
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )
        print("Email sent")
        