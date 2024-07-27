class Super():
    def __init__(self):
        self.name = ""
        self.choice = 0

    def get_name(self):
        self.name = input("What is your name: ")

    def hello(self):
        print("Hello, " + self.name + "!")

    def get_choice(self):
        self.choice = int(input("Choose what you want to do but before this all options: " 
                                "\n number 1 is costumer"
                                "\n number 2 is usher  \n"))
        if self.choice == 1:
            # here have code to go to customer
            print("customer")
            pass
        elif self.choice == 2:
            # here have code to go to usher
            print("usher") #סדרן
            pass
#         123

obj = Super()
obj.get_name()
obj.hello()
obj.get_choice()



#
# class Super:
#     def __init__(self):
#         self.supermarket = Supermarket()
#         self.ui = UI(self.supermarket)
#
#     def run(self):
#         while True:
#             choice = self.ui.display_main_menu()
#             if choice == '1':
#                 # Create customer and show customer menu
#                 customer = Customer(input("ID: "), input("Name: "), int(input("Age: ")), input("Phone: "))
#                 self.supermarket.add_customer(customer)
#                 self.ui.customer_menu(customer)
#             elif choice == '2':
#                 # Create stocker and show stocker menu
#                 pass
#             elif choice == '3':
#                 # Create cashier and show cashier menu
#                 pass
#             elif choice == '4':
#                 # Create shift manager and show shift manager menu
#                 pass
#             elif choice == '5':
#                 # Create general manager and show general manager menu
#                 pass
#             elif choice == '6':
#                 print("Thank you for using our supermarket system. Goodbye!")
#                 break
#             else:
#                 print("Invalid option. Please try again.")
#
# if __name__ == "__main__":
#     supermarket_system = Super()
#     supermarket_system.run()