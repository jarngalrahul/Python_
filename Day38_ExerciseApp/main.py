import datetime
import requests
import os
APPLICATION_ID = os.environ.get("APPLICATION_ID_NUTRITIONX")
APPLICATION_KEY = os.environ.get("APPLICATION_KEY_NUTRITIONX")
TOKEN = os.environ.get("sheety_auth_token")
url_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
spreadsheet_endpoint = os.environ.get("spreadsheet_endpoint")
cur_dt = datetime.datetime.now()

# ------------------------Selecting data from user using nutrition-x-----------------------#
headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_KEY
}

query_text = input("Enter the exercise you did today?  ")
parameters = {
    "query": query_text,
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 180,
    "age": 19,
}
sheety_header = {
    "Authorization": f'Bearer {TOKEN}'
}
response = requests.post(
    url=url_endpoint, json=parameters, headers=headers)
response.raise_for_status()
print(response.json())

# -----------------------Using the sheety api to print the data to spreadsheets---------------------#
for result in response.json()['exercises']:
    data = {
        "workout": {
            "date": cur_dt.strftime("%x"),
            "time": cur_dt.strftime("%X"),
            "exercise": result['name'].lower().title(),
            "duration": result['duration_min'],
            "calories": result['nf_calories']
        }}
    response = requests.post(url=spreadsheet_endpoint,
                             json=data, headers=sheety_header)
    print(response.text)
