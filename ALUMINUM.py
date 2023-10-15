import requests
import os
import time

WAIT_TIME = 60 / 140
API_KEY = os.environ.get('YOUR_API_KEY')
BASE_URL = "https://www.alphavantage.co/query"
FUNCTION = "ALUMINUM"
INTERVALS = ["monthly", "quarterly", "annual"]
DATA_DIRECTORY = "e:/stock_data/commodities/ALUMINUM"

os.makedirs(DATA_DIRECTORY, exist_ok=True)

def fetch_aluminum(interval):
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
        fetch_aluminum(interval)
    print("ALUMINUM data collection complete!")

if __name__ == "__main__":
    main()
