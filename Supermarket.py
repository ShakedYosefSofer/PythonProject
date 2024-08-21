from typing import List, Dict
from Customer import Customer
from Employee import Employee
from Product import Product

class Supermarket:
    def __init__(self):
        self.products: List[Product] = []
        self.employees: List[Employee] = []
        self.customers: List[Customer] = []
        self.daily_revenue: float = 0.0
        self.daily_purchases: Dict[str, List[Product]] = {}

    def add_product(self, product: Product):
        """Add a product to the supermarket inventory."""
        if product not in self.products:
            self.products.append(product)
            print(f"Product {product.name} added to inventory.")
        else:
            print(f"Product {product.name} already exists in the inventory.")

    def remove_product(self, product: Product):
        """Remove a product from the supermarket inventory."""
        if product in self.products:
            self.products.remove(product)
            print(f"Product {product.name} removed from inventory.")
        else:
            print(f"Product {product.name} not found in the inventory.")

    def add_employee(self, employee: Employee):
        """Add an employee to the supermarket."""
        if employee not in self.employees:
            self.employees.append(employee)
            print(f"Employee {employee.name} added to the team.")
        else:
            print(f"Employee {employee.name} already exists.")

    def remove_employee(self, employee: Employee):
        """Remove an employee from the supermarket."""
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"Employee {employee.name} removed from the team.")
        else:
            print(f"Employee {employee.name} not found.")

    def add_customer(self, customer: Customer):
        """Add a customer to the supermarket."""
        if customer not in self.customers:
            self.customers.append(customer)
            print(f"Customer {customer.name} added to the customer list.")
        else:
            print(f"Customer {customer.name} already exists.")

    def get_products(self) -> List[Product]:
        """Return a list of all products in the supermarket."""
        return self.products

    def get_daily_customers(self) -> List[Customer]:
        """Return a list of customers who visited the supermarket today."""
        return self.customers

    def get_daily_revenue(self) -> float:
        """Return the total revenue for the day."""
        return self.daily_revenue

    def update_daily_revenue(self, amount: float):
        """Update the daily revenue by a certain amount."""
        if amount < 0:
            print("Revenue amount cannot be negative.")
        else:
            self.daily_revenue += amount
            print(f"Revenue updated by {amount}. Total revenue: {self.daily_revenue}")

    def record_purchase(self, customer: Customer, products: List[Product]):
        """Record a customer's purchase and update daily revenue."""
        try:
            self.daily_purchases[customer.id] = products
            total_price = sum(product.price for product in products)
            self.update_daily_revenue(total_price)
            print(f"Recorded purchase for customer {customer.name}: Total price = {total_price}")
        except Exception as e:
            print(f"Failed to record purchase: {e}")
