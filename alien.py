alien_0 = {'color' : 'green', 'points' : 5}

print(alien_0['color'])          #green
print(alien_0['points'])         #5

new_points = alien_0['points']
print(f"You just earned {new_points} points!")  #You just earned 5 points!

print(alien_0)                   #{'color': 'green', 'points': 5}

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)                   #{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

alien_0 = {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)          #{'color': 'green', 'points': 5}

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")  #The alien is green.

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")  #The alien is now yellow.

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print(f"Original position: {alien_0['x_position']}")

    # Move the alien to the right.
    # Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:                                   # This must be a fast alien.
    x_increment = 3

    # The new position is the old position plus the increment.

alien_0['x_position'] = alien_0['x_position'] + x_increment         #Original position: 0
print(f"New position: {alien_0['x_position']}")                     #New position: 2

alien_0['speed'] = 'fast'

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)                                                      #{'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0)                                                      #{'color': 'green'}