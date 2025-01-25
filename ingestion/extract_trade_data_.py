import requests
import pandas as pd
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
load_dotenv()
api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
raw_data_path = "data/raw"
processed_data_path = "data/processed"


def extract_trade_data(symbol="IBM", interval="15min"):
    """
    Extract trade data from Alpha Vantage API.

    Parameters:
    symbol (str): Stock symbol.
    interval (str): Time interval for the trade data.
    """
    url_Time_Series_Intraday_URL = (
        "https://www.alphavantage.co/query?"
        f"function=TIME_SERIES_INTRADAY&"
        f"symbol={symbol}&"
        f"interval={interval}&"
        f"apikey={api_key}"
    )
    logging.info("Sending request to Alpha Vantage API")
    logging.info(f"Extracting data from: {url_Time_Series_Intraday_URL}")
    response = requests.get(url_Time_Series_Intraday_URL)

    if response.status_code != 200:
        logging.error(f"Failed to fetch data from {url_Time_Series_Intraday_URL}")
        return None
    data = response.json()

    if not data:
        logging.error("No data found")
        return None

    time_series = data[f"Time Series ({interval})"]

    df = pd.DataFrame(time_series).T
    df.reset_index(inplace=True)
    df.rename(columns={"index": "timestamp"}, inplace=True)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")
    df["symbol"] = symbol
    return df


def process_trade_data(df):
    """
    Process the extracted trade data.

    Parameters:
    df (pd.DataFrame): DataFrame containing the extracted trade data.
    """
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")
    
    # Map Alpha Vantage column names to standard names
    column_mapping = {
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume"
    }
    df.rename(columns=column_mapping, inplace=True)
    
    numeric_columns = ["open", "high", "low", "close", "volume"]
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")
    return df


def save_raw_data(df, path, symbol):
    """
    Save raw data to CSV file.

    Parameters:
    df (pd.DataFrame): DataFrame containing the raw data.
    path (str): Path to save the raw data.
    symbol (str): Stock symbol.
    """
    timestamp = pd.Timestamp.now().strftime("%Y%m%d%H%M%S")
    file_path = f"{path}/{symbol}_raw_{timestamp}.csv"
    df.to_csv(file_path, index=False)
    logging.info(f"Raw data saved to {file_path}")
    return file_path


def main():
    # df = extract_trade_data()
    symbols = ["IBM", "AAPL", "MSFT"]
    for symbol in symbols:
        df = extract_trade_data(symbol=symbol)
        if df is not None:
            logging.info("Previewing the extracted data")
            logging.info(df.head())
            logging.info("-" * 80)
            df = process_trade_data(df)
            logging.info("-" * 80)
            raw_data_file = save_raw_data(df, raw_data_path, symbol)
            # logging.info(f"Raw data saved to {raw_data_file}")


# Call the main function
if __name__ == "__main__":
    main()
