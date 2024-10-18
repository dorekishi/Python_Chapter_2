pizza_topping = ''
pizza_toppings = []

active = True

while active:
    print("Enter 'quit' To Finish")
    pizza_topping = input('Enter A Pizza Topping: ')
    if pizza_topping.lower().strip() != 'quit':
        pizza_topping = pizza_topping.lower().strip()
        pizza_toppings.append(pizza_topping)
        print(f"\nAdded {pizza_topping} To Pizza.\n")
    if len(pizza_toppings) > 5:     #conditional test used here to stop the loop on next line
        break                       #break
    if pizza_topping.lower().strip() == 'quit':     #if 'quit' is entered, 'active' will become False on next line
        active = False                              #stops the loop

if pizza_toppings:
    print(f"Your Toppings: ")
    for pizza_topping in pizza_toppings:
        print(f"\t{pizza_topping.title()}")
else:
    print(f"No Toppings Chosen")
    print(f"You Have Chosen Cheese Pizza.")