import os
import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def main():
    stock_params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY
    }
    r = requests.get(url="https://www.alphavantage.co/query",
                     params=stock_params)
    stock_data = r.json()['Time Series (Daily)']
    data_list = [value for (key, value) in stock_data.items()]
    yesterday_data = data_list[0]
    cp_yest = float(yesterday_data['4. close'])
    day_before_yesterday_data = data_list[1]
    cp_day_before_yest = float(day_before_yesterday_data['4. close'])
    gains = round(abs((1-cp_day_before_yest/cp_yest)*100))
    if gains > 1:
        news_params = {
            "q": STOCK,
            "apikey": NEWS_API_KEY,
        }
        results = requests.get(url=NEWS_ENDPOINT, params=news_params)
        results.raise_for_status()
        data = results.json()['articles'][:3]
        formatted_msg = [
            f"Title: {entry['title']}\nDescription: {entry['description']}" for entry in data]
        for msg in formatted_msg:
            print("\n\n", msg)
            # we could use twilio to send msg if the service is available in your country


if __name__ == "__main__":
    main()
