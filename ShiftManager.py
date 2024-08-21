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
        self.supermarket = None  # Initialize the supermarket reference

    def add_product_to_shelf(self, product: Product):
        """Add a product to the supermarket shelf."""
        if product not in self.supermarket.get_products():
            self.supermarket.add_product(product)
            print(f"Product {product.name} added to the shelf in area {self.responsibility_area}.")
        else:
            print(f"Product {product.name} is already on the shelf in area {self.responsibility_area}.")

    def remove_product_from_shelf(self, product: Product):
        """Remove a product from the supermarket shelf."""
        if product in self.supermarket.get_products():
            self.supermarket.remove_product(product)
            print(f"Product {product.name} removed from the shelf in area {self.responsibility_area}.")
        else:
            print(f"Product {product.name} is not on the shelf in area {self.responsibility_area}.")

    def update_employee(self, employee: Employee):
        """Update the information of an employee."""
        # Placeholder for logic to update employee information.
        pass

    def add_employee(self, employee: Employee):
        """Add a new employee to the supermarket."""
        self.supermarket.employees.append(employee)
        print(f"Employee {employee.name} added to the supermarket.")

    def remove_employee(self, employee: Employee):
        """Remove an employee from the supermarket."""
        self.supermarket.employees.remove(employee)
        print(f"Employee {employee.name} removed from the supermarket.")

    def get_daily_customers(self) -> List[Customer]:
        """Get a list of customers who visited the supermarket on the current day."""
        return self.supermarket.get_daily_customers()

    def set_supermarket(self, supermarket: Supermarket):
        """Set the supermarket reference for the ShiftManager."""
        self.supermarket = supermarket