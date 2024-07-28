from abc import ABC, abstractmethod

from PythonProject.PythonProject.Employee import Employee
from PythonProject.PythonProject.Product import Product


class LogisticsEmployee(Employee, ABC):
    @abstractmethod
    def add_product_to_shelf(self, product: Product, supermarket: 'Supermarket'):
        pass

    @abstractmethod
    def remove_product_from_shelf(self, product: Product, supermarket: 'Supermarket'):
        pass









# class LogisticsEmployee(Employee, ABC):
#     @abstractmethod
#     def add_product_to_shelf(self, product, supermarket):
#         pass
#
#     @abstractmethod
#     def remove_product_from_shelf(self, product, supermarket):
#         pass