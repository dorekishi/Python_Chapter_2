alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
    #print(alien)

aliens = []

for alien_number in range(30):              #make 30 aliens !!!!!!!!!!!!!!!!!!!!!!!!!!
    new_alien = {
        'color':        'green',
        'points':       5,
        'speed':        'slow'
    }
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':        #if there are any yellow aliens before the start of the if-elif chain,
        alien['color'] = 'red'              #they will turn red, since it's only elif
        alien['speed'] = 'fast'             #if you used if instead it would turn the yellow aliens, that were turned
        alien['points'] = 15                #from green, into red too

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")

