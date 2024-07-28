class Product:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self) -> str:
        return f"{self.name} - ${self.price:.2f} ({self.category})"

    def __eq__(self, other) -> bool:
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False













# class Product:
#     def __init__(self, name, price, category):
#         self.name = name
#         self.price = price
#         self.category = category
#
#     def __str__(self):
#         return f"{self.name} - ${self.price:.2f} ({self.category})"