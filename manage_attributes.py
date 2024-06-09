# Manage Class Attributes with @property Decorator
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)):
            raise ValueError("Price must be a number")
        if value < 0:
            raise ValueError("Price cannot be negative")


# creating instance of the class
product = Product("Laptop", 300)
print(product.price)