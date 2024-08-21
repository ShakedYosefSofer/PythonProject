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

            if product in customer.shopping_cart:
                customer.shopping_cart.remove(product)
                customer.purchase_history.append(product)
                print(f"Sold {product.name} to {customer.name}")
            else:
                raise ValueError(f"{product.name} not in {customer.name}'s shopping cart")
        except TypeError as e:
            print(f"Type error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def process_purchase(self, customer: Customer):
        """Processes the customer's purchase by selling all items in their shopping cart."""
        try:
            if not isinstance(customer, Customer):
                raise TypeError("Invalid customer object")

            if not customer.shopping_cart:
                raise ValueError("Customer's shopping cart is empty.")

            for product in customer.shopping_cart:
                self.sell_to_customer(customer, product)
            print(f"Purchase complete for {customer.name}.")
        except TypeError as e:
            print(f"Type error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")