# Randomisation in Python
'''
# Module -> parts of code where each module is responsible for some functionality
import my_module
print(my_module.pi)

import random

random_integer = random.randint(1, 10)
print(random_integer)

0.000000 to 0.9999999
random_float = random.random()
print(random_float)

0.0000000 to 4.99999999
random_float_bw_0_and_5 = random.random()*5
print(random_float_bw_0_and_5)



# Python Lists
fruits = ["Apples", "Oranges", "Cherry"]

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine","Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# Index starts from 0
print(states_of_america[0])

# Negative Index
print(states_of_america[-1])

states_of_america[1] = "ABC"

# Append -> add at last
states_of_america.append("HAHAHA")

# Extend -> Add multiple items to list by using iterables
states_of_america.extend(["ABC", "DEF"])

# Insert -> Add at particular index
states_of_america.insert(5, "ABC")

# Remove -> Removes 1st Occurance Elements
states_of_america.remove("Hawaii")

# Pop -> Removes last element and returns last elem
last_elem = states_of_america.pop()

# Reverse -> Reverses the list
states_of_america.reverse()

print(states_of_america)
print(last_elem)


# List Errors
print(states_of_america[50])
# Traceback (most recent call last):
#   File "d:\100DaysofPython\Day 2\main.py", line 60, in <module>
#     print(states_of_america[50])
#           ~~~~~~~~~~~~~~~~~^^^^
# IndexError: list index out of range


# List inside List
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])


# Loops
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

# Mix and Max
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
print(min(student_scores))
print(max(student_scores))


# For loop with range function 
# range(initial, final, step) -> final not included
total = 0
for number in range(1, 101):
    total += number
print(total)
'''