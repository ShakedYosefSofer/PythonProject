from typing import List

from Classes.main import Person
from PythonProject.PythonProject.Product import Product


class Customer(Person):
    def __init__(self, id: str, name: str, age: int, phone: str):
        super().__init__(id, name, age, phone)
        self.shopping_list: List[Product] = []
        self.purchased_items: List[Product] = []

    def __str__(self) -> str:
        return f"Customer: {self.name} (ID: {self.id})"

    def add_to_shopping_list(self, product: Product):
        self.shopping_list.append(product)

    def purchase(self, cashier: 'Cashier'):
        for product in self.shopping_list:
            cashier.sell_to_customer(self, product)
        self.purchased_items.extend(self.shopping_list)
        self.shopping_list.clear()













# class Customer(Person):
#     def __init__(self, id, name, age, phone):
#         super().__init__(id, name, age, phone)
#         self.shopping_list = []
#         self.purchased_items = []
#
#     def __str__(self):
#         return f"Customer: {self.name} (ID: {self.id})"
#
#     def add_to_shopping_list(self, product):
#         self.shopping_list.append(product)
#
#     def purchase(self, cashier):
#         for product in self.shopping_list:
#             cashier.sell_to_customer(self, product)
#         self.purchased_items.extend(self.shopping_list)
#         self.shopping_list.clear()
