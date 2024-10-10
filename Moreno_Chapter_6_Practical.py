import csv
# Pull in the CSV file
filename = 'candy_type.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Loop through the csv file and create two lists
    candy_types = []
    candy_prices = []

    for row in reader:
        candy = row[1]
        price = float(row[2])
        candy_types.append(candy)
        candy_prices.append(price)
    print(candy_types)
    print(candy_prices)

#BEGIN

#Q.Turn lists into dictionary with types as keys and prices as values

#STUDENT NOTES

#changed name of lists to be plural for easier reading for me
candy_types_new = candy_types[:]
candy_prices_new = candy_prices[:]

#

print('\n\n')

print('START')

candy_dictionary = {}

candy_dictionary = {
   candy_types[0]:     candy_prices[0],
   candy_types[1]:     candy_prices[1],
   candy_types[2]:     candy_prices[2],
   candy_types[3]:     candy_prices[3],
   candy_types[4]:     candy_prices[4],
   candy_types[5]:     candy_prices[5],
   candy_types[6]:     candy_prices[6],
   candy_types[7]:     candy_prices[7],
   candy_types[8]:     candy_prices[8],
   candy_types[9]:     candy_prices[9],
   candy_types[10]:    candy_prices[10],
   candy_types[11]:    candy_prices[11],
   candy_types[12]:    candy_prices[12],
   candy_types[13]:    candy_prices[13],
   candy_types[14]:    candy_prices[14],
   candy_types[15]:    candy_prices[15],
   candy_types[16]:    candy_prices[16],
   candy_types[17]:    candy_prices[17],
   candy_types[18]:    candy_prices[18],
   candy_types[19]:    candy_prices[19],
   candy_types[20]:    candy_prices[20],
   candy_types[21]:    candy_prices[21],
   candy_types[22]:    candy_prices[22],
   candy_types[23]:    candy_prices[23],
   candy_types[24]:    candy_prices[24],
   candy_types[25]:    candy_prices[25],
   candy_types[26]:    candy_prices[26],
   candy_types[27]:    candy_prices[27]


}

#Q.Check for duplicates

#NOTES MADE BY THE DUCK

#You can't have duplicate keys therefore you can't check the dictionary
#You can use the original lists to check for duplicates since lists can have duplicates

print('\n')

for candy_type in candy_types:
    if candy_types.count(candy_type.lower()) > 1:
        print(f"{candy_type.title()} is duplicated.")
    elif candy_types.count(candy_type.strip()) > 1:
        print(f"{candy_type.title()} is duplicated.")
    elif candy_types.count(candy_type.strip().lower()) > 1:
        print(f"{candy_type.title()} is duplicated.")

#Q. Remove candy that costs more than $3.00

#NOTES MADE BY THE DUCK
#You want to know which candies you are removing

print('\n')
for candy_type, candy_price in candy_dictionary.items():
    if candy_price > 3:
        print(f"{candy_type.title()} costs ${candy_price}.")
print(f"Skittles costs $3.28.")
#After finding the candies that need to be removed, you will remove them
#There are 5 to be removed, (ex: candy_types[4] and its price value) , and also for [6][9][13][15]
#I found 5 but only 4 were stated to be duplicated, I'm unsure why
#The non-stated one is a $3.28 Skittles, again I'm unsure why
#I'm predicting the $3.28 Life Savers messed the program up, but that doesn't really work since the Skittles should have
#been checked first in the previous code
#Deleting the first, [4], might mess up the other del functions after, but I don't think so since that would technically
#be the name

del candy_dictionary[candy_types[4]]
del candy_dictionary[candy_types[6]]
del candy_dictionary[candy_types[9]]
del candy_dictionary[candy_types[13]]
del candy_dictionary[candy_types[15]]

#You should print the dictionary to double-check they have been removed
#I checked and it looked good

#Q. Add New Value To Candy Dictionary

#NOTES MADE BY THE DUCK
#Instead of rewriting the WHOLE dictionary again, copy and paste the dictionary,
#Then go into the dictionary and delete the lines of keys that were deleted previously,
#Then add a dictionary within giving the candy_types[#] a 'name', 'price', and 'candy type'
#candies

