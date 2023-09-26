import random
import string
class Person():

    def customers():
        customer1 = ['111111111', 'Alice Smith', 25, '555-111111']
        customer2 = ['222222222', 'Bob Johnson', 35, '555-222222']
        customer3 = ['333333333', 'Charlie Brown', 45, '555-333333']
        customer4 = ['123456789', 'John Doe', 30, '555-123456']

    def generate_random_number():
        number = ''.join(random.choice(string.digits)
            for _ in range(8))
             return number

        random_number = generate_random_number()
        print(random_number)



