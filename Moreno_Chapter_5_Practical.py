import csv          # Pull in the CSV file

filename = 'candy_type.csv'     #variable=str

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
                                                              # Loop through the csv file and create two lists
    candy_types = []                                           #names of candies
    candy_prices = []                                          #numerical price of candy

    for row in reader:
        candy = row[1]
        price = float(row[2])                                 #set numbers to float
        candy_types.append(candy)
        candy_prices.append(price)
    print(candy_types)                 #preserved
    print(candy_prices)                #preserved

#

print('\n PRACTICAL BEGINS BELOW \n')

#       Begin Practical
#Using the file provided by Mr. McKinstry (change the name to reflect your name) take the two lists that are created
#from the file and sort the list in Alphabetical order (I recommend not changing the list)

#            STUDENT NOTES
#I made new copied lists of the old lists that I can preserve the old list AND if someone wanted to add ANOTHER candy
#                                       they can add it to that one without a care where they add it in the list
#I made all the candies lower case so it filters better

print('\n\n')

sorted_candy_types = [candy.lower() for candy in candy_types]
sorted_candy_types = sorted(sorted_candy_types)
print(sorted_candy_types)

sorted_candy_prices = sorted(candy_prices)
print(sorted_candy_prices)

#Then check for duplicate candy names in the list and print duplicate candy types in a statement.
#For example, Snickers has been duplicated.

#             STUDENT NOTES
#since the code to declare duplicates removes them once they're found, I create a new copied and expendable list
#                                                                             of sorted_candy_types list
#I also changed the names of the lists from the original code given since it made it hard to read what I was writing
#Added .strip() to filter better for example there was a Snickers in the list with a whitespace and there was more than
#one snickers WITHOUT whitespaces BUT if there wasn't more than one the program wouldn't of told me

print('\n\n')

sorted_candy_types_duplicate_reduction_list=sorted_candy_types[:]

for candy_type in sorted_candy_types_duplicate_reduction_list:
    if sorted_candy_types_duplicate_reduction_list.count(candy_type.strip()) > 1:
        print(f"{candy_type.title()} has been duplicated.")
        sorted_candy_types_duplicate_reduction_list.remove(candy_type)

#Take the last 5 items in each list and print out that the candy costs this much at Walmart.com.

#      STUDENT NOTES
#Since this is asking for the last 5 items from each list and to match it with its price, I think the question is
#asking for the preserved lists, candy_types and candy_prices, to be used for this
#used ANOTHER list so it ALWAYS uses the last five candies in case more candies and prices are added to the lists

print('\n\n')

last_five_candy_types_in_preserved_list=candy_types[-5:]
last_five_candy_prices_in_preserved_list=candy_prices[-5:]

print(f"{last_five_candy_types_in_preserved_list[0].strip().title()} costs ${last_five_candy_prices_in_preserved_list[0]
} at Walmart.com.")
print(f"{last_five_candy_types_in_preserved_list[1].strip().title()} costs ${last_five_candy_prices_in_preserved_list[1]
} at Walmart.com.")
print(f"{last_five_candy_types_in_preserved_list[2].strip().title()} costs ${last_five_candy_prices_in_preserved_list[2]
} at Walmart.com.")
print(f"{last_five_candy_types_in_preserved_list[3].strip().title()} costs ${last_five_candy_prices_in_preserved_list[3]
} at Walmart.com.")
print(f"{last_five_candy_types_in_preserved_list[4].strip().title()} costs ${last_five_candy_prices_in_preserved_list[4]
} at Walmart.com.")

#Finally sum the entire (full) price list

print('\n\n')

print(f"The sum of the price list is ${sum(candy_prices)}")

#Use the price list to count the number of different candies that are more than $3.00
#then remove them from the price list. Print this list to show that all the candy costs over $3.00 have been removed.
#       STUDENT NOTES
#I have to make a new copied list of candy_prices
#Count the amount of prices that are greater than $3.00
#           which means I have to make ANOTHER list so the prices OVER $3.00 can be counted
#Then I have to remove them
#Then print the new list with prices that are at a maximum of $3.00
#new list name is candy_prices_with_three_dollar_maximum
#I made 2 statements for each list to be extra and for 'funzies'

print('\n\n')

candy_prices_with_three_dollar_maximum = candy_prices[:]
candy_prices_over_three_dollars = []

for candy_price in candy_prices_with_three_dollar_maximum:
    if candy_price > 3:
        candy_prices_over_three_dollars.append(candy_price)
        candy_prices_with_three_dollar_maximum.remove(candy_price)

print(f"There are {len(candy_prices_over_three_dollars)} candies with prices over $3.00.")
print(f"The candy's prices are:")
print(candy_prices_over_three_dollars)

print('\n\n')

print(f"There are {len(candy_prices_with_three_dollar_maximum)} candies with prices over $3.00 or under.")
print(f"All the candy's with prices, $3.00 or under are:")
print(candy_prices_with_three_dollar_maximum)


#Finally sum the new price list
#       STUDENT NOTES
# All I should have to do is print the sum of the numbers in candy_prices_with_three_dollar_maximum

print('\n\n')

print(f"The sum of the new candy list is ${sum(candy_prices_with_three_dollar_maximum)}.")







#some of the code I messed around with to help me solve some of my issues and to better understand
print('\n\nCODE I PLAYED WITH TO HELP ME SOLVE THE PROBLEMS BELOW\n\n')

my_list = [1, 2, 3, 2, 4, 5]
element_to_check = 2

if my_list.count(element_to_check) > 1:
    print(f"The element {element_to_check} appears more than once.")
else:
    print(f"The element {element_to_check} does not appear more than once.")

print(f"{candy_types[27].strip().title()} costs ${candy_prices[27]} at Walmart.com.")
print(f"{candy_types[26].strip().title()} costs ${candy_prices[26]} at Walmart.com.")
print(f"{candy_types[25].strip().title()} costs ${candy_prices[25]} at Walmart.com.")
print(f"{candy_types[24].strip().title()} costs ${candy_prices[24]} at Walmart.com.")
print(f"{candy_types[23].strip().title()} costs ${candy_prices[23]} at Walmart.com.")