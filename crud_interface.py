from abc import ABC, abstractmethod


# Defines the rules that implementing classes must follow.
class CrudInterface(ABC):

    # Every implementing class must define these CRUD methods.
    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def get_by_id(self, item_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, item_id, data):
        pass

    @abstractmethod
    def delete(self, item_id):
        pass