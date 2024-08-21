from typing import List
from Employee import Employee
from Supermarket import Supermarket
from Product import Product

class GeneralManager(Employee):
    def __init__(self, id: str, name: str, age: int, phone: str, employee_number: str, management_level: str, department: str):
        super().__init__(id, name, age, phone, employee_number)
        self.management_level = management_level
        self.department = department
        self.supermarket = None  # Initialize the supermarket reference

    def add_employee(self, employee: Employee):
        """Add a new employee to the supermarket."""
        if employee not in self.supermarket.employees:
            self.supermarket.add_employee(employee)
            print(f"Employee {employee.name} added to the supermarket.")
        else:
            print(f"Employee {employee.name} already exists in the supermarket.")

    def remove_employee(self, employee: Employee):
        """Remove an employee from the supermarket."""
        if employee in self.supermarket.employees:
            self.supermarket.remove_employee(employee)
            print(f"Employee {employee.name} removed from the supermarket.")
        else:
            print(f"Employee {employee.name} does not exist in the supermarket.")

    def update_employee(self, employee: Employee, new_name: str = None, new_phone: str = None, new_department: str = None):
        """Update the information of an employee."""
        if new_name:
            employee.name = new_name
        if new_phone:
            employee.phone = new_phone
        if new_department:
            employee.department = new_department
        print(f"Employee {employee.id} updated.")

    def get_shelf_products(self) -> List[Product]:
        """Get a list of all products on the shelves."""
        return self.supermarket.get_products()

    def get_daily_revenue(self) -> float:
        """Get the total daily revenue for the supermarket."""
        return self.supermarket.get_daily_revenue()

    def set_supermarket(self, supermarket: Supermarket):
        """Set the supermarket reference for the GeneralManager."""
        self.supermarket = supermarket