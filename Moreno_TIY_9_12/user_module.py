class User:
    def __init__(self, first_name, last_name, phone_number, address, age):
        self.login_attempts = 0
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.age = age

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old.")
        print(f"You can reach {self.first_name} at {self.phone_number}, and their address is {self.address}")

    def greet_user(self):
        print(f"\nWelcome in {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"\nLogin Attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"\nLogin Attempts Reset.")