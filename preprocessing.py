import pandas as pd
import os

DATA_DIR = "E:/stock_data"

def preprocess_symbol_updated(symbol):
    # Create a list to store dataframes
    dfs = []

    # Load technical indicators data
    tech_indicators = ["ADX", "AROON", "BBANDS", "CCI", "EMA", "MACD", "RSI", "SMA", "STOCH", "VWAP"]
    tech_indicators_multiple_periods = ["ADX", "BBANDS", "EMA", "RSI", "SMA"]
    
    for indicator in tech_indicators:
        if indicator in tech_indicators_multiple_periods:
            for period in [7, 14, 21, 28]:
                file_path = os.path.join(DATA_DIR, "technical_indicators", indicator, symbol, f"period_{period}", f"{symbol}_{indicator.lower()}_period_{period}.csv")
                if os.path.exists(file_path):
                    df = pd.read_csv(file_path)
                    # Rename columns to include the period, except for the 'date' column
                    df.columns = [f"{col}_{period}" if col not in ['Date', 'time', 'timestamp', 'latestDay'] else col for col in df.columns]
                    dfs.append(df)
        else:
            file_path = os.path.join(DATA_DIR, "technical_indicators", indicator, symbol, f"{symbol}_{indicator}.csv")
            if os.path.exists(file_path):
                dfs.append(pd.read_csv(file_path))

    # Load time series data
    time_series_types = ["TIME_SERIES_DAILY_ADJUSTED", "GLOBAL_QUOTE"]
    for ts_type in time_series_types:
        file_path = os.path.join(DATA_DIR, "timeSeries", ts_type, symbol, f"{symbol}_{ts_type}.csv")
        if os.path.exists(file_path):
            dfs.append(pd.read_csv(file_path))

    # Check and rename date columns
    for df in dfs:
        if 'Date' in df.columns:
            df.rename(columns={'Date': 'date'}, inplace=True)
        elif 'time' in df.columns:
            df.rename(columns={'time': 'date'}, inplace=True)
        elif 'timestamp' in df.columns:
            df.rename(columns={'timestamp': 'date'}, inplace=True)
        elif 'latestDay' in df.columns:
            df.rename(columns={'latestDay': 'date'}, inplace=True)

    # Merge all dataframes on date
    if dfs:
        df_merged = dfs[0]
        for df in dfs[1:]:
            df_merged = pd.merge(df_merged, df, on="date", how="outer")
        return df_merged
    else:
        print(f"No data found for symbol: {symbol}")
        return None

# Test with AAPL
symbol = "AAPL"
test_df = preprocess_symbol_updated(symbol)
test_df.head()

