from user_module import User

class Privileges:
    def __init__(self):
        privileges = ["can add a post", "can delete a post", "can ban a user"]
        self.privileges = privileges

    def show_privileges(self):
        print('\n')
        for privilege in self.privileges:
            print(f"This user {privilege}.")

class Admin(User):
    def __init__(self, first_name, last_name, phone_number, address, age):
        super().__init__(first_name, last_name, phone_number, address, age)
        self.privileges = Privileges()