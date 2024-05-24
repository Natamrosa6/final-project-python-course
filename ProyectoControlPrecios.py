import matplotlib.pyplot as plt

from Product import Product
from Supermarket import Supermarket

def create_supermarket(name, location):
        return Supermarket(name, location)

def create_product(name, description=""):
        return Product(name, description)

def add_price_to_product(product, amount, date):
        product.add_price(amount, date)

def show_sorted_prices(product):
        sorted_prices = product.get_sorted_prices()
        for price in sorted_prices:
                print(f"Date: {price['date']}, Price: {price['amount']}")

def get_price_history(product):
        dates = [price['date'] for price in product.prices]
        amounts = [price['amount'] for price in product.prices]
        return dates, amounts


def plot_price_history(product):
        dates, amounts = get_price_history(product)
        plt.figure(figsize=(10,5))
        plt.plot(dates, amounts, marker='o')
        plt.title(f'Price History for {product.name}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.grid(True)
        plt.show()

def plot_price_comparison(products):
        supermarket_names = [product.name for product in products]
        #lowest_prices = [min(product.prices, key= lambda x: x['amount'])['amount'] for product in products]

        plt.figure(figsize=(10,5))
        plt.bar(supermarket_names, lowest_prices)
        plt.title('Price Comparison by Supermarket')
        plt.xlabel('Supermarket')
        plt.ylabel('Lowest Price')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

