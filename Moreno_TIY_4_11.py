pizzatypes=['pineapple',
            'stuffed crust',
            'meat lovers']
for pizzatype in pizzatypes:
    print(f'I love {pizzatype} pizza!')
print(f'\nI love the flavor of {pizzatypes[0]} pizza.'), print(f'I love the cheese and idea of {pizzatypes[1]} pizza.'), print(f'I love the amount of toppings on {pizzatypes[2]} pizza.'), print('I really love pizza!')
#^old program above
#new program below
print('\n!!!!!!!!!!!!!!!!!!New Program Below!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

friend_pizzas=pizzatypes[:]
pizzatypes.append('chicken alfredo')
friend_pizzas.append('supreme')
print('\nMy favorite pizzas are:')
for mypizzas in pizzatypes:
    print(mypizzas.title())

print("\nMy friend's favorite pizzas are:")
for friendsPizzas in friend_pizzas:
    print(friendsPizzas.title())