class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

products = [
    Product(1, 'Collar', 20, 100),
    Product(2, 'Pulsera', 10, 150),
    Product(3, 'Anillo', 5, 200)
]
