alien_color=input('Alien Color: ')
alien_color=alien_color.strip().lower()
if alien_color == 'green':
    print('The Player Earned 5 Points!')
elif alien_color == 'yellow':
    print('The Player Earned 10 Points!')
elif alien_color == 'red':
    print('The Player Earned 15 Points!')
else:
    print('Please Try Again.')