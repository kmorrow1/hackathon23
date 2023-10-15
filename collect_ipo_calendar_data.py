import os
import requests
import csv
import time

WAIT_TIME = 60 / 140
def main():
    # Define symbols
    symbols = [
    "TSLA", "PLTR", "AMD", "BAC", "AAL", "NVDA", "F", "AAPL", "AMZN", "PLUG", "SWN", 
    "C", "JPM", "T", "RIVN", "UBER", "NIO", "XOM", "CCL", "JD", "WFC", "PFE", "SNAP", 
    "GOOGL", "GRAB", "PBR", "SOFI", "GOLD", "BBD", "VZ", "NEE", "WBA", "META", "INTC", 
    "SIRI", "KGC", "LCID", "GOOG", "NOK", "HBAN", "MSFT", "AGNC", "NCLH", "GM", "KEY", 
    "NU", "VALE", "KO", "CSCO", "GGB"
]

    base_url = 'https://www.alphavantage.co/query?'
    data_directory = "e:/stock_data"
    CSV_URL = f"{base_url}function=IPO_CALENDAR&apikey={os.environ.get('YOUR_API_KEY')}"

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)

        with open(os.path.join(data_directory, "fundamental_data", "IPO_CALENDAR.csv"), "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(my_list)
        time.sleep(WAIT_TIME)
    print("IPO Calendar data collection complete!")

if __name__ == "__main__":
    main()
