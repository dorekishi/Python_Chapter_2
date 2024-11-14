from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


die_6 = Die()

roll = 0
while roll != 10:
    die_6.roll_die()
    roll += 1


die_10 = Die(10)
print('\n')

roll = 0
while roll != 10:
    die_10.roll_die()
    roll += 1


die_20 = Die(20)
print('\n')

roll = 0
while roll != 10:
    die_20.roll_die()
    roll += 1