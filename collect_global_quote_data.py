import os
import requests
import csv
import time

WAIT_TIME = 60 / 140
def main():
    symbols = [
    "TSLA", "PLTR", "AMD", "BAC", "AAL", "NVDA", "F", "AAPL", "AMZN", "PLUG", "SWN", 
    "C", "JPM", "T", "RIVN", "UBER", "NIO", "XOM", "CCL", "JD", "WFC", "PFE", "SNAP", 
    "GOOGL", "GRAB", "PBR", "SOFI", "GOLD", "BBD", "VZ", "NEE", "WBA", "META", "INTC", 
    "SIRI", "KGC", "LCID", "GOOG", "NOK", "HBAN", "MSFT", "AGNC", "NCLH", "GM", "KEY", 
    "NU", "VALE", "KO", "CSCO", "GGB"
]
    base_url = 'https://www.alphavantage.co/query?'
    data_directory = "e:/stock_data"
    function_directory = os.path.join(data_directory, "timeSeries", "GLOBAL_QUOTE")

    for symbol in symbols:
        symbol_directory = os.path.join(function_directory, symbol)
        
        # Ensure directory exists
        if not os.path.exists(symbol_directory):
            os.makedirs(symbol_directory)

        api_url = f"{base_url}function=GLOBAL_QUOTE&symbol={symbol}&apikey={os.environ.get('YOUR_API_KEY')}&datatype=csv"
        response = requests.get(api_url)
        time.sleep(WAIT_TIME)
        with open(os.path.join(symbol_directory, f"{symbol}_GLOBAL_QUOTE.csv"), 'wb') as file:
            file.write(response.content)

    print("Quote endpoint data collection complete!")

if __name__ == "__main__":
    main()


