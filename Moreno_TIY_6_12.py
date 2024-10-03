#from 'many_users' example
#i am changing the user's usernames and i am going to add more information to them
#i am going to change the way the dictionaries inside of the 'users' dictionary are organized to my preferences

users = {
    'KushStarKish': {

        'name': {
            'first':    'miguel',
            'middle':   'daniel',
            'last':     'moreno',
            'suffix':    '',
        },

        'phone number': '(123) 456 7890',
        'sex':          'male',
        'age':          18,
    },

    'PlayboiTatsei': {

        'name': {
            'first': 'jayden',
            'middle': '',
            'last': 'cooper',
            'suffix': '',
        },

        'phone number': '(234) 567 8901',
        'sex': 'male',
        'age': 17,
    },

    'AveryTheDestroyer': {

        'name': {
            'first': 'avery',
            'middle': 'michelle',
            'last': 'patterson',
            'suffix': '',
        },

        'phone number': '(345) 678 9012',
        'sex': 'female',
        'age': 19,
    },
}

#username is key 'kushstarkish'
#users_data is value 'name',etc.

#need users_data['name'] to become key 'name'
#first, middle, last, suffix should become value 'names'

for username, users_data in users.items():
    print(f"{username}:")
    full_name = (f"{users_data['name']['first'].title()} {users_data['name']['middle'].title()} "
                 f"{users_data['name']['last'].title()} {users_data['name']['suffix'].title()}")
    print(f"\tFull Name: {full_name}")
    print(f"\tNumber: {users_data['phone number']}")
    print(f"\tSex: {users_data['sex']}")
    print(f"\tAge: {users_data['age']}")
    print('\n')

#FINISHED REMODELING!
#If i wanted to be stupid nerdy i could have made an if-elif chain for the full name part since not everyone
#would have had a middle name, suffix, or both but i'm not nerdy enough for all that