# API- using authentication keys, etc....
# method : setx keyname "value"
# finding it back: set | findstr keynamE
import os
import requests
key = os.environ.get("key")
key2 = os.environ.get("key2")
parameters = {
    "lat": 32.726601,
    "lon": 74.857025,
    "appid": key2,
    "exclude": "current,minutely,daily",
}
response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
hourly_weather = data['hourly']
print(hourly_weather)
i = 0
while i in range(0, 12):
    id = hourly_weather[i]['weather'][0]['id']
    i += 1
    if id < 700:
        print("Bring your umbrella.")
        # send mail or message using python
