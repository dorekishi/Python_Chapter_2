# Create a list from an input that includes 5 fast food restaurants.

popular_food_restaurants = [
    'arbys',
    'mcdonalds',
    'culvers',
    'pizza hut',
    'rallys'
]

print('\n')
# Create a dictionary from user input and then check to see if the user input is in a dictionary of popular fast-food
# restaurants.
# The key should be the name of the student, and the values should be a list of different fast-food
# restaurants.
# Include 8 students' fast food restaurants in your dictionary.
# Write a while loop that will loop until 8 students have answered your survey.
# You should also create a loop that allows students to add multiple entries to the dictionary.

users_lists_fast_foods = {}  # set dictionary

active_a = True

while active_a:
    # if theres more than 8 entries, end the while loop
    if len(users_lists_fast_foods) == 8:

        active_a = False
    # if there isn't 8 entries, keep going
    else:

        name = input('Please Type Your Name: ')  # receive and create name from user input

        places = []  # state that places is a list

        users_lists_fast_foods[name] = places  # make key and value entry for dictionary

        active_b = 0

        while active_b != 8:  # new loop in loop

            for k, v in users_lists_fast_foods.items():

                place = input('Please Type The Name of a Fast Food Restaurant: ')

                places.append(place)

                active_b = active_b + 1

                if active_b == 8:

                    break

        print('\n')

print('\n')
# Check to see If the input fast food restaurant is in your original list.
# If not on the list add it to your list.

for places in users_lists_fast_foods.values():
    for place in places:
        if place not in popular_food_restaurants:
            popular_food_restaurants.append(place)

print('\n')
# Make sure no duplicates are in your list.

print(len(popular_food_restaurants))

for place in popular_food_restaurants:
    popular_food_restaurants = set(popular_food_restaurants)

print(len(popular_food_restaurants))

#no duplicates