from Person import Person

class Employee(Person):
    def __init__(self, id: str, name: str, age: int, phone: str, employee_number: str):
        super().__init__(id, name, age, phone)
        try:
            if not employee_number or not isinstance(employee_number, str):
                raise ValueError("Employee number must be a non-empty string")
            self.employee_number = employee_number
        except ValueError as e:
            print(f"Error initializing employee: {e}")

    def __str__(self) -> str:
        return f"Employee: {self.name} (Employee #: {self.employee_number})"



