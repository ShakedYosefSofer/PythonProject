from LogisticsEmployee import LogisticsEmployee
from Product import Product
from Supermarket import Supermarket

class Stocker(LogisticsEmployee):
    def __init__(self, id: str, name: str, age: int, phone: str, employee_number: str, vest_color: str):
        super().__init__(id, name, age, phone, employee_number)
        self.vest_color = vest_color

    def add_product_to_shelf(self, product: Product, supermarket: Supermarket):
        """Add a product to the supermarket shelf."""
        if product not in supermarket.get_products():
            supermarket.add_product(product)
            print(f"Product {product.name} added to the shelf.")
        else:
            print(f"Product {product.name} is already on the shelf.")

    def remove_product_from_shelf(self, product: Product, supermarket: Supermarket):
        """Remove a product from the supermarket shelf."""
        if product in supermarket.get_products():
            supermarket.remove_product(product)
            print(f"Product {product.name} removed from the shelf.")
        else:
            print(f"Product {product.name} is not on the shelf.")


