tatsei  =   {
    'first_name':      'jayden',
    'last_name':       'cooper',
    'age':             17,
    'city':            'fort wayne'}

ecstacy  =   {
    'first_name':      'armando',
    'last_name':       'robles',
    'age':             19,
    'city':            'fort wayne'}

nickelas  =   {
    'first_name':      'nickelas',
    'last_name':       'rogers',
    'age':             18,
    'city':            'fort wayne'}

people = [
    tatsei,
    ecstacy,
    nickelas
]

for person in people:
    full_name =f"{person['first_name']} {person['last_name']}"
    print(f"\nFull Name: {full_name.title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tCity: {person['city']}")