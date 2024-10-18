sandwich_orders = [
    'ham and cheese',
    'peanut butter and jelly',
    'nutella',
    'marmalade',
]

finished_sandwiches = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        print(f'\nI made your {sandwich} sandwich.')
        finished_sandwiches.append(sandwich)
        sandwich_orders.remove(sandwich)

print('\nFinished Sandwiches: ')
for sandwich in finished_sandwiches:
    print(f"\t{sandwich} sandwich.")