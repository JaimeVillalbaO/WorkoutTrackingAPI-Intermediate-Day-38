import requests
from datetime import datetime
import os

app_id = os.environ.get('ID_TRACK')
app_keys = os.environ.get('KEYS_TRACK')

gender = 'male'
weight = 83
height = 180
age = 28

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

excercise_text = input('Tell me wich exercises you did: ')

headers = {
    "x-app-id": app_id,
    "x-app-key": app_keys, 
}

parameters = {
    'query' : excercise_text, 
    'gender' : gender, 
    'weight_kg' : weight, 
    'height_cm' : height, 
    'age' : age
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)

results = response.json()
print(results)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_endpoint = 'https://api.sheety.co/f41b8c95a70fdcd5f74702ffddbe6ed3/workoutTracking/workouts'
for exercise in results["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)
    

    print(sheet_response.text)
    
#Basic Authentication
# bearer_headers = {
#         'Authorization' : 'Basic amFpbWV2aWxsYWxiYToxNTA0MzQwMA=='
#     }
# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)


# #Bearer Token Authentication
# bearer_headers = {
# "Authorization": "Bearer 09ijhgt65432wdrty78"
# }
# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)