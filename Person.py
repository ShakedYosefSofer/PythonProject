from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, id: str, name: str, age: int, phone: str):
        try:
            if not isinstance(id, str) or not id.strip():
                raise ValueError("ID must be a non-empty string")
            if not isinstance(name, str) or not name.strip():
                raise ValueError("Name must be a non-empty string")
            if not isinstance(age, int) or age <= 0:
                raise ValueError("Age must be a positive integer")
            if not isinstance(phone, str) or not phone.strip():
                raise ValueError("Phone must be a non-empty string")

            self.id = id
            self.name = name
            self.age = age
            self.phone = phone
        except ValueError as e:
            print(f"Error initializing Person: {e}")
            raise  # מעדכן את התוכנית שהתהליך נכשל

    @abstractmethod
    def __str__(self) -> str:
        pass

# check the function
    def __eq__(self, other) -> bool:
        if isinstance(other, Person):
            return self.id == other.id
        return False
