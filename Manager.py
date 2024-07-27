class Manager(Employee, ABC):
    @abstractmethod
    def add_employee(self, employee, supermarket):
        pass

    @abstractmethod
    def remove_employee(self, employee, supermarket):
        pass

    @abstractmethod
    def update_employee(self, employee):
        pass