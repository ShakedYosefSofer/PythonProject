from typing import List

from PythonProject.PythonProject.Employee import Employee
from PythonProject.PythonProject.Product import Product


class GeneralManager(Employee):
    def __init__(self, id: str, name: str, age: int, phone: str, employee_number: str, management_level: str, department: str):
        super().__init__(id, name, age, phone, employee_number)
        self.management_level = management_level
        self.department = department

    def add_employee(self, employee: Employee, supermarket: 'Supermarket'):
        supermarket.add_employee(employee)

    def remove_employee(self, employee: Employee, supermarket: 'Supermarket'):
        supermarket.remove_employee(employee)

    def update_employee(self, employee: Employee):
        # Implement logic to update employee information
        pass

    def get_shelf_products(self, supermarket: 'Supermarket') -> List[Product]:
        return supermarket.get_products()

    def get_daily_revenue(self, supermarket: 'Supermarket') -> float:
        return supermarket.get_daily_revenue()






# class GeneralManager(Manager):
#     def __init__(self, id, name, age, phone, employee_number, management_level, department):
#         super().__init__(id, name, age, phone, employee_number)
#         self.management_level = management_level
#         self.department = department
#
#     def add_employee(self, employee, supermarket):
#         supermarket.add_employee(employee)
#
#     def remove_employee(self, employee, supermarket):
#         supermarket.remove_employee(employee)
#
#     def update_employee(self, employee):
#         # Implement logic to update employee information
#         pass
#
#     def get_shelf_products(self, supermarket):
#         return supermarket.get_products()
#
#     def get_daily_revenue(self, supermarket):
#         return supermarket.get_daily_revenue()