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

def plot_price_comparison(list_supermarkets, product_name):
        supermarket_names = []
        product_prices = []

        for supermarket in list_supermarkets:
                supermarket_names.append(supermarket.get_name())
                found_product = supermarket.get_product_by_name(product_name)
                current_price_found_product = found_product.get_current_price()
                product_prices.append(current_price_found_product['amount'])

        plt.figure(figsize=(10,5))
        #plt.bar(list(range(len(supermarket_names))), product_prices, data=supermarket_names)
        plt.bar(supermarket_names, product_prices)
        plt.title('Price Comparison by Supermarket')
        plt.xlabel('Supermarket')
        plt.ylabel(f'{product_name} Price')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()