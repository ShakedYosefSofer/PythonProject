from Classes.main import Person


class Employee(Person):
    def __init__(self, id: str, name: str, age: int, phone: str, employee_number: str):
        super().__init__(id, name, age, phone)
        self.employee_number = employee_number

    def __str__(self) -> str:
        return f"Employee: {self.name} (Employee #: {self.employee_number})"











# class Employee(Person):
#     def __init__(self, id, name, age, phone, employee_number):
#         super().__init__(id, name, age, phone)
#         self.employee_number = employee_number
#
#     def __str__(self):
#         return f"Employee: {self.name} (Employee #: {self.employee_number})"
