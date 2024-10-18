finished_sandwiches = []

sandwich_orders = [
    'ham and cheese',
    'pastrami',
    'peanut butter and jelly',
    'pastrami',
    'nutella',
    'pastrami',
    'marmalade',
]

print('\nThe deli has run out of pastrami.')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    for sandwich in sandwich_orders:
        print(f'\nI made your {sandwich} sandwich.')
        finished_sandwiches.append(sandwich)
        sandwich_orders.remove(sandwich)

print('\nFinished Sandwiches: ')
for sandwich in finished_sandwiches:
    print(f"\t{sandwich} sandwich.")