import os
import requests
url_endpoint = 'https://api.sheety.co/64766665ed6253ea153c83d824dd8641/copyOfFlightDeals/prices'
TOKEN = os.environ.get("sheety_auth_token")

sheety_header = {
    "Authorization": f'Bearer {TOKEN}'
}
FLIGHT_USERS_ENDPOINT = "https://api.sheety.co/64766665ed6253ea153c83d824dd8641/copyOfFlightDeals/users"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(url=url_endpoint, headers=sheety_header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{url_endpoint}/{city['id']}", headers=sheety_header, json=new_data)
            print(response.text)

    def get_user_data(self):
        print("Welcome to Rahul's flight club.\nWe find best flight deals and email you.")
        first_name = input("What is your name?\n")
        last_name = input("What is your last name?\n")
        email = input("Enter your email - ")
        if email == input("Enter your email again!! - "):
            print("You are in the club!")
            sheety_header = {
                "Authorization": f'Bearer {TOKEN}'
            }
            data = {
                "user":
                {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email
                }
            }
            response = requests.post(url=FLIGHT_USERS_ENDPOINT,
                                     headers=sheety_header, json=data)
            print(response.text)
        else:
            print("Email not verified")

    def get_customer_emails(self):
        response = requests.get(
            url=FLIGHT_USERS_ENDPOINT, headers=sheety_header)
        self.user_data = response.json()["users"]
        return self.user_data
