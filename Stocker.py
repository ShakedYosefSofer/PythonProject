from LogisticsEmployee import LogisticsEmployee
from Product import Product
from Supermarket import Supermarket

class Stocker(LogisticsEmployee):
    def __init__(self, id: str, name: str, age: int, phone: str, employee_number: str, vest_color: str):
        super().__init__(id, name, age, phone, employee_number)
        self.vest_color = vest_color

    def add_product_to_shelf(self, product: Product, supermarket: Supermarket):
        """Add a product to the supermarket shelf."""
        if product not in supermarket.get_products():
            supermarket.add_product(product)
            print(f"Product {product.name} added to the shelf.")
        else:
            print(f"Product {product.name} is already on the shelf.")

    def remove_product_from_shelf(self, product: Product, supermarket: Supermarket):
        """Remove a product from the supermarket shelf."""
        if product in supermarket.get_products():
            supermarket.remove_product(product)
            print(f"Product {product.name} removed from the shelf.")
        else:
            print(f"Product {product.name} is not on the shelf.")

    def manage_products(self, supermarket: Supermarket):
        """Provide the Stocker with the ability to manage products on the shelves."""
        while True:
            choice = input("Enter choice (1: Add product, 2: Remove product, q: Quit): ").strip().lower()
            if choice == 'q':
                break
            elif choice == '1':
                product = self.create_product(supermarket)
                self.add_product_to_shelf(product, supermarket)
            elif choice == '2':
                product_id = input("Enter product ID to remove: ")
                product = supermarket.get_product_by_id(product_id)
                if product:
                    self.remove_product_from_shelf(product, supermarket)
                else:
                    print("Product not found.")
            else:
                print("Invalid choice. Please try again.")

    def create_product(self, supermarket: Supermarket) -> Product:
        """Helper function to create a new product."""
        product_id = input("Enter product ID: ").strip()
        name = input("Enter product name: ").strip()
        department = input("Enter department: ").strip()
        price = float(input("Enter price: ").strip())
        return Product(product_id, name, department, price)