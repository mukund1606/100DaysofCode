# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

# Solution

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:  # or was used instead of and
        print("FizzBuzz")
    # if was used instead of elif
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)  # List was used to print the number
