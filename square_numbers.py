squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
#concise code
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
#simple statistics with a list of numbers
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))