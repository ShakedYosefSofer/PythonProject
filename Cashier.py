from PythonProject.PythonProject.Customer import Customer
from PythonProject.PythonProject.Employee import Employee
from PythonProject.PythonProject.Product import Product


class Cashier(Employee):
    def __init__(self, id: str, name: str, age: int, phone: str, employee_number: str, register_number: str, shift_type: str):
        super().__init__(id, name, age, phone, employee_number)
        self.register_number = register_number
        self.shift_type = shift_type

    def sell_to_customer(self, customer: Customer, product: Product):
        if product in customer.shopping_list:
            customer.shopping_list.remove(product)
            customer.purchased_items.append(product)
            print(f"Sold {product.name} to {customer.name}")
        else:
            print(f"Error: {product.name} not in {customer.name}'s shopping list")










# class Cashier(Employee):
#     def __init__(self, id, name, age, phone, employee_number, register_number, shift_type):
#         super().__init__(id, name, age, phone, employee_number)
#         self.register_number = register_number
#         self.shift_type = shift_type
#
#     def sell_to_customer(self, customer, product):
#         if product in customer.shopping_list:
#             customer.shopping_list.remove(product)
#             customer.purchased_items.append(product)
#             print(f"Sold {product.name} to {customer.name}")
#         else:
#             print(f"Error: {product.name} not in {customer.name}'s shopping list")
