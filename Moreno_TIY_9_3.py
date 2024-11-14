class User:
    def __init__(self, first_name, last_name, phone_number, address, age):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.age = age

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old.")
        print(f"You can reach {self.first_name} at {self.phone_number}, and their address is {self.address}")

    def greet_user(self):
        print(f"Welcome in {self.first_name}!")

dorekishi   = User('Miguel','Moreno', '(123) 456 7890', '1234 Main St.', 18)
tatsei      = User('Jayden','Cooper', '(012) 345 6789', '2345 Main St.', 17)
xtasy       = User('Armando','Robles', '(901) 234 5678', '3456 Main St.', 19)

users = dorekishi, tatsei, xtasy

for user in users:
    print('\n'), user.describe_user(), user.greet_user()