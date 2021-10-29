# %% Additional Exercise 6.2
""" Generate 50 salaries randomly within the range of 3000 to 6000 in list 
format. 
[hint: 
    import random
    x = random.randint(min, max)
    # generate a random number between min to max. ]
Next, create another list based on the random salaries from above to 
include salaries which are higher than 4500. Include dollar sign and 
thousand separator in the new list."""

import random
list = []
list_higherthan4500 = []
for i in range(50):
    x = random.randint(3000, 6000)
    list.append(x)
    if x > 4500:
        list_higherthan4500.append("${:,}".format(x))
print(list)
print(list_higherthan4500)

# %% Additional Exercise 6.3
"""
Create a new file called salaries_sample.csv. Make use of the csv module 
from python to write the previously constructed list to the csv file. 
"""
import csv

filename = "salaries_sample.csv"

file = open(filename,"w")
for i in list_higherthan4500:
    file.write(str(i)+"\n") #must convert to str as write argument not int
file.close()
