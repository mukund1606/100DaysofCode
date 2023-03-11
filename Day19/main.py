# FileNotFound

# with open("a-file.txt") as file:
#     file.read()


# KeyError

# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]


# IndexError

# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError

# text = "abc"
# print(text + 5)


# Catching Exceptions

# Try, Except, Else and Finally

"""
try:
    Something that might cause an exception
catch:
    Do this if there was an exception
else:
    Do this if there were no exceptions
finally:
    Do this no matter what happens


    
# FileNotFound
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "Value"}
    # print(a_dictionary["non-existent"])
    print(a_dictionary["key"])
# Using only except checks all errors but doesn't specify which error so we should use type of error as well
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
# Raising Exceptions -> raise


# FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "Value"}
#     # print(a_dictionary["non-existent"])
#     print(a_dictionary["key"])
# # Using only except checks all errors but doesn't specify which error so we should use type of error as well
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     raise TypeError("This is an error that I made up")


# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")

# bmi = weight / height**2
# print(bmi)


# Index Error Handling
fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)

facebook_posts = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 13, "Comments": 2, "Shares": 1},
    {"Likes": 33, "Comments": 8, "Shares": 3},
    {"Comments": 4, "Shares": 2},
    {"Comments": 1, "Shares": 1},
    {"Likes": 19, "Comments": 3},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        pass


print(total_likes)
"""

# JSON -> JavaScript Object Notation
# Write -> json.dump()
# Read -> json.load()
# Update -> json.update()
