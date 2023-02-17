import random

names_string = input("Give me everybody's name, seperated by a comma. ")
names = names_string.split(", ")

# num_of_names = len(names)
# random_person = names[random.randint(0, num_of_names - 1)]

# With Choice Method
random_person = random.choice(names)
print(random_person, "is going to buy the meal.")