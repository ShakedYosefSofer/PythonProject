from Customer import Customer
from Employee import Employee
from Product import Product


class Cashier(Employee):
    def __init__(self, id: str, name: str, age: int, phone: str, employee_number: str, register_number: str,
                 shift_type: str):
        super().__init__(id, name, age, phone, employee_number)
        self.register_number = register_number
        self.shift_type = shift_type

    def sell_to_customer(self, customer: Customer, product: Product):
        try:
            if not isinstance(customer, Customer):
                raise TypeError("Invalid customer object")
            if not isinstance(product, Product):
                raise TypeError("Invalid product object")

            if product in customer.shopping_list:
                customer.shopping_list.remove(product)
                customer.purchased_items.append(product)
                print(f"Sold {product.name} to {customer.name}")
            else:
                raise ValueError(f"{product.name} not in {customer.name}'s shopping list")
        except TypeError as e:
            print(f"Type error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
