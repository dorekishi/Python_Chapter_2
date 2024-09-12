basicFoods=('fried chicken',
            'dinner_roll',
            'mac n cheese',
            'pizza',
            'mashed potatoes n gravy')
print("The Buffet Offers:")
for food in basicFoods:
    print(food.title())

#TUPLE ERROR BELOW IN # LINE
#basicFoods[0]='watermelon'
#LESSON CONTINUED BELOW

basicFoods=('fried chieckn',
            'dinner roll',
            'watermelon',
            'pizza',
            'grapes')
print("\nNew Buffet Menu Contains:")
for food in basicFoods:
    print(food.title())