import requests
import os
import time

WAIT_TIME = 60 / 140
API_KEY = os.environ.get('YOUR_API_KEY')
BASE_URL = "https://www.alphavantage.co/query"
FUNCTION = "TOP_GAINERS_LOSERS"
DATA_DIRECTORY = "E:/stock_data/alpha_intelligence/top_gainers_losers"

def fetch_top_gainers_losers():
    params = {
        "function": FUNCTION,
        "apikey": API_KEY,
        "datatype": "csv"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching top gainers, losers, and most actively traded tickers. Status code: {response.status_code}")
        return None

def save_data(data):
    os.makedirs(DATA_DIRECTORY, exist_ok=True)
    file_name = "top_gainers_losers.csv"
    with open(os.path.join(DATA_DIRECTORY, file_name), 'w') as f:
        f.write(data)

if __name__ == "__main__":
    print("Fetching top gainers, losers, and most actively traded tickers...")
    data = fetch_top_gainers_losers()
    if data:
        save_data(data)
        print("Top gainers, losers, and most actively traded tickers data saved successfully!")
    else:
        print("Failed to fetch data.")
    time.sleep(WAIT_TIME)
    print("Data fetching completed.")
