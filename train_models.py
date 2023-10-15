import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

SYMBOLS = [
    "TSLA", "PLTR", "AMD", "BAC", "AAL", "NVDA", "F", "AAPL", "AMZN", "PLUG", "SWN", 
    "C", "JPM", "T", "RIVN", "UBER", "NIO", "XOM", "CCL", "JD", "WFC", "PFE", "SNAP", 
    "GOOGL", "GRAB", "PBR", "SOFI", "GOLD", "BBD", "VZ", "NEE", "WBA", "META", "INTC", 
    "SIRI", "KGC", "LCID", "GOOG", "NOK", "HBAN", "MSFT", "AGNC", "NCLH", "GM", "KEY", 
    "NU", "VALE", "KO", "CSCO", "GGB"
]
def train_model():
    for symbol in SYMBOLS:
        data = preprocessing.preprocess_symbol_updated(symbol)  # Make sure to use the updated preprocessing function
        if data is not None:
            print(f"Columns for {symbol}: {data.columns}")  # Print columns to debug
            target_column = "close" if "close" in data.columns else "Close" if "Close" in data.columns else None
            if target_column:
                X = data.drop(columns=[target_column])
                y = data[target_column]

                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                model = RandomForestRegressor()
                model.fit(X_train, y_train)

                # Evaluate the model (this is just a placeholder, you can replace with your evaluation method)
                score = model.score(X_test, y_test)
                print(f"{symbol}: Model Score: {score}")
            else:
                print(f"No 'close' or 'Close' column found for {symbol}.")

if __name__ == "__main__":
    train_model()
