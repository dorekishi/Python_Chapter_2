class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"{self.restaurant_name} makes {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

restaurant = Restaurant('Raising Canes', 'chicken tenders, fries, buttered bread')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

print('\n')

restaurant.describe_restaurant()
restaurant.open_restaurant()