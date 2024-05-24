from User import User
from Supermarket import Supermarket
from Product import Product
from ProyectoControlPrecios import add_price_to_product, show_sorted_prices, plot_price_comparison, plot_price_history


def test_user_object_creation():
    User1 = User('Juan')
    print(User1)


#Crear supermercado
def create_supermarket(name, address):
    return Supermarket(name, address)

def test_Supermarket_object_creation():
    Supermarket1 = create_supermarket("Mercadona", "Nou de la Rambla 180")  
    print(Supermarket1)
    return Supermarket1


#Crear producto

def create_product(name, description):
    return Product(name, description)

def test_Product_object_creation():
    product1 = create_product("Rice", "white rice") 
    product2 = create_product("Milk", "milk desnatada") 
    print(product1)
    return product1, product2
    


# Agregar precios al producto

def test_add_price_to_product(product):
    add_price_to_product(product, 2.50, "2024-01-01")
    add_price_to_product(product, 3.75, "2024-02-01")
    print(f"Sorted prices for {product.name}:")
    show_sorted_prices(product) 

#Agregar productos a los superm
def test_supermarket_add_product(product, supermarket):
    supermarket.add_product(product) 

test_user_object_creation()
test_product1, test_product2  = test_Product_object_creation() 
test_Supermarket1 = test_Supermarket_object_creation()
test_add_price_to_product(test_product1)
test_supermarket_add_product(test_product1, test_Supermarket1)
plot_price_history(test_product1)
plot_price_comparison(test_product1)
