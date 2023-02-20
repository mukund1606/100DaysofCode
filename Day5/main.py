'''

# Funcitons with inputs
def greet():
    print("Hello World")

def greet_with_data(name):      ## Name is parameter
    print(f"Hello {name}")

greet_with_data("mukund")       ## Argument is Value

# Positional and Keyword Arguments

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# Positional
greet_with("Mukund", "India")
greet_with("India", "Mukund")

# Keyword Args
greet_with(name = "Mukund", location = "India")
greet_with(location = "India", name = "Mukund")
'''

