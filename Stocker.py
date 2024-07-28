from PythonProject.PythonProject.LogisticsEmployee import LogisticsEmployee
from PythonProject.PythonProject.Product import Product


class Stocker(LogisticsEmployee):
    def __init__(self, id: str, name: str, age: int, phone: str, employee_number: str, vest_color: str):
        super().__init__(id, name, age, phone, employee_number)
        self.vest_color = vest_color

    def add_product_to_shelf(self, product: Product, supermarket: 'Supermarket'):
        supermarket.add_product(product)

    def remove_product_from_shelf(self, product: Product, supermarket: 'Supermarket'):
        supermarket.remove_product(product)









# class Stocker(LogisticsEmployee):
#     def __init__(self, id, name, age, phone, employee_number, vest_color):
#         super().__init__(id, name, age, phone, employee_number)
#         self.vest_color = vest_color
#
#     def add_product_to_shelf(self, product, supermarket):
#         supermarket.add_product(product)
#
#     def remove_product_from_shelf(self, product, supermarket):
#         supermarket.remove_product(product)