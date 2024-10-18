poll = True

dream_vacation = {}

while poll:
    name = input('Hello, Please Enter Your Name: ')
    spot = input(f"Hi {name.title().strip()}, Please Enter Your Dream Vacation Spot: ")

    dream_vacation[name] = spot

    yes_no = input(f"Would You Like Another Person To Respond (yes/no) ? \n")
    if yes_no == 'no':
        print('\n')
        poll = False

    print('\n')

print('Poll Results: ')
for name, spot in dream_vacation.items():
    print(f"\t{name.title().strip()} would like to go to {spot.title().strip()}")