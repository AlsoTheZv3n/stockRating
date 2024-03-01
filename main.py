import requests


def get_stock_data(symbol, api_key):
    base_url = "https://www.alphavantage.co/query"
    function = "TIME_SERIES_DAILY"

    # Define parameters for the API request
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    except Exception as e:
        print("Error fetching data:", e)
        return None


def evaluate_stock(stock_data):
    # Check if data is available
    if "Time Series (Daily)" not in stock_data:
        print("Data not available for this stock.")
        return False

    # Get the latest two closing prices
    time_series = stock_data["Time Series (Daily)"]
    dates = list(time_series.keys())[:2]
    latest_close = float(time_series[dates[0]]["4. close"])
    prev_close = float(time_series[dates[1]]["4. close"])

    # Calculate percentage change
    pct_change = ((latest_close - prev_close) / prev_close) * 100

    print("Latest Close Price:", latest_close)
    print("Previous Close Price:", prev_close)
    print("Percentage Change:", pct_change)

    # Evaluate based on percentage change
    if pct_change > 5:
        print("Buy! The stock price increased by more than 5%.")
        return True
    else:
        print("Don't Buy. The stock price change is not significant.")
        return False


def main():
    # Get user input for stock symbol
    symbol = input("Enter the stock symbol (e.g., AAPL): ").upper()

    # Alpha Vantage API key
    api_key = "YOUR_API_KEY_HERE"

    # Get stock data
    stock_data = get_stock_data(symbol, api_key)

    if stock_data is not None:
        # Evaluate the stock
        evaluate_stock(stock_data)
    else:
        print("Unable to fetch data. Please try again later.")


if __name__ == "__main__":
    main()
