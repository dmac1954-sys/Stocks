import requests
import json
from datetime import datetime
from stocks import Stocks
from portfolio import Portfolio
from position import Position

url = "http://api.marketstack.com/v1/eod/latest"
params = {"access_key": "357ad00c4bbbcc5fcd571e94411b46b8", "symbols": "AAPL,AMZN,GOOG"}

response = requests.get(url, params=params)

customer_name = input("Enter customer name: ")
google_shares = int(input("How many Google shares do you own? "))
apple_shares = int(input("How many Apple shares do you own? "))
amazon_shares = int(input("How many Amazon shares do you own? "))

if response.status_code == 200:
    data = response.json()
    stocks = []
    for stock_data in data["data"]:
        date = datetime.strptime(stock_data["date"], "%Y-%m-%dT%H:%M:%S%z").strftime(
            "%Y-%m-%d"
        )
        stock = Stocks(
            stock_data["open"], stock_data["close"], stock_data["symbol"], date
        )
        stocks.append(stock)

    p1 = Portfolio(customer_name)
    p1.add_position(Position("GOOG", google_shares))
    p1.add_position(Position("AAPL", apple_shares))
    p1.add_position(Position("AMZN", amazon_shares))

    p1.calculate_profit_loss(stocks)

else:
    print("Failed to retrieve data. Error:", response.status_code)
