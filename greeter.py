name = input(f"Please enter your username: ")
print(f"\nHello {name}!")

prompt = "If you share your first name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
name = name.title().strip()
print(f"\nHello, {name}!")

age = input(f"How old are you {name.title()}? ")

#inputs are turned into strings
#we can use int to change the string into an integer

age = int(age)

if age >= 18:
    print('\nYou are 18 or over.')
else:
    print('\nYou are under 18.')