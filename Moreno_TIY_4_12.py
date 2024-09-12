my_foods=['pizza', 'falafel', 'carrot cake']
friend_foods=my_foods[:]

my_foods.append('canoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
#old program above
print('\n!!!!!!!!!!!!!!!!!!New Program Below!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#new program below

print("\nMy Friend's Favorite Foods:")
for FriendsFoods in friend_foods:
    print(f'{FriendsFoods}')

print("\nMy Favorite Foods:")
for MyFoods in my_foods:
    print(f'{MyFoods}')