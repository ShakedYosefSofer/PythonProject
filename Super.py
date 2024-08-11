from Cashier import Cashier
from Customer import Customer
from GeneralManager import GeneralManager
from ShiftManager import ShiftManager
from Stocker import Stocker
from Supermarket import Supermarket
from Person import Person  # Ensure Person is defined or imported correctly


def UI(supermarket):
    # Implement the user interface logic here
    pass


class Super:
    def __init__(self):
        self.supermarket = Supermarket()
        self.ui = UI(self.supermarket)

    def run(self):
        while True:
            try:
                user_type = input("Enter user type (customer/stocker/cashier/shift_manager/general_manager) or 'q' to quit: ").strip().lower()
                if user_type == 'q':
                    break

                user = self.create_user(user_type)
                if user:
                    while True:
                        try:
                            choice = self.ui.display_menu(user_type)
                            if not self.ui.process_menu_choice(user, choice):
                                break
                        except ValueError as e:
                            print(f"Invalid menu choice: {e}. Please try again.")
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
