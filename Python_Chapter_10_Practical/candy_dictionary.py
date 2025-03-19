# pip install pandas
# watch python data sources: reading & writing to Excel files - bryan
#                                                                                                   Cafferky
# installed something called pyxel instead of openpyxl, oops
# hopefully in doesn't affect anything later
    # reading pandas website to learn how to use pandas
# while trying to figure out how to use items() with an Excel file
# I learned that you can index through each row using the second
# part, v, since k just gave me 'time stamp', 'name', and 'whats your...',
# I ended up watching 'Python Pandas Tutorial ( Basics ) - Start Replacing
# Excel for Python 2021 Series' by Derrick Sherrill
# pip install xlwt

import pandas as pd
x = pd.read_excel(f"Candy_Request_Responses_1.xlsx")

x_v2 = x.copy()

# for k, v in x.items():
#     print(v)

# Names are 'Timestamp, dtype: datetime64[ns]',
# 'Name, dtype: object',
# 'What's your favorite candy?, dtype: object'

names = x['Name']
candies = x[f"What's your favorite candy?"]

orders={}

for name, candy in zip(names, candies):
    orders[str(name.lower().strip())] = str(candy.lower().strip())

print(orders)

ts = 0
ph = 52
while True:
    n = input(f"\n\n\n\nType New Responder's Name: ")
    c = input(f"Type New Responder's Candy: ")
    ts += 1
    ph += 1

    orders[n] = c

    new_row = [ts, n, c]

    x_v2.loc[ph] = new_row
    x_v2.sort_index()

    print(f"New Response Added\n")
    r = input(f"Would You Like To Add Another Responder? (yes/no)\n")
    if r == 'yes':
        continue
    if r == 'no':

        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html
        # I found out how to use pandas a little more in depth here

        x_v2.to_excel(f"new_candy_requests.xlsx",
                      sheet_name=f"requests")

        break

# for k, v in x_v2.items():
#     print(v)

# https://www.geeksforgeeks.org/python-find-keys-with-duplicate-values-in-dictionary/

pretty = {}

for k, v in orders.items():
    if v not in pretty:
        pretty[v] = k
    else:
        pretty[v] += f', {k}'

# This was method #2 of finding dup values of keys, I really liked this
# one from the website above, 'Using flipping dictionary'

for candy, names in pretty.items():
    print(f"{names.title()} want/s {candy.title()}.")