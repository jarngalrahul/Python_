# API - An Application Programming Interface (API) is a set of commands, functions,
# protocols, and objects that programmers can use to create software or
# intreact with an external system.

import datetime
import os
import smtplib
import time
import requests
MY_LAT = 99
MY_LONG = 99

# ------------iss api for its position----------#


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG+5:
        return True
# ------------------------Sunset-sunrise api with parameters------------------------#


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response_2 = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response_2.raise_for_status()
    data = response_2.json()
    sunrise = int(data["results"]["sunrise"].split("T")
                  [1].split(":")[0])  # sunrise hour
    sunset = int(data["results"]["sunset"].split("T")
                 [1].split(":")[0])  # sunset hour
    time = datetime.datetime.now().hour

    if time >= sunset or time <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and iss_overhead():
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=os.environ.get("GOOGLE_TEST_MAIL"),
                             password=os.environ.get("GOOGLE_TEST_PASSWORD"))
            connection.sendmail(from_addr=os.environ.get("GOOGLE_TEST_MAIL"),
                                to_addrs="pythontesting1922@gmail.com",
                                msg="Subject:Look out bro👆\n\nIss is overhead you in the sky")
