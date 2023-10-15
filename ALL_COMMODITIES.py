import requests
import os
import time

WAIT_TIME = 60 / 140
API_KEY = os.environ.get('YOUR_API_KEY')
BASE_URL = "https://www.alphavantage.co/query"
FUNCTION = "ALL_COMMODITIES"
INTERVALS = ["monthly", "quarterly", "annual"]
DATA_DIRECTORY = "e:/stock_data/commodities/ALL_COMMODITIES"


os.makedirs(DATA_DIRECTORY, exist_ok=True)

def fetch_all_commodities(interval):
    response = requests.get(BASE_URL, params={
        "function": FUNCTION,
        "interval": interval,
        "apikey": API_KEY,
        "datatype": "csv"
    })
    time.sleep(WAIT_TIME)
    file_path = os.path.join(DATA_DIRECTORY, f"{interval}.csv")
    with open(file_path, "w", newline='') as f:
        f.write(response.text)

    
    
def main():
    for interval in INTERVALS:
        fetch_all_commodities(interval)
    print("ALL_COMMODITIES data collection complete!")

if __name__ == "__main__":
    main()
