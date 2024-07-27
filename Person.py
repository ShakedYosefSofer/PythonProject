import random
import string

class Person:
    # chck something
    def customers(self):
        customer1 = ['111111111', 'Alice Smith', 25, '555-111111']
        customer2 = ['222222222', 'Bob Johnson', 35, '555-222222']
        customer3 = ['333333333', 'Charlie Brown', 45, '555-333333']
        customer4 = ['123456789', 'John Doe', 30, '555-123456']

    def generate_random_number(self):
        number = ''.join(random.choice(string.digits)
        for _ in range(8))
        return number

#  Person
person = Person()
random_number = person.generate_random_number()
print(random_number)




#
#
# class Person(ABC):
#     def __init__(self, id, name, age, phone):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.phone = phone
#
#     @abstractmethod
#     def __str__(self):
#         pass
#
#     def __eq__(self, other):
#         if isinstance(other, Person):
#             return self.id