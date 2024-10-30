def sandwich_items_collector(*items):
    """accepts list of items a person wants on a sandwich"""
    print(f'\nOrder Summary:')
    for item in items:
        print(f"- {item}")

sandwich_items_collector(
    'ham',
)

sandwich_items_collector(
    'ham',
    'pepperoni',
)

sandwich_items_collector(
    'ham',
    'pepperoni',
    'swiss cheese'
)