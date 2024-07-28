from typing import List

from PythonProject.PythonProject.Customer import Customer
from PythonProject.PythonProject.Employee import Employee
from PythonProject.PythonProject.LogisticsEmployee import LogisticsEmployee
from PythonProject.PythonProject.Product import Product


class ShiftManager(LogisticsEmployee):
    def __init__(self, id: str, name: str, age: int, phone: str, employee_number: str, shift_hours: str, responsibility_area: str):
        super().__init__(id, name, age, phone, employee_number)
        self.shift_hours = shift_hours
        self.responsibility_area = responsibility_area

    def add_product_to_shelf(self, product: Product, supermarket: 'Supermarket'):
        supermarket.add_product(product)

    def remove_product_from_shelf(self, product: Product, supermarket: 'Supermarket'):
        supermarket.remove_product(product)

    def update_employee(self, employee: Employee):
        # Implement logic to update employee information
        pass

    def get_daily_customers(self, supermarket: 'Supermarket') -> List[Customer]:
        return supermarket.get_daily_customers()






# class ShiftManager(LogisticsEmployee):
#     def __init__(self, id, name, age, phone, employee_number, shift_hours, responsibility_area):
#         super().__init__(id, name, age, phone, employee_number)
#         self.shift_hours = shift_hours
#         self.responsibility_area = responsibility_area
#
#     def add_product_to_shelf(self, product, supermarket):
#         supermarket.add_product(product)
#
#     def remove_product_from_shelf(self, product, supermarket):
#         supermarket.remove_product(product)
#
#     def update_employee(self, employee):
#         # Implement logic to update employee information
#         pass
#
#     def get_daily_customers(self, supermarket):
#         return supermarket.get_daily_customers()