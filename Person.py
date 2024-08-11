from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, id: str, name: str, age: int, phone: str):
        try:
            if not isinstance(id, str):
                raise ValueError("ID must be a string")
            if not isinstance(name, str):
                raise ValueError("Name must be a string")
            if not isinstance(age, int) or age <= 0:
                raise ValueError("Age must be a positive integer")
            if not isinstance(phone, str):
                raise ValueError("Phone must be a string")

            self.id = id
            self.name = name
            self.age = age
            self.phone = phone
        except ValueError as e:
            print(f"Error initializing Person: {e}")

    @abstractmethod
    def __str__(self) -> str:
        pass

    def __eq__(self, other) -> bool:
        if isinstance(other, Person):
            return self.id == other.id
        return False
