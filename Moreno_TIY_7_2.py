attendees = input('How many people are in your dinner group? ')
attendees = int(attendees)

if attendees > 8:
    print("You'll have have to wait for a table.")
else:
    print("Your table is ready.")