from typing import List
from Person import Person
from Product import Product

class Customer(Person):
    def __init__(self, id: str, name: str, age: int, phone: str):
        super().__init__(id, name, age, phone)
        self.shopping_list: List[Product] = []
        self.purchased_items: List[Product] = []

    def __str__(self) -> str:
        return f"Customer: {self.name} (ID: {self.id})"

    def add_to_shopping_list(self, product: Product):
        try:
            if not isinstance(product, Product):
                raise ValueError("Can only add instances of Product")
            self.shopping_list.append(product)
            print(f"Added {product.name} to {self.name}'s shopping list.")
        except ValueError as e:
            print(f"Error adding to shopping list: {e}")

    def purchase(self, cashier: 'Cashier'):
        try:
            if not self.shopping_list:
                raise ValueError("Shopping list is empty. Nothing to purchase.")

            for product in self.shopping_list:
                cashier.sell_to_customer(self, product)
            self.purchased_items.extend(self.shopping_list)
            print(f"Purchased items: {[product.name for product in self.purchased_items]}")
            self.shopping_list.clear()
        except ValueError as e:
            print(f"Error during purchase: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during purchase: {e}")
