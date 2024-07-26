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