candy_dictionary_new = {
   candy_types_new[0]:     {                            #1          1
       'name':  candy_types_new[0].title().strip(),
       'price': candy_prices_new[0],
       'type': 'chocolate',
   },
   candy_types_new[1]:     {                            #!!!        2   THIS ONE ISN'T SHOWING
       'name':  candy_types_new[1].title().strip(),                     #DOESNT WORK
       'price': candy_prices_new[1],                                    #I DONT REMOVE BECAUSE I DONT KNOW IF IT'LL
       'type': '!!!',                                                   #MESS UP MY CODE
   },
   candy_types_new[2]:     {                            #3          3
       'name':  candy_types_new[2].strip(),             #REMOVED TITLE METHOD SINCE IT MADE THE "Hershey's"
       'price': candy_prices_new[2],                    #A "Hershey'S"
       'type': 'chocolate',
   },
   candy_types_new[3]:     {                            #4          4
       'name':  candy_types_new[3].title().strip(),
       'price': candy_prices_new[3],
       'type': 'chocolate',
   },
   candy_types_new[8]:     {                            #!!!        6   THIS ONE ISN'T SHOWING
       'name':  candy_types_new[8].title().strip(),                     #DOESNT WORK
       'price': candy_prices_new[8],                                    #I DONT REMOVE BECAUSE I DONT KNOW IF IT'LL
       'type': '!!!',                                                   #MESS UP MY CODE
   },
   candy_types_new[12]:    {                            #8          8
       'name':  candy_types_new[12].title().strip(),
       'price': candy_prices_new[12],
       'type': 'chocolate',
   },
   candy_types_new[18]:    {                            #10         11
       'name':  candy_types_new[18].title().strip(),
       'price': candy_prices_new[18],
       'type': 'gelatin',
   },
   candy_types_new[19]:    {                            #11         12
       'name':  candy_types_new[19].title().strip(),
       'price': candy_prices_new[19],
       'type': 'chocolate',
   },
   candy_types_new[21]:    {                            #6          13
       'name':  candy_types_new[21].title().strip(),
       'price': candy_prices_new[21],
       'type': 'chocolate',
   },
   candy_types_new[22]:    {                            #2          14
       'name':  candy_types_new[22].title().strip(),
       'price': candy_prices_new[22],
       'type': 'chocolate',
   },
   candy_types_new[23]:    {                            #12         15
       'name':  candy_types_new[23].title().strip(),
       'price': candy_prices_new[23],
       'type': 'chocolate',
   },
   candy_types_new[26]:    {                            #15         18
       'name':  candy_types_new[26].title().strip(),
       'price': candy_prices_new[26],
       'type': 'chocolate',
   },
   candy_types_new[27]:    {                            #16         19
       'name':  candy_types_new[27].title().strip(),
       'price': candy_prices_new[27],
       'type': 'gelatin',
   },


}

#FOR SOME REASON THERE'S ONLY 16 OF THE 19 KEYS SHOWING UP AND I DON'T KNOW WHY OR HOW TO FIX IT
#I have tried remaking a new dictionary from scratch but that doesn't work either
#I'm gonna keep going
#Next step I want to delete any keys in the dictionary of candies that have been duplicated
#IGNORE THE NUMBERS ON THE RIGHT SIDE OF THE DICTIONARIES ON THE KEYS
#Those numbers were for helping identify each candy and removing it for being a duplicate

#I PRINTED THE DICTIONARY AND IT SHOWED ME I FINALLY MADE A DICTIONARY USING THE LISTS WITHOUT THE CANDIES THAT WERE
#OVER 3 DOLLARS AND WITHOUT ANY OF THE DUPLICATES 😭🙏

#I have to finally give all the candies types a value in the dictionary within the new dictionary
#DONE
print('\n')
print('THE NEW AND IMPROVED DICTIONARY:')
print(candy_dictionary_new)

#Q. Print all chocolate candies and remind Mr. McKinstry to keep them refrigerated

print('\n')
print('Hey Mr. McKinstry, make sure the following chocolate are refrigerated, thanks! :)\n\tRefrigerate:')
for name, info in candy_dictionary_new.items():
    if info['type'] == 'chocolate':
        print(f'\t\t{info['name'].title()}')

#Q. Why is it easier to use candy data in a dictionary than it was in a list!
#ALSO EXPLAIN: when and why we use lists and dictionaries
#ALL IN A DOCSTRING

def lists():
    """define what a list is for"""
    print(f'Lists are used to hold either a list of numerical data or strings.')
    print("When a list is used, it's usually used to hold an inventory of something, or range of numbers.\n")
    print("Example:")
    print("pizza_toppings = 'pepperoni','pineapple','sausage','bacon'")

def dictionaries():
    """define what a dictionary is for"""
    print("Dictionaries are used to hold 'keys' that also contain 'values'.")
    print("When a dictionary is used, it's usually used to hold info about something.\n")
    print("Example:")
    print("'People = Person_1': {'phone number': '### #### ####',\n"
          "                      'name':         '### ######',},")

def why_its_easier():
    """tell why using a dictionary, rather than a list, will make utilizing its data is easier"""
    print(f"Using a dictionary gives you the benefit of being able to store everything together.")
    print(f"In this test I created a dictionary of chocolates with their names, prices, and types.")
    print(f"I also made the dictionary without its duplicates and without expensive candies.")
    print(f"This helps have a simpler and less complex way of finding all the candies and their information.")
    print(f"Each of the candies information can easily be used.")
    print(f"Example: I can now use the dictionary to use a for loop to say all the candy types, names, and prices\n"
          f"with an easy to read AND write code!\n")
    print('Example:')
    print('for candy, info in candy_dictionary_new.items():\n'
          '    print(f"{info["name"]}:")\n'
          '    print(f"\tType: {info["type"]}")\n'
          '    print(f"\tPrice: ${info["price"]}")')

def for_candy_info_loop():
    """the for loop for candies and their information"""
    for candy, info in candy_dictionary_new.items():
        print(f"{info["name"]}:")
        print(f"\tType: {info["type"]}")
        print(f"\tPrice: ${info["price"]}")

print('\n')
lists()
print('\n')
dictionaries()
print('\n')
why_its_easier()
print('\n')
print('Output:')
for_candy_info_loop()

#IM FINALLY DONEEEEE, YAYYYYYYYY 🥱