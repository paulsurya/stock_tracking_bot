import time
import yfinance as yf

def track_stock(ticker:str):
    stock = yf.Ticker(ticker)
    while True:
        try:
            info = stock.info
            current_price = info.get("currentPrice", "Price not available")
            print(f"Current {ticker} Price: {current_price}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(20)  # Pause for 1 minute

# Call the function
track_stock("ACEL")