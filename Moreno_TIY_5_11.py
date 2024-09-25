the_list=list(range(1,10))
#print(the_list) # [1, . . ., 9]
for number in the_list:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f"{number}th")