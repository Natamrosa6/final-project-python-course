import uuid
import matplotlib.pyplot as plt

class Product: 
    def __init__(self, name ="", description =""):
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.prices = []

    def add_price(self, amount, date):
        self.prices.append({'amount':amount, 'date':date})

    def get_sorted_prices(self):
        return sorted(self.prices, key=lambda x: x['amount']) 
    
    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, description: {self.description}, price: {self.prices}'
    
    def get_price_history(self):
        date = []
        amounts = []
        for price in self.prices:
                date.append(price['date'])
                amounts.append(price['amount'])
        return date, amounts

    def get_current_price(self):
        order_prices_by_date = sorted(self.prices, key=lambda x: x['date'])
        return order_prices_by_date[-1]

    def plot_price_history(self):
        dates, amounts = self.get_price_history()
        plt.figure(figsize=(10,5))
        plt.plot(dates, amounts, marker='o')
        plt.title(f'Price History for {self.name}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.grid(True)
        plt.show()