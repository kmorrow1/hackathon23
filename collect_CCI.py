import os
import requests
import time

WAIT_TIME = 10 / 140
# Constants
BASE_URL = "https://www.alphavantage.co/query"
API_KEY = os.environ.get('YOUR_API_KEY')
FUNCTION = "CCI"
SAVE_PATH = "E:/stock_data/technical_indicators/CCI"

# Define symbols
symbols = [
    "TSLA", "PLTR", "AMD", "BAC", "AAL", "NVDA", "F", "AAPL", "AMZN", "PLUG", "SWN", 
    "C", "JPM", "T", "RIVN", "UBER", "NIO", "XOM", "CCL", "JD", "WFC", "PFE", "SNAP", 
    "GOOGL", "GRAB", "PBR", "SOFI", "GOLD", "BBD", "VZ", "NEE", "WBA", "META", "INTC", 
    "SIRI", "KGC", "LCID", "GOOG", "NOK", "HBAN", "MSFT", "AGNC", "NCLH", "GM", "KEY", 
    "NU", "VALE", "KO", "CSCO", "GGB"
]

def fetch_data(symbol):
    """Fetches CCI data for a given symbol"""
    parameters = {
        "function": FUNCTION,
        "symbol": symbol,
        "apikey": API_KEY,
        "interval" : "daily",
        "time_period" : "14",
        "datatype": "csv"
    }
    response = requests.get(BASE_URL, params=parameters)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching data for {symbol}. Status code: {response.status_code}")
        return None

def save_data(symbol, data):
    """Saves fetched data to the appropriate location"""
    if not os.path.exists(f"{SAVE_PATH}/{symbol}"):
        os.makedirs(f"{SAVE_PATH}/{symbol}")

    with open(f"{SAVE_PATH}/{symbol}/{symbol}_CCI.csv", 'w') as f:
        f.write(data)

if __name__ == "__main__":
    for symbol in symbols:
        print(f"Fetching CCI data for {symbol}...")
        data = fetch_data(symbol)
        if data:
            save_data(symbol, data)
            print(f"Data for {symbol} saved successfully!")
        else:
            print(f"Failed to fetch data for {symbol}.")
        time.sleep(WAIT_TIME)
    
    print("CCI data fetching completed.")

