class Stocker(LogisticsEmployee):
    def __init__(self, id, name, age, phone, employee_number, vest_color):
        super().__init__(id, name, age, phone, employee_number)
        self.vest_color = vest_color

    def add_product_to_shelf(self, product, supermarket):
        supermarket.add_product(product)

    def remove_product_from_shelf(self, product, supermarket):
        supermarket.remove_product(product)