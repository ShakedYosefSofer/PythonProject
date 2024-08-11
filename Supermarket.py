from typing import List, Dict

from Customer import Customer
from Employee import Employee
from Product import Product


class Supermarket:
    def __init__(self):
        self.products: List[Product] = []
        self.employees: List[Employee] = []
        self.customers: List[Customer] = []
        self.daily_revenue = 0.0
        self.daily_purchases: Dict[str, List[Product]] = {}

    def add_product(self, product: Product):
        if product not in self.products:
            self.products.append(product)
        else:
            print(f"Product {product.name} already exists in the inventory.")

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)
        else:
            print(f"Product {product.name} not found in the inventory.")

    def add_employee(self, employee: Employee):
        if employee not in self.employees:
            self.employees.append(employee)
        else:
            print(f"Employee {employee.name} already exists.")

    def remove_employee(self, employee: Employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print(f"Employee {employee.name} not found.")

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)
        else:
            print(f"Customer {customer.name} already exists.")

    def get_products(self) -> List[Product]:
        return self.products

    def get_daily_customers(self) -> List[Customer]:
        return self.customers

    def get_daily_revenue(self) -> float:
        return self.daily_revenue

    def update_daily_revenue(self, amount: float):
        if amount < 0:
            print("Revenue amount cannot be negative.")
        else:
            self.daily_revenue += amount

    def record_purchase(self, customer: Customer, products: List[Product]):
        try:
            self.daily_purchases[customer.id] = products
            self.update_daily_revenue(sum(product.price for product in products))
        except Exception as e:
            print(f"Failed to record purchase: {e}")
