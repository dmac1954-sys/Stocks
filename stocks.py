import requests
import json
class Stocks:
    def __init__(self, open_price, close_price, symbol, date):
        self.open_price = open_price
        self.close_price = close_price
        self.symbol = symbol
        self.date = date

    @property
    def change(self):
        return self.close_price - self.open_price

