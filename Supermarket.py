from typing import List, Dict, Optional
from Customer import Customer
from Employee import Employee
from Product import Product

class Supermarket:
    def __init__(self):
        self.products: List[Product] = []
        self.employees: List[Employee] = []
        self.customers: List[Customer] = []
        self.daily_revenue: float = 0.0
        self.daily_purchases: Dict[str, List[Product]] = {}

    def add_product(self, product: Product):
        """Add a product to the supermarket inventory."""
        if product not in self.products:
            self.products.append(product)
            print(f"Product {product.name} added to inventory.")
        else:
            print(f"Product {product.name} already exists in the inventory.")

    def remove_product(self, product: Product):
        """Remove a product from the supermarket inventory."""
        if product in self.products:
            self.products.remove(product)
            print(f"Product {product.name} removed from inventory.")
        else:
            print(f"Product {product.name} not found in the inventory.")

    def update_product(self, old_product: Product, new_product: Product):
        """Update an existing product in the inventory."""
        if old_product in self.products:
            index = self.products.index(old_product)
            self.products[index] = new_product
            print(f"Product {old_product.name} updated to {new_product.name}.")
        else:
            print(f"Product {old_product.name} not found in the inventory.")

    def get_product_by_name(self, name: str) -> Optional[Product]:
        """Return a product by its name, or None if not found."""
        for product in self.products:
            if product.name == name:
                return product
        print(f"Product {name} not found.")
        return None

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        """Return a product by its index in the product list, or None if not found."""
        if 0 <= product_id < len(self.products):
            return self.products[product_id]
        print(f"Product with ID {product_id} not found.")
        return None

    def get_products_by_category(self, category: str) -> List[Product]:
        """Return a list of products by category."""
        return [product for product in self.products if product.category == category]

    def calculate_inventory_value(self) -> float:
        """Calculate the total value of the inventory."""
        return sum(product.price for product in self.products)

    def get_products(self) -> List[Product]:
        """Return a list of all products in the supermarket."""
        return self.products

    def get_daily_customers(self) -> List[Customer]:
        """Return a list of customers who visited the supermarket today."""
        return self.customers

    def get_daily_revenue(self) -> float:
        """Return the total revenue for the day."""
        return self.daily_revenue

    def update_daily_revenue(self, amount: float):
        """Update the daily revenue by a certain amount."""
        if amount < 0:
            print("Revenue amount cannot be negative.")
        else:
            self.daily_revenue += amount
            print(f"Revenue updated by {amount}. Total revenue: {self.daily_revenue}")

    def record_purchase(self, customer: Customer, products: List[Product]):
        try:
            if not self.check_customer_balance(customer, products):
                return

            if customer.id not in self.daily_purchases:
                self.daily_purchases[customer.id] = []

            self.daily_purchases[customer.id].extend(products)
            total_price = sum(product.price for product in products)
            customer.balance -= total_price
            self.update_daily_revenue(total_price)
            customer.purchase_history.extend(products)
            print(f"DONE {customer.name}: sum price = {total_price}")
        except Exception as e:
            print(f"ERORR {e}")

    def remove_expired_products(self, expired_products: List[Product]):
        """Remove expired products from the inventory."""
        for product in expired_products:
            self.remove_product(product)
            print(f"Expired product {product.name} removed from inventory.")

    def apply_discount_to_category(self, category: str, discount: float):
        """Apply a discount to all products in a specific category."""
        for product in self.get_products_by_category(category):
            original_price = product.price
            product.price *= (1 - discount)
            print(f"Discount applied to {product.name}: {original_price:.2f} -> {product.price:.2f}")

    def add_customer(self, customer: Customer):
        """Add a customer to the supermarket."""
        if customer not in self.customers:
            self.customers.append(customer)
            print(f"Customer {customer.name} added to the customer list.")
        else:
            print(f"Customer {customer.name} already exists.")

    def remove_customer(self, customer: Customer):
        """Remove a customer from the supermarket."""
        if customer in self.customers:
            self.customers.remove(customer)
            print(f"Customer {customer.name} removed from the customer list.")
        else:
            print(f"Customer {customer.name} not found.")

    def get_customer_by_id(self, customer_id: str) -> Optional[Customer]:
        """Return a customer by their ID, or None if not found."""
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        print(f"Customer with ID {customer_id} not found.")
        return None

    def get_customers(self) -> List[Customer]:
        """Return a list of all customers in the supermarket."""
        return self.customers

    def get_customer_purchase_history(self, customer: Customer) -> List[Product]:
        """Return the purchase history of a specific customer."""
        return customer.purchase_history

    def get_customer_cart(self, customer: Customer) -> List[Product]:
        """Return the current shopping cart of a specific customer."""
        return customer.shopping_cart

    def clear_customer_cart(self, customer: Customer):
        """Clear the shopping cart of a specific customer."""
        customer.shopping_cart.clear()
        print(f"{customer.name}'s shopping cart has been cleared.")

        def check_customer_balance(self, customer: Customer, products: List[Product]) -> bool:
            total_price = sum(product.price for product in products)
            if customer.balance >= total_price:
                return True
            print(f"{customer.name} no money.")
            return False
