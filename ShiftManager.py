from typing import List
from Customer import Customer
from Employee import Employee
from LogisticsEmployee import LogisticsEmployee
from Product import Product
from Supermarket import Supermarket

class ShiftManager(LogisticsEmployee):
    def __init__(self, id: str, name: str, age: int, phone: str, employee_number: str, shift_hours: str, responsibility_area: str):
        super().__init__(id, name, age, phone, employee_number)
        self.shift_hours = shift_hours
        self.responsibility_area = responsibility_area

    def add_product_to_shelf(self, product: Product, supermarket: Supermarket):
        """Add a product to the supermarket shelf."""
        if product not in supermarket.get_products():
            supermarket.add_product(product)
            print(f"Product {product.name} added to the shelf in area {self.responsibility_area}.")
        else:
            print(f"Product {product.name} is already on the shelf in area {self.responsibility_area}.")

    def remove_product_from_shelf(self, product: Product, supermarket: Supermarket):
        """Remove a product from the supermarket shelf."""
        if product in supermarket.get_products():
            supermarket.remove_product(product)
            print(f"Product {product.name} removed from the shelf in area {self.responsibility_area}.")
        else:
            print(f"Product {product.name} is not on the shelf in area {self.responsibility_area}.")

    def update_employee(self, employee: Employee):
        """Update the information of an employee."""
        # Placeholder for logic to update employee information.
        pass

    def get_daily_customers(self, supermarket: Supermarket) -> List[Customer]:
        """Get a list of customers who visited the supermarket on the current day."""
        return supermarket.get_daily_customers()
