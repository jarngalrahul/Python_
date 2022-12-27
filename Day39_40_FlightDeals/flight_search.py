import requests
import os
from flight_data import FlightData
KIWI_FLIGHT_API_KEY = os.environ.get("KIWI_FLIGHT_API_KEY")
URL_ENDPOINT = "https://api.tequila.kiwi.com"

# AFFIL_ID = "pythontesting1922flightapp"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    flight_search_header = {"apikey": KIWI_FLIGHT_API_KEY}

    def __init__(self) -> None:
        self.flight_price_data = {}

    def get_destination_code(self, city_name):
        query = {"term": city_name}
        response = requests.get(url=f"{URL_ENDPOINT}/locations/query",
                                headers=FlightSearch.flight_search_header,
                                params=query)
        data = response.json()["locations"]
        city_code = data[0]["code"]
        return city_code

    def check_flights(self, origin_city_code, dest_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": dest_code,
            "date_from": from_time.strftime(f'%d/%m/%Y'),
            "date_to": to_time.strftime(f'%d/%m/%Y'),
            "one_for_city": 1,
            "max_stopovers": 0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{URL_ENDPOINT}/search",
            headers=FlightSearch.flight_search_header,
            params=query
        )

        try:
            result = response.json()
            data = result["data"][0]
        except IndexError:
            print(f"No flights found from {origin_city_code} to {dest_code}")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["dTimeUTC"],
                return_date=data["route"][1]["dTimeUTC"]
            )
            return flight_data
