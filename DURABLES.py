import requests
import os
import time

WAIT_TIME = 60 / 140
API_KEY = os.environ.get('YOUR_API_KEY')
BASE_URL = "https://www.alphavantage.co/query"
FUNCTION = "DURABLES"
DATA_TYPE = "csv"

def fetch_durables():
    params = {
        "function": FUNCTION,
        "datatype": DATA_TYPE,
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    time.sleep(WAIT_TIME)
    file_name = f"E:/stock_data/economic_indicators/{FUNCTION}/{FUNCTION}.csv"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)

    with open(file_name, "wb") as file:
        file.write(response.content)

def main():
    fetch_durables()

if __name__ == "__main__":
    main()
