favorite_places = {
    'kush star kish':           ['new zealand','jakarta','el salvador'],
    'playboi tatsei':           ['japan','china','dubai'],
    'lil mir':                  ['paris','france','london'],
    'poppin ecstacy':           ['sweden','finland','mexico'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s Favorite Places:")
    for place in places:
        print(f"\t{place.title()}")
    print('\n')