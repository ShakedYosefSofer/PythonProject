class Cashier(Employee):
    def __init__(self, id, name, age, phone, employee_number, register_number, shift_type):
        super().__init__(id, name, age, phone, employee_number)
        self.register_number = register_number
        self.shift_type = shift_type

    def sell_to_customer(self, customer, product):
        if product in customer.shopping_list:
            customer.shopping_list.remove(product)
            customer.purchased_items.append(product)
            print(f"Sold {product.name} to {customer.name}")
        else:
            print(f"Error: {product.name} not in {customer.name}'s shopping list")
