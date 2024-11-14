from random import choice

lot = [number for number in range(1,11)]
word = 'words'
words = [letter for letter in word]
for letter in words:
    lot.append(letter)

winning_numbers = f"{choice(lot)}{choice(lot)}{choice(lot)}{choice(lot)}"
print(f"Winners: {winning_numbers}")
print(f"Whoever has the four characters together as shown, wins a prize!")