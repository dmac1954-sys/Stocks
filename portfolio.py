from stocks import Stocks

class Portfolio:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.positions = []

    def add_position(self, position):
        self.positions.append(position)

    def calculate_profit_loss(self, stocks):
        total_profit_loss = 0
        for position in self.positions:
            for stock in stocks:
                if stock.symbol == position.symbol:
                    profit_loss = (stock.close_price - stock.open_price) * position.quantity
                    total_profit_loss += profit_loss
                    print(f"{position.symbol}: {profit_loss:.2f}")
        if total_profit_loss < 0:
            print(f"On the last day the market was open ({stocks[-1].date}), your portfolio, {self.customer_name}, lost ${total_profit_loss:.2f} USD")
        else:
            print(f"On the last day the market was open ({stocks[-1].date}), your portfolio, {self.customer_name}, gained ${total_profit_loss:.2f} USD")