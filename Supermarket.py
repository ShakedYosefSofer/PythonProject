class Supermarket:
    def __init__(self):
        self.products = []
        self.employees = []
        self.customers = []
        self.daily_revenue = 0

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_products(self):
        return self.products

    def get_daily_customers(self):
        return self.customers

    def get_daily_revenue(self):
        return self.daily_revenue

    def update_daily_revenue(self, amount):
        self.daily_revenue += amount