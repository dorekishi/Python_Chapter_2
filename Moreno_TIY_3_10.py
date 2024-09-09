#Creating a list
ug_brands=['vetements',
           'rick owens',
           'balenciaga',
           'DC',
           'affliction',
           'newrock',
           'demonias',
           'G Shock',
           'Chrome Hearts',
           'van cleef',
           'rolex',
           'rock revival',
           'IfSixWasNine',
           'hood by air',
           'goyard']

#displaying my list
print(f'\n{ug_brands}')

#displaying a brand from my list in uppercase
print(f'\n{ug_brands[9].upper()}')

#displaying a brand from my list in lowercase
print(f'\n{ug_brands[-8].lower()}')

#replacing a brand from my list with string
ug_brands[0]='I need a vetements hoodie'
print(f'\n{ug_brands[0]}')
#replacing string from above back to its original brand
ug_brands[0]='vetements'

#adding a brand to the end of my list
ug_brands.append('oakley')
print(f'\n{ug_brands}')

#inserting a brand to the beginning of my list
ug_brands.insert(0, 'AP Skelly')
print(f'\n{ug_brands[0]}')

#removing a brand from my list
del ug_brands[16]
print(f'\n{ug_brands}')

#using pop() method for a more unpopular brand compared to most others on my list and using titlecase
popped_ug_brands=ug_brands.pop()
print(f'\n{popped_ug_brands.title()} are kinda unpopular.')

#removing a cool brand that I wouldn't wear
ug_brands.remove('demonias')
print(f'\n{ug_brands}')

#removing a brand and stating reasoning for removal
too_expensive_and_popular='balenciaga'
ug_brands.remove(too_expensive_and_popular)
print(f'\n{ug_brands}')
print(f'{too_expensive_and_popular.title()} is too expensive and popular to use.')

#series of print codes in different temporal/permanent alphabetical/reverse-alphabetical og ug_brands list using different methods
print(f'\nMy list of underground brands are temporarily in alphabetical order: {sorted(ug_brands)}')
print(f'Proof: {ug_brands}')
#
print(f'\nMy list of underground brands are temporarily in reverse alphabetical order: {sorted(ug_brands, reverse=True)}')
print(f'Proof: {ug_brands}')
#
ug_brands.sort()
print(f'\nMy list of underground brands are permanently in alphabetical order: {ug_brands}')
#
ug_brands.sort(reverse=True)
print(f'My list of underground brands are permanently in reverse alphabetical order: {ug_brands}')

#stating how many brands are left in the list
print(f'\nIn the end of using all the new code from chapter 3, we are left with {len(ug_brands)} underground brands.')