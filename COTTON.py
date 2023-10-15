import requests
import os
import time

WAIT_TIME = 60 / 140
API_KEY = os.environ.get('YOUR_API_KEY')
BASE_URL = "https://www.alphavantage.co/query"
DATA_DIRECTORY = "e:/stock_data/commodities"

def fetch_data(FUNCTION, INTERVALS):
    os.makedirs(os.path.join(DATA_DIRECTORY, FUNCTION), exist_ok=True)
    for interval in INTERVALS:
        response = requests.get(BASE_URL, params={
            "function": FUNCTION,
            "interval": interval,
            "apikey": API_KEY,
            "datatype": "csv"
        })
        time.sleep(WAIT_TIME)
        file_path = os.path.join(DATA_DIRECTORY, FUNCTION, f"{interval}.csv")
        with open(file_path, "w", newline='') as f:
            f.write(response.text)
    print(f"{FUNCTION} data collection complete!")

if __name__ == "__main__":
    FUNCTION = "COTTON"
    INTERVALS = ["daily", "weekly", "monthly"]
    fetch_data(FUNCTION, INTERVALS)
