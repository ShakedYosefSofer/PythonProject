from typing import List


class Product:
    def __init__(self, name: str, price: float, category: str):
        try:
            if not name or not isinstance(name, str):
                raise ValueError("Name must be a non-empty string")
            if price <= 0 or not isinstance(price, (float, int)):
                raise ValueError("Price must be a positive number")
            if not category or not isinstance(category, str):
                raise ValueError("Category must be a non-empty string")

            self.name = name
            self.price = price
            self.category = category
        except ValueError as e:
            print(f"Error initializing product: {e}")

    def __str__(self) -> str:
        return f"{self.name} - ${self.price:.2f} ({self.category})"

    def __eq__(self, other) -> bool:
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'price': self.price,
            'category': self.category
        }

    @staticmethod
    def from_dict(data: dict) -> 'Product':
        return Product(
            name=data['name'],
            price=data['price'],
            category=data['category']
        )

