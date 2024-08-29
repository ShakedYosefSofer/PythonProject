from typing import List
from Person import Person
from Product import Product

class Customer(Person):
    def __init__(self, id: str, name: str, age: int, phone: str):
        super().__init__(id, name, age, phone)
        self.shopping_cart: List[Product] = []
        self.purchase_history: List[Product] = []
        self.balance: float = 1000.0  # start money

    def __str__(self) -> str:
        return f"Customer: {self.name} (ID: {self.id})"

    def add_product_to_cart(self, product: Product):
        try:
            if not isinstance(product, Product):
                raise ValueError("Can only add instances of Product")
            self.shopping_cart.append(product)
            print(f"Added {product.name} to {self.name}'s cart.")
        except ValueError as e:
            print(f"Error adding product to cart: {e}")

    def complete_purchase(self, cashier: 'Cashier'):
        try:
            if not self.shopping_cart:
                raise ValueError("Shopping cart is empty. Nothing to purchase.")
            cashier.process_purchase(self)
            self.purchase_history.extend(self.shopping_cart)
            print(f"Purchased items: {[product.name for product in self.purchase_history]}")
            self.shopping_cart.clear()
        except ValueError as e:
            print(f"Error during purchase: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during purchase: {e}")