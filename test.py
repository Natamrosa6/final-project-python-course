from User import User
from Supermarket import Supermarket
from Product import Product
from ProyectoControlPrecios import add_price_to_product, show_sorted_prices, plot_price_comparison


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

def test_plot_price_comparison():
    # Definimos las variables importantes para el plot
    product_name = "Rice"
    test_supermarkets = []

    # Rellenamos los objetos necesarios para el test
    test_product1 = Product(name=product_name)
    test_product1.add_price(2.50, "2024-01-01")
    test_product1.add_price(3.50, "2024-02-01")
    test_product2 = Product(name=product_name)
    test_product2.add_price(2, "2024-01-01")
    test_product2.add_price(3.75, "2024-02-01")
    test_product2.add_price(5.75, "2023-02-01")
    test_supermarket1 = create_supermarket("Mercadona", "Nou de la Rambla 180")
    test_supermarket1.add_product(test_product1)
    test_supermarket2 = create_supermarket("Lidl", "Bailén")
    test_supermarket2.add_product(test_product2)
    test_supermarkets.append(test_supermarket1)
    test_supermarkets.append(test_supermarket2)
    print(test_supermarkets)

    # Ploteamos
    plot_price_comparison(test_supermarkets, product_name)

test_user_object_creation()
test_product1, test_product2  = test_Product_object_creation() 
test_Supermarket1 = test_Supermarket_object_creation()
test_add_price_to_product(test_product1)
test_supermarket_add_product(test_product1, test_Supermarket1)
test_product1.plot_price_history()
test_plot_price_comparison()