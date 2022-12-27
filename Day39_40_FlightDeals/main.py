# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

import os
import requests
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager


CURRENT_DEST_CODE = "LON"


def main():
    sheet_data = data_manager.get_destination_data()
    flight_search = FlightSearch()

    if sheet_data[0]["iataCode"] == "":
        flight_search = FlightSearch()
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
        print(f"sheet_data:\n{sheet_data}")

        data_manager.destination_data = sheet_data
        data_manager.update_destination_code()

    tommorow = datetime.now()+timedelta(days=1)
    after_six_months = tommorow+timedelta(days=180)
    for city in sheet_data:
        flight = flight_search.check_flights(
            origin_city_code=CURRENT_DEST_CODE,
            dest_code=city["iataCode"],
            from_time=tommorow,
            to_time=after_six_months
        )
        if flight is None:
            continue
        if flight.price < city["lowestPrice"]:
            users = data_manager.get_customer_emails()
            emails = [row["email"] for row in users]
            names = [row["firstName"] for row in users]
            msg = f"Low price alert!! Only {flight.price} to fly form {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
            notification_manager.send_mails(names, emails, msg)


if __name__ == "__main__":
    data_manager = DataManager()
    notification_manager = NotificationManager()
    enter_user = True
    while enter_user:
        if input("Do you want to enter into flight club (y/n)") == 'y':
            data_manager.get_user_data()
        else:
            enter_user = False
    main()
