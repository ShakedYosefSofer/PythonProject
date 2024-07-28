import json
from typing import List, Dict

from PythonProject.PythonProject.Customer import Customer
from PythonProject.PythonProject.Employee import Employee
from PythonProject.PythonProject.Product import Product


class Supermarket:
    def __init__(self):
        self.products: List[Product] = []
        self.employees: List[Employee] = []
        self.customers: List[Customer] = []
        self.daily_revenue = 0.0
        self.daily_purchases: Dict[str, List[Product]] = {}

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def remove_employee(self, employee: Employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def get_products(self) -> List[Product]:
        return self.products

    def get_daily_customers(self) -> List[Customer]:
        return self.customers

    def get_daily_revenue(self) -> float:
        return self.daily_revenue

    def update_daily_revenue(self, amount: float):
        self.daily_revenue += amount

    def record_purchase(self, customer: Customer, products: List[Product]):
        self.daily_purchases[customer.id] = products
        self.update_daily_revenue(sum(product.price for product in products))

    def save_to_file(self, filename: str):
        data = {
            "products": [{"name": p.name, "price": p.price, "category": p.category} for p in self.products],
            "daily_revenue": self.daily_revenue,
            "daily_purchases": {k: [p.name for p in v] for k, v in self.daily_purchases.items()}
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, filename: str):
        with open(filename, 'r') as f:
            data = json.load(f)
        self.products = [Product(**p) for p in data["products"]]
        self.daily_revenue = data["daily_revenue"]
        self.daily_purchases = {k: [Product(name=n, price=0, category="") for n in v] for k, v in data["daily_purchases"].items()}




#
#
#
# class Supermarket:
#     def __init__(self):
#         self.products = []
#         self.employees = []
#         self.customers = []
#         self.daily_revenue = 0
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def remove_product(self, product):
#         if product in self.products:
#             self.products.remove(product)
#
#     def add_employee(self, employee):
#         self.employees.append(employee)
#
#     def remove_employee(self, employee):
#         if employee in self.employees:
#             self.employees.remove(employee)
#
#     def add_customer(self, customer):
#         self.customers.append(customer)
#
#     def get_products(self):
#         return self.products
#
#     def get_daily_customers(self):
#         return self.customers
#
#     def get_daily_revenue(self):
#         return self.daily_revenue
#
#     def update_daily_revenue(self, amount):
#         self.daily_revenue += amount