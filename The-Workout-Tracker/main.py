import requests
import datetime

APP_ID = "7bbfa4ef"
API_KEY = "2477c4d1db4222de8314a6c8379b08f1"
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/a2dd0dbf19dab537a97213058fc85451/myWorkouts/workouts"


YOUR_USERNAME = "rayyan"
YOUR_PASSWORD = "ApassowrdIsSafe3#"


GENDER = "Male"
WEIGHT_KG = 80
HEIGHT_CM = 190
AGE = 20

workout_query = input("What exercise did you do today?\n")

headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}

parameters = {
    "query": workout_query, 
    "gender": GENDER,
    "weight_kg": WEIGHT_KG, 
    "height_cm": HEIGHT_CM, "age": AGE
}

workout_output = requests.post(
    API_ENDPOINT,
    json=parameters,
    headers=headers
).json()


date = datetime.date.today().strftime("%d-%m-%Y")
time = datetime.datetime.now().strftime("%H:%M:%S")
duration = workout_output["exercises"][0]["duration_min"]
exercise = workout_output["exercises"][0]["name"]
calories = workout_output["exercises"][0]["nf_calories"]

sheet_inputs = {
    
    "workout": {
        "date": date, 
        "time": time,
        "exercise": exercise,
        "duration": duration, 
        "calories": calories
    }
}

sheet_response = requests.post(
    
    SHEET_ENDPOINT,
    json=sheet_inputs,
    auth=(
        YOUR_USERNAME,
        YOUR_PASSWORD,
    )
)

print("Response added!")
