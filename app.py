from flask import Flask, render_template, jsonify, request
import yfinance as yf
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

app = Flask(__name__)
sentiment_analysis = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


BASE_URL = "https://finance.yahoo.com/quote/"

def get_news(ticker):
    url = BASE_URL + ticker
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    headlines = []
    for item in soup.find_all('h3', class_='Mb(5px)'):
        text = item.get_text()
        link = item.a['href']
        headlines.append((text, link))
    return headlines

def analyze_sentiment(news):
    return [sentiment_analysis(item[0]) for item in news]

@app.route('/stock_data', methods=['POST'])
def stock_data():
    ticker = request.form.get('ticker', 'AAPL')
    data = yf.Ticker(ticker).history(period="1mo")
    
    data.index = data.index.strftime('%Y-%m-%d')
    
    news = get_news(ticker)
    sentiment = analyze_sentiment(news)
    
    return jsonify({"stock_data": data.to_dict(), "sentiment": sentiment})


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



