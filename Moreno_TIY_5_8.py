usernames=['dorekishi',
           'kish',
           'mig',
           'admin',
           'cash kish']

for username in usernames:
    if 'admin' == username:
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {username}, thank you for logging in again.')