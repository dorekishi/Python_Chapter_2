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

    def increment_number_served(self, increment):   # daily
        self.number_served += increment
        print(f"\n{increment} more people have been served today!")

class IceCreamStand(Restaurant):
    def __init__(self, flavors, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        flavors = [flavor for flavor in flavors.split()]
        self.flavors = flavors

    def describe_flavors(self):
        print(f"\n{self.restaurant_name} has {len(self.flavors)} flavors!")
        print(f"Including:")
        for flavor in self.flavors:
            print(f"\t{flavor}")

zestos = IceCreamStand("vanilla, chocolate, cherry, banana, strawberry", "Zestos",
                       "chili dogs")

zestos.describe_flavors()