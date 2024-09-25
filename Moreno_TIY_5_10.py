current_users=['Dorekishi',
               'Kish',
               'Mig',
               'Admin',
               'Cash Kish']

current_users=[item.lower() for item in current_users]

#print(current_users)
#CHECK IF CURRENT USERS NAMES ARE LOWER

new_users=['Miguel',
           'Daniel',
           'Moreno',
           'Cash Kish',
           'Dorekishi']

new_users=[item.lower() for item in new_users]

for new_users_name in new_users:
    if new_users_name in current_users:
        print(f"\nSomeone is already using '{new_users_name}'.")
        print(f"Please select a new username.")
    else:
        print(f"'{new_users_name}' is available!")
