panchita  =   {
    'name':                 'panchita',
    'kind':                 'lizard',
    'owners_name':          'miguel',
}

mickey  =   {
    'name':                 'mickey',
    'kind':                 'dog',
    'owners_name':          'david',
}

luna  =   {
    'name':                 'luna',
    'kind':                 'cat',
    'owners_name':          'mia',
}

pets = [
    panchita,
    mickey,
    luna
]

for pet in pets:
    print(f"{pet['name'].title()}:")
    print(f"\tOwners Name: {pet['owners_name'].title()}")
    print(f"\tPet Kind: {pet['kind'].title()}\n")
