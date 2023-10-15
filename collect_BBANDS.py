import requests
import os
import time

WAIT_TIME = 61 / 150
# Constants
BASE_URL = "https://www.alphavantage.co/query"
API_KEY = os.environ.get('YOUR_API_KEY')
FUNCTION = "BBANDS"
SAVE_PATH = "E:/stock_data/technical_indicators/BBANDS"
PERIODS = [7, 14, 21, 28]  # Common periods for Bollinger Bands

# Define symbols
symbols = [
    "TSLA", "PLTR", "AMD", "BAC", "AAL", "NVDA", "F", "AAPL", "AMZN", "PLUG", "SWN", 
    "C", "JPM", "T", "RIVN", "UBER", "NIO", "XOM", "CCL", "JD", "WFC", "PFE", "SNAP", 
    "GOOGL", "GRAB", "PBR", "SOFI", "GOLD", "BBD", "VZ", "NEE", "WBA", "META", "INTC", 
    "SIRI", "KGC", "LCID", "GOOG", "NOK", "HBAN", "MSFT", "AGNC", "NCLH", "GM", "KEY", 
    "NU", "VALE", "KO", "CSCO", "GGB"
]

def fetch_bbands_data(symbol, period):
    # Define the parameters
    params = {
        "function": FUNCTION,
        "symbol": symbol,
        "interval": "daily",
        "time_period": str(period),
        "series_type": "close",
        "apikey": API_KEY,
        "datatype": "csv"
    }

    # Fetch the data
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching data for {symbol} with period {period}. Status code: {response.status_code}")
        return None

def save_data(symbol, period, data):
    """Saves fetched data to the appropriate location"""
    symbol_dir = os.path.join(SAVE_PATH, symbol, f"period_{period}")
    if not os.path.exists(symbol_dir):
        os.makedirs(symbol_dir)
    
    file_path = os.path.join(symbol_dir, f"{symbol}_bbands_period_{period}.csv")
    with open(file_path, 'w') as f:
        f.write(data)

if __name__ == "__main__":
    for symbol in symbols:
        for period in PERIODS:
            print(f"Fetching BBANDS data for {symbol} with period {period}...")
            data = fetch_bbands_data(symbol, period)
            if data:
                save_data(symbol, period, data)
                print(f"Data for {symbol} with period {period} saved successfully!")
            else:
                print(f"Failed to fetch data for {symbol} with period {period}.")
            time.sleep(WAIT_TIME)

    print("BBANDS data fetching completed.")
