favorite_numbers    =   {
    'mason':       [4,7],
    'troy':        [6,8],
    'adams':       [9,6],
    'miguel':      [7,5],
    'avery':       [3,6]
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)
    print('\n')