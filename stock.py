import yfinance as yf
from datetime import datetime

def get_type(ticker:str):
    stock = yf.Ticker(ticker)
    if (len(ticker) == 6 and ticker.isalpha()):
        return True
    else:
        return False

def format_stock(ticker:str):
    stock = yf.Ticker(ticker)
    formatted_dic = {
        "Name": stock.info['longName'],
        "Purchase Price": stock.info['regularMarketPrice'],
        "Type":"Stock",
        "DOP": datetime.now().strftime("%Y-%m-%d"),
        "Forecast":(stock.info['targetMeanPrice']/stock.info['regularMarketPrice'])*100
    }

    return formatted_dic

def forecast_currency(ticker):
    currency = yf.Ticker(ticker)
    forecast = ((currency.info['regularMarketPrice']-currency.info['fiftyTwoWeekLow'])/(currency.info['fiftyTwoWeekHigh']-currency.info['fiftyTwoWeekLow']))*100

    return forecast

def fromat_currency(ticker):
    currency = yf.Ticker(ticker)
    formatted_dic = {
        "Name": currency.info['shortName'],
        "Purchase Price": currency.info['regularMarcketPrice'],
        "Type": "Currency",
        "DOP": datetime.now().strftime("%Y-%m-%d"),
        "Forecast":forecast_currency(ticker)
    }

    return formatted_dic