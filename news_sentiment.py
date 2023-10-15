import requests
import os
import time

WAIT_TIME = 60 / 140
API_KEY = os.environ.get('YOUR_API_KEY')
BASE_URL = "https://www.alphavantage.co/query"
FUNCTION = "NEWS_SENTIMENT"
DATA_DIRECTORY = "E:/stock_data/alpha_intelligence/news_sentiment"
symbols = [
    "TSLA", "PLTR", "AMD", "BAC", "AAL", "NVDA", "F", "AAPL", "AMZN", "PLUG", "SWN",
    "C", "JPM", "T", "RIVN", "UBER", "NIO", "XOM", "CCL", "JD", "WFC", "PFE", "SNAP",
    "GOOGL", "GRAB", "PBR", "SOFI", "GOLD", "BBD", "VZ", "NEE", "WBA", "META", "INTC",
    "SIRI", "KGC", "LCID", "GOOG", "NOK", "HBAN", "MSFT", "AGNC", "NCLH", "GM", "KEY",
    "NU", "VALE", "KO", "CSCO", "GGB"
]
topics = [
    "blockchain", "earnings", "ipo", "mergers_and_acquisitions",
    "financial_markets", "economy_fiscal", "economy_monetary",
    "economy_macro", "energy_transportation", "finance",
    "life_sciences", "manufacturing", "real_estate",
    "retail_wholesale", "technology"
]

def fetch_news_sentiment(symbol, topic=None):
    params = {
        "function": FUNCTION,
        "tickers": symbol,
        "apikey": API_KEY,
        "datatype": "csv"
    }
    if topic:
        params["topics"] = topic

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching data for {symbol} with topic {topic}. Status code: {response.status_code}")
        return None

def save_data(symbol, data, topic=None):
    topic_dir = topic if topic else "all_topics"
    path = os.path.join(DATA_DIRECTORY, topic_dir, symbol)
    os.makedirs(path, exist_ok=True)
    file_name = f"{symbol}_news_sentiment.csv" if not topic else f"{symbol}_{topic}_news_sentiment.csv"
    with open(os.path.join(path, file_name), 'w') as f:
        f.write(data)

if __name__ == "__main__":
    for symbol in symbols:
        for topic in topics:
            print(f"Fetching news sentiment data for {symbol} with topic {topic}...")
            data = fetch_news_sentiment(symbol, topic)
            if data:
                save_data(symbol, data, topic)
                print(f"Data for {symbol} with topic {topic} saved successfully!")
            else:
                print(f"Failed to fetch data for {symbol} with topic {topic}.")
            time.sleep(WAIT_TIME)
        print(f"Fetching combined news sentiment data for {symbol}...")
        combined_data = fetch_news_sentiment(symbol)
        if combined_data:
            save_data(symbol, combined_data)
            print(f"Combined data for {symbol} saved successfully!")
        else:
            print(f"Failed to fetch combined data for {symbol}.")
        time.sleep(WAIT_TIME)
    print("News sentiment data fetching completed.")
