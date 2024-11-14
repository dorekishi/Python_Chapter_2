class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.number_served = 0
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThe name of the restaurant is {self.restaurant_name}.")
        print(f"{self.restaurant_name} makes {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is open.")

    def increment_number_served(self, increment):   # daily
        self.number_served += increment
        print(f"\n{increment} more people have been served today!")