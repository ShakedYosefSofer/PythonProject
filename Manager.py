from abc import ABC, abstractmethod
from Employee import Employee
from Supermarket import Supermarket

class Manager(Employee, ABC):
    @abstractmethod
    def add_employee(self, employee: Employee, supermarket: Supermarket):
        """Add an employee to the supermarket."""
        pass

    @abstractmethod
    def remove_employee(self, employee: Employee, supermarket: Supermarket):
        """Remove an employee from the supermarket."""
        pass

    @abstractmethod
    def update_employee(self, employee: Employee):
        """Update the information of an employee."""
        pass
