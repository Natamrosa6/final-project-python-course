class Supermarket:
    def __init__(self, name, location = None): #wip location is temporary none by default for testing
        self.name = name
        self.location = location
        self.product = []

    def add_product(self, product):
        self.product.append(product)

    def get_product_by_name(self, product_name):
        for product in self.product:
            if product_name == product_name:
                return product
            return None
        
    def __str__(self):
        return f"Supermarket: {self.name}, Location: {self.location}"
    
    