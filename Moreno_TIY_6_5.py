rivers = {
    'nile river':         'egypt',
    'michigan river':     'america',
    'rio bravo':    'mexico'
}

for river, location in rivers.items():
    print(f"The {river.title()} is located in {location.title()}!")

print('\nRivers:')
for river in rivers.keys():
    print(river.title())

print('\nLocations:')
for location in rivers.values():
    print(location.title())