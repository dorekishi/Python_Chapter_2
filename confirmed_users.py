unconfirmed_users = [
    'alice',
    'brian',
    'candace',
]

confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying User: {current_user.title()}")
    confirmed_users.append(current_user)

print(f"\nThe Following Users Have Been Confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())