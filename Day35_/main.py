# API- using authentication keys, etc....
import requests
key = "fc4a07f6debb37aaff4bef91567e0756"
key2 = "69f04e4613056b159c2761a9d9e664d2"
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
i = 0
while i in range(0, 12):
    id = hourly_weather[i]['weather'][0]['id']
    i += 1
    if id < 700:
        print("Bring your umbrella.")
