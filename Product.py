import uuid

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