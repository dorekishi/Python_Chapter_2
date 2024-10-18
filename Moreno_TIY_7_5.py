age = ''

while age == '':
    age = input('How Old Are You (Number) ? ')
    age = int(age)

    if age < 3:
        print('Ticket Is Free!\n')
    elif 3 <= age <= 12:
        print('Ticket Is $10\n')
    elif age > 12:
        print('Ticket Is $15\n')

    age = ''