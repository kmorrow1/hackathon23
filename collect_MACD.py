import requests
import os
import time

WAIT_TIME = 61 / 150
# Constants
BASE_URL = "https://www.alphavantage.co/query"
API_KEY = os.environ.get('YOUR_API_KEY')
FUNCTION = "MACD"
SAVE_PATH = "E:/stock_data/technical_indicators/MACD"

# Define symbols
symbols = [
    "TSLA", "PLTR", "AMD", "BAC", "AAL", "NVDA", "F", "AAPL", "AMZN", "PLUG", "SWN", 
    "C", "JPM", "T", "RIVN", "UBER", "NIO", "XOM", "CCL", "JD", "WFC", "PFE", "SNAP", 
    "GOOGL", "GRAB", "PBR", "SOFI", "GOLD", "BBD", "VZ", "NEE", "WBA", "META", "INTC", 
    "SIRI", "KGC", "LCID", "GOOG", "NOK", "HBAN", "MSFT", "AGNC", "NCLH", "GM", "KEY", 
    "NU", "VALE", "KO", "CSCO", "GGB"
]

def fetch_macd_data(symbol):
    # Define the parameters
    params = {
        "function": FUNCTION,
        "symbol": symbol,
        "interval": "daily",
        "series_type": "close",
        "apikey": API_KEY,
        "datatype": "csv"
    }

    # Fetch the data
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching data for {symbol}. Status code: {response.status_code}")
        return None

def save_data(symbol, data):
    """Saves fetched data to the appropriate location"""
    symbol_dir = os.path.join(SAVE_PATH, symbol)
    if not os.path.exists(symbol_dir):
        os.makedirs(symbol_dir)
    
    file_path = os.path.join(symbol_dir, f"{symbol}_macd.csv")
    with open(file_path, 'w') as f:
        f.write(data)

if __name__ == "__main__":
    for symbol in symbols:
        print(f"Fetching MACD data for {symbol}...")
        data = fetch_macd_data(symbol)
        if data:
            save_data(symbol, data)
            print(f"Data for {symbol} saved successfully!")
        else:
            print(f"Failed to fetch data for {symbol}.")
        time.sleep(WAIT_TIME)

    print("MACD data fetching completed.")
