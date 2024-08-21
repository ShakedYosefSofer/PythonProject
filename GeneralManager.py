from typing import List
from Employee import Employee
from Supermarket import Supermarket
from Product import Product

class GeneralManager(Employee):
    def __init__(self, id: str, name: str, age: int, phone: str, employee_number: str, management_level: str, department: str):
        super().__init__(id, name, age, phone, employee_number)
        self.management_level = management_level
        self.department = department

    def add_employee(self, employee: Employee, supermarket: Supermarket):
        if employee not in supermarket.employees:
            supermarket.add_employee(employee)
            print(f"Employee {employee.name} added to the supermarket.")
        else:
            print(f"Employee {employee.name} already exists in the supermarket.")

    def remove_employee(self, employee: Employee, supermarket: Supermarket):
        if employee in supermarket.employees:
            supermarket.remove_employee(employee)
            print(f"Employee {employee.name} removed from the supermarket.")
        else:
            print(f"Employee {employee.name} does not exist in the supermarket.")

    def update_employee(self, employee: Employee, new_name: str = None, new_phone: str = None, new_department: str = None):
        if new_name:
            employee.name = new_name
        if new_phone:
            employee.phone = new_phone
        if new_department:
            employee.department = new_department
        print(f"Employee {employee.id} updated.")

    def get_shelf_products(self, supermarket: Supermarket) -> List[Product]:
        return supermarket.get_products()

    def get_daily_revenue(self, supermarket: Supermarket) -> float:
        return supermarket.get_daily_revenue()
