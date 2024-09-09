#Creating 3 empty lists
ugBrands1 = []
ugBrands2 = []
ugBrands3 = []

#adding 5 items in each list
ugBrands1.insert(0,'vetements')
ugBrands1.insert(0,'rick owen')
ugBrands1.insert(0,'balenciaga')
ugBrands1.insert(0,'DC')
ugBrands1.insert(0,'affliction')

ugBrands2.insert(0,'newrock')
ugBrands2.insert(0,'demonias')
ugBrands2.insert(0,'G Shock')
ugBrands2.insert(0,'Chrome Hearts')
ugBrands2.insert(0,'Van Cleef')

ugBrands3.insert(0,'rolex')
ugBrands3.insert(0,'rock revival')
ugBrands3.insert(0,'IfSixWasNine')
ugBrands3.insert(0,'hood by air')
ugBrands3.insert(0,'goyard')

#list output test
print(ugBrands1)
print(ugBrands2)
print(ugBrands3)

#displaying a brand from my lists in uppercase
print(f'I LOVE MY {ugBrands1[3].upper()} SHOES.')

#displaying a brand from my lists in lowercase
print(f'i love my {ugBrands2[2].lower()} watch.')

#replacing a brand from my list with string and pop method with titlecase method
print(f"I don't like {ugBrands3[0].title()}.")
ehBrand=ugBrands3.pop(0)
ugBrands3[0]='sp5der'
print(f"I'd rather wear {ugBrands3[0].title()} than {ehBrand.title()}.")

#appending a brand to the end of my list
ugBrands1.append('cartier')
print(ugBrands1[5])

#inserting a brand to my list
ugBrands3.insert(2,'prada')
print(ugBrands3[2])

#removing a brand from my list
ugBrands3.remove('rock revival')
print(ugBrands3)

#series of print codes in different temporary/permanent alphabetical/reverse-alphabetical lists using different methods
print(f'\nMy list of underground brands are temporarily in alphabetical order: {sorted(ugBrands1)}')
print(f'Proof: {ugBrands1}')

print(f'\nMy list of underground brands are temporarily in reverse alphabetical order: {sorted(ugBrands2, reverse=True)}')
print(f'Proof: {ugBrands2}')

ugBrands3.sort()
print(f'\n\nMy list of underground brands are permanently in alphabetical order: \n{ugBrands3}')

ugBrands2.sort(reverse=True)
print(f'\nMy list of underground brands are permanently in reverse alphabetical order: \n{ugBrands2}')

#stating how many brands are left in my lists
print(f'\nThere are {len(ugBrands1)} left in List 1')
print(f'\nThere are {len(ugBrands2)} left in List 2')
print(f'\nThere are {len(ugBrands3)} left in List 3')