from abc import ABC
from Employee import Employee
from Product import Product
from Supermarket import Supermarket

class LogisticsEmployee(Employee, ABC):
    def add_product_to_shelf(self, product: Product, supermarket: Supermarket):
        """Add a product to the supermarket shelf."""
        try:
            if product not in supermarket.get_products():
                supermarket.add_product(product)
                print(f"Product {product.name} added to the shelf.")
            else:
                print(f"Product {product.name} is already on the shelf.")
        except Exception as e:
            print(f"Failed to add product to shelf: {e}")

    def remove_product_from_shelf(self, product: Product, supermarket: Supermarket):
        """Remove a product from the supermarket shelf."""
        try:
            if product in supermarket.get_products():
                supermarket.remove_product(product)
                print(f"Product {product.name} removed from the shelf.")
            else:
                print(f"Product {product.name} is not on the shelf.")
        except Exception as e:
            print(f"Failed to remove product from shelf: {e}")
