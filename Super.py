# class Super():
#     def __init__(self):
#         self.name = ""
#         self.choice = 0
#
#     def get_name(self):
#         self.name = input("What is your name: ")
#
#     def hello(self):
#         print("Hello, " + self.name + "!")
#
#     def get_choice(self):
#         self.choice = int(input("Choose what you want to do but before this all options: "
#                                 "\n number 1 is costumer"
#                                 "\n number 2 is usher  \n"))
#         if self.choice == 1:
#             # here have code to go to customer
#             print("customer")
#             pass
#         elif self.choice == 2:
#             # here have code to go to usher
#             print("usher") #סדרן
#             pass
# #         123
#
# obj = Super()
# obj.get_name()
# obj.hello()
# obj.get_choice()
#
from Classes.main import Person
from PythonProject.PythonProject.Cashier import Cashier
from PythonProject.PythonProject.Customer import Customer
from PythonProject.PythonProject.GeneralManager import GeneralManager
from PythonProject.PythonProject.ShiftManager import ShiftManager
from PythonProject.PythonProject.Stocker import Stocker
from PythonProject.PythonProject.Supermarket import Supermarket


def UI(supermarket):
    pass


class Super:
    def __init__(self):
        self.supermarket = Supermarket()
        self.ui = UI(self.supermarket)

    def run(self):
        while True:
            user_type = input(
                "Enter user type (customer/stocker/cashier/shift_manager/general_manager) or 'q' to quit: ")
            if user_type == 'q':
                break

            user = self.create_user(user_type)
            if user:
                while True:
                    choice = self.ui.display_menu(user_type)
                    if not self.ui.process_menu_choice(user, choice):
                        break
            else:
                print("Invalid user type. Please try again.")

        self.supermarket.save_to_file("supermarket_data.json")
        print("Thank you for using our supermarket system. Goodbye!")

    def create_user(self, user_type: str) -> Person:
        id = input("Enter ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        phone = input("Enter phone number: ")

        if user_type == "customer":
            return Customer(id, name, age, phone)
        elif user_type == "stocker":
            employee_number = input("Enter employee number: ")
            vest_color = input("Enter vest color: ")
            return Stocker(id, name, age, phone, employee_number, vest_color)
        elif user_type == "cashier":
            employee_number = input("Enter employee number: ")
            register_number = input("Enter register number: ")
            shift_type = input("Enter shift type: ")
            return Cashier(id, name, age, phone, employee_number, register_number, shift_type)
        elif user_type == "shift_manager":
            employee_number = input("Enter employee number: ")
            shift_hours = input("Enter shift hours: ")
            responsibility_area = input("Enter responsibility area: ")
            return ShiftManager(id, name, age, phone, employee_number, shift_hours, responsibility_area)
        elif user_type == "general_manager":
            employee_number = input("Enter employee number: ")
            management_level = input("Enter management level: ")
            department = input("Enter department: ")
            return GeneralManager(id, name, age, phone, employee_number, management_level, department)
        else:
            return None
