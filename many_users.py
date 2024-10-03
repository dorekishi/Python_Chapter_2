users = {
    'aeinstein': {
        'first':    'albert',
        'last':     'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first':    'marie',
        'last':     'curie',
        'location': 'paris',
    },
}

for username, users_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{users_info['first']} {users_info['last']}"
    location = users_info['location']

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")