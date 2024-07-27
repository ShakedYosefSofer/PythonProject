class LogisticsEmployee(Employee, ABC):
    @abstractmethod
    def add_product_to_shelf(self, product, supermarket):
        pass

    @abstractmethod
    def remove_product_from_shelf(self, product, supermarket):
        pass