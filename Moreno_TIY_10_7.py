while True:
    try:
        a =  int(input(f"\nHow Many Apples Have You Eaten Today? "))
    except ValueError:
        print('Type A Integer Number.')
        continue

    try:
        b =  int(input(f"\nHow Many Apples Have You Eaten Yesterday? "))
    except ValueError:
        print('Type A Integer Number.')
        continue

    v = a + b

    print(f"You Have Eaten {v} Apples Yesterday and Today!")  # I just ran this test and realized a child wouldn't
                                                                # probably know what an integer is 😭😭😭
    if v >= 1:
        print(f"Good Job!")
    elif v < 0:
        print(f"how you got negative apples 😂😂😂 🤣🤣🤣")
    else:
        print(f"Lets Try To Eat A Apple Once A Day!")
    print(f"An Apple A Day Keeps The Doctor Away!")