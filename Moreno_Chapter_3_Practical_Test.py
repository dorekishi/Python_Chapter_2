#trace = twix
#seth = reeses
#josue = twix
#julian = sour patch kids
candies=['twix',
         'reeses',
         'twix',
         'sour patch kids']
print(f"Trace's Favorite Candy Is {candies[0].title()}.")
print(f"Seth's Favorite Candy Is {candies[1].title()}.")
print(f"Josue's Favorite Candy Is {candies[2].title()}.")
print(f"Julian's Favorite Candy Is {candies[3].title()}.")
#
print(f'\n{candies}\n')
#
for candy in candies:
    print(candy)
#
print('\ncandies sorted:')
candies.sort()
for candy in candies:
    print(candy)
#
print('\ncandies sorted with a skipped line:\n')
candies.sort()
for candy in candies:
    print(f'{candy}\n')
#
#list to prove it's reversed below
print(candies)
#
#McKinstry's favorite candy is Almond Joy
#
candies.append('almond joy')
#reversed list below
print('\n')
candies.sort(reverse=True)
print(candies)
print('\n')
#
print(f"The candies list is {len(candies)} items long.")