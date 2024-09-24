#Testing equality and inequality with strings
igloos='cold'
print("Is 'igloos==hot' ? I predict false.")
print(igloos=='hot')

print("\nIs 'igloos==cold' ? I predict true.")
print(igloos=='cold')
#Testing using the lower() method
person='MiGuEl'
print("\nIs 'person.upper()==miguel' ? I predict false.")
print(f'{person.upper()=='miguel'}')

print("\nIs 'person.lower()==miguel' ? I predict true.")
print(f'{person.lower()=='miguel'}')
#Numerical testing involving equality and inequality, greater than and less than,
#greater than or equal to, and less or equal to
number=7
print("\nIs 'number==7' ? I predict true.")
print(number==7)

print("\nIs 'number==3' ? I predict false.")
print(number==3)

print("\nIs 'number>6' ? I predict true.")
print(number>6)

print("\nIs 'number<3' ? I predict false.")
print(number<3)

print("\nIs 'number>=6' ? I predict true.")
print(number>=6)

print("\nIs 'number<=3' ? I predict false.")
print(number<=3)
#Testing using the 'and' keyword and the 'or' keyword
print("\nIs '(number>4) and (number<8)' ? I predict true.")
print((number>4) and (number<8))

print("\nIs '(number>=4) and (number<=4)' ? I predict false.")
print((number>=4) and (number<=4))

print("\nIs '(number>4) or (number<6)' ? I predict true.")
print((number>4) or (number<6))

print("\nIs '(number>=8) or (number<=4)' ? I predict false.")
print((number>=8) or (number<=4))
#Testing whether an item is in a list
brands=['rick owen',
        'balenciaga']

print("\nIs 'ed hardy in brands' ? I predict false.")
print('ed hardy' in brands)

print("\nIs balenciaga in brands ? I predict true.")
print('balenciaga' in brands)
#Testing whether an item is not in a list
print("\nIs 'ed hardy not in brands' ? I predict true.")
brand='ed hardy'
if brand not in brands:
    print(True)
if brand in brands:
    print(False)

print("\nIs 'balenciaga not in brands' ? I predict false.")
brand='balenciaga'
if brand not in brands:
    print(True)
if brand in brands:
    print(False)