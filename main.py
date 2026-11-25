
from crud_interface import CrudInterface


# Inherits from CrudInterface.
# All abstract methods must be implemented, or Python throw a TypeError.
class User(CrudInterface):

    def __init__(self):
        self.users = []

    # Implements the create method.
    def create(self, data):
        self.users.append(data)
        print("User created successfully.")

    # Implements the get_all method.
    def get_all(self):
        return self.users

    # Implements the get_by_id method.
    def get_by_id(self, item_id):
        if 0 <= item_id < len(self.users):
            return self.users[item_id]
        return None

    # Implements the update method.
    def update(self, item_id, data):
        if 0 <= item_id < len(self.users):
            self.users[item_id].update(data)
            print("User updated successfully.")
        else:
            print("User not found.")

    # Implements the delete method.
    def delete(self, item_id):
        if 0 <= item_id < len(self.users):
            self.users.pop(item_id)
            print("User deleted successfully.")
        else:
            print("User not found.")


# Testing the CRUD operations.
user = User()

user.create({"name": "Newton", "email": "newton@example.com"})
user.create({"name": "Alex", "email": "alex@example.com"})

print("All users:", user.get_all())

user.update(0, {"name": "Newton Bepari"})
user.delete(1)

print("User details:", user.get_by_id(0))
