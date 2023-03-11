"""

# List Comprehension

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

## String to List
name = "Mukund"
new_list = [letter for letter in name]
print(new_list)

## Range to List
print([num * 2 for num in range(1, 5)])

## Conditional List Comprehension
print([num * 2 for num in range(1, 5) if num % 2 == 0])


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)


# Squaring Numbers

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

squared_numbers = [num * num for num in numbers]

# Write your code 👆 above:

print(squared_numbers)


# Filtering Even Numbers

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:

result = [num for num in numbers if num % 2 == 0]

# Write your code 👆 above:

print(result)


# Data Overlap


# Write your code above 👆
file1_data = []
# with open("file1.txt") as file1:
#     file1_data = file1.readlines()

# file2_data = []
# with open("file2.txt") as file2:
#     file2_data = file2.readlines()

# file1_data = [int(num.strip()) for num in file1_data]
# file2_data = [int(num.strip()) for num in file2_data]

# result = [num for num in file1_data if num in file2_data]

# print(result)


# Dictionary Comprehension

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {
    student: score for (student, score) in student_scores.items() if score >= 33
}
print(passed_students)


# Dictionary Comprehension 2

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
words_list = sentence.split()

result = {word: len(word) for word in words_list}


print(result)

# Dictionary Comprehension 3
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}

# Write your code 👇 below:


print(weather_f)
"""

# Iterate over DataFrames

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through of a data frame

# for key, value in student_data_frame.items():
#     print(key)
#     print(value)


# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
