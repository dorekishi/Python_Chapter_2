class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"{self.restaurant_name} makes {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

mcdonalds = Restaurant('McDonalds', 'burgers and fries')
tacobell = Restaurant('TacoBell', 'tacos and burritos')
zestos = Restaurant('Zestos', 'ice cream and chili dogs')

restaurants = mcdonalds, tacobell, zestos

for restaurant in restaurants:
    restaurant.describe_restaurant()
    print('\n')