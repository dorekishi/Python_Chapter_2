class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.number_served = 0
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"{self.restaurant_name} makes {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is open.")

    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
            print(f"\n{restaurant.restaurant_name} has served {restaurant.number_served} "
                  f"people {restaurant.cuisine_type}"
                  f" so far.")
        else:
            print("\nYou can't 'un-serve' people!")

    def increment_number_served(self, increment):   # daily
        self.number_served += increment
        print(f"\n{increment} more people have been served today!")

restaurant = Restaurant('Raising Canes', 'chicken tenders, fries and buttered bread')

print(restaurant.number_served)

restaurant.number_served = 8
print(restaurant.number_served)

restaurant.set_number_served(1200)

restaurant.set_number_served(10)

restaurant.increment_number_served(300)

print(f"\nTotal Sales All Time: {restaurant.number_served}")