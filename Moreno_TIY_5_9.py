usernames=[]

if usernames:
    for username in usernames:
        if 'admin' == username:
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again.')
else:
    print('We need to find some users!')