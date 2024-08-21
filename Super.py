from Cashier import Cashier
from Customer import Customer
from GeneralManager import GeneralManager
from Product import Product
from ShiftManager import ShiftManager
from Stocker import Stocker
from Supermarket import Supermarket
from Person import Person  # Ensure Person is defined or imported correctly


class Super:
    def __init__(self):
        self.supermarket = Supermarket()

    def run(self):
        while True:
            try:
                user_type = input("Enter user type (customer/stocker/cashier/shift_manager/general_manager) or 'q' to quit: ").strip().lower()
                if user_type == 'q':
                    break

                user = self.create_user(user_type)
                if user:
                    if user_type == "customer":
                        self.process_customer_choice(user)
                    elif user_type == "stocker":
                        self.process_stocker_choice(user)
                    elif user_type == "cashier":
                        self.process_cashier_choice(user)
                    elif user_type == "shift_manager":
                        self.process_shift_manager_choice(user)
                    elif user_type == "general_manager":
                        self.process_general_manager_choice(user)
                else:
                    print("Invalid user type. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")

        print("Thank you for using our supermarket system. Goodbye!")

    def create_user(self, user_type: str) -> Person:
        try:
            id = input("Enter ID: ").strip()
            name = input("Enter name: ").strip()
            age = int(input("Enter age: ").strip())
            phone = input("Enter phone number: ").strip()

            if user_type == "customer":
                return Customer(id, name, age, phone)

            elif user_type == "stocker":
                employee_number = input("Enter employee number: ").strip()
                vest_color = input("Enter vest color: ").strip()

                return Stocker(id, name, age, phone, employee_number, vest_color)

            elif user_type == "cashier":
                employee_number = input("Enter employee number: ").strip()
                register_number = input("Enter register number: ").strip()
                shift_type = input("Enter shift type: ").strip()

                return Cashier(id, name, age, phone, employee_number, register_number, shift_type)

            elif user_type == "shift_manager":
                employee_number = input("Enter employee number: ").strip()
                shift_hours = input("Enter shift hours: ").strip()
                responsibility_area = input("Enter responsibility area: ").strip()

                return ShiftManager(id, name, age, phone, employee_number, shift_hours, responsibility_area)

            elif user_type == "general_manager":
                employee_number = input("Enter employee number: ").strip()
                management_level = input("Enter management level: ").strip()
                department = input("Enter department: ").strip()

                return GeneralManager(id, name, age, phone, employee_number, management_level, department)

            else:
                print("Invalid user type.")
                return None
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter correct values.")
            return None

    def process_customer_choice(self, customer):
        while True:
            choice = input("Enter choice (1: Add to cart, 2: Checkout, q: Quit): ").strip().lower()
            if choice == 'q':
                break
            elif choice == '1':
                product_id = input("Enter product ID to add to cart: ")
                product = self.supermarket.get_product_by_id(product_id)
                if product:
                    customer.add_product_to_cart(product)
                    print(f"{product.name} added to cart.")
                else:
                    print("Product not found.")
            elif choice == '2':
                cashier = self.create_user("cashier")
                if cashier:
                    cashier.process_purchase(customer)
                    print("Purchase completed.")
                break
            else:
                print("Invalid choice. Please try again.")

    def process_stocker_choice(self, stocker):
        while True:
            choice = input("Enter choice (1: Add product to shelf, 2: Remove product from shelf, q: Quit): ").strip().lower()
            if choice == 'q':
                break
            elif choice == '1':
                product = self.create_product()
                self.supermarket.add_product(product)
                print(f"{product.name} added to shelf.")
            elif choice == '2':
                product_id = input("Enter product ID to remove: ")
                product = self.supermarket.get_product_by_id(product_id)
                if product:
                    self.supermarket.remove_product(product)
                    print(f"{product.name} removed from shelf.")
                else:
                    print("Product not found.")
            else:
                print("Invalid choice. Please try again.")

    def process_cashier_choice(self, cashier):
        while True:
            choice = input("Enter choice (1: Process purchase, q: Quit): ").strip().lower()
            if choice == 'q':
                break
            elif choice == '1':
                customer_id = input("Enter customer ID: ")
                customer = self.supermarket.get_customer_by_id(customer_id)
                if customer:
                    cashier.process_purchase(customer)
                    print("Purchase processed.")
                else:
                    print("Customer not found.")
            else:
                print("Invalid choice. Please try again.")

    def process_shift_manager_choice(self, shift_manager):
        while True:
            choice = input("Enter choice (1: Add employee, 2: Remove employee, 3: Update employee, 4: Manage products, q: Quit): ").strip().lower()
            if choice == 'q':
                break
            elif choice == '1':
                employee = self.create_user("stocker")  # לדוגמה, ניתן גם ליצור סוגי עובדים אחרים
                shift_manager.add_employee(employee)
                print(f"Employee {employee.name} added.")
            elif choice == '2':
                employee_id = input("Enter employee ID to remove: ")
                employee = self.supermarket.get_employee_by_id(employee_id)
                if employee:
                    shift_manager.remove_employee(employee)
                    print(f"Employee {employee.name} removed.")
                else:
                    print("Employee not found.")
            elif choice == '3':
                employee_id = input("Enter employee ID to update: ")
                employee = self.supermarket.get_employee_by_id(employee_id)
                if employee:
                    shift_manager.update_employee(employee)
                    print(f"Employee {employee.name} updated.")
                else:
                    print("Employee not found.")
            elif choice == '4':
                self.process_stocker_choice(shift_manager)  # שימוש בפונקציות של הסדרן לניהול מוצרים
            else:
                print("Invalid choice. Please try again.")

    def process_general_manager_choice(self, general_manager):
        while True:
            choice = input("Enter choice (1: Add employee, 2: Remove employee, 3: Update employee, 4: View products on shelves, 5: View daily revenue, q: Quit): ").strip().lower()
            if choice == 'q':
                break
            elif choice in ['1', '2', '3']:
                self.process_shift_manager_choice(general_manager)
            elif choice == '4':
                products = self.supermarket.get_products()
                print("Products on shelves:")
                for product in products:
                    print(product.name)
            elif choice == '5':
                revenue = self.supermarket.get_daily_revenue()
                print(f"Total daily revenue: {revenue}")
            else:
                print("Invalid choice. Please try again.")

    def create_product(self):
        product_id = input("Enter product ID: ").strip()
        name = input("Enter product name: ").strip()
        department = input("Enter department: ").strip()
        price = float(input("Enter price: ").strip())
        return Product(product_id, name, department, price)

