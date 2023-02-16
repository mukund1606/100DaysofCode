# Input, Output, Variables

'''print("Hello World!")
name = input("What is your name:")
print("Hello " + name)
print(len(name))


a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

# Datatypes, Numbers, Operations, Type Conversion, f-Strings

# Strings

print("Hello"[2])
print("123"+"345")

# Integers
12548
123_456_789
print(123 + 453)


# Float

3.14159

# Boolean

True
False


# Len function and type conversion

num_char = len(input("What is your name?"))
print(type(num_char))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
'''

# Formatted Strings

greet = "YOOOO"
print(f'Hey this is formatted string {greet}')


# Operators
'''
+
-
*
/
//
**

PEDMAS
()
**
/ *
+ -


// Floor Division -> returns int value 

# Round Function

num = 12.3466
print(round(num, 2))
print(round(num, 3))
print(round(num, 1))

# Comparison Operators

==  -> Equal to
!=  -> Not Equal to
>   -> Greater Than
<   -> Less Than
>=  -> Greater Than or Equal to
<=  -> Less Than or Equal to

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the rollercoaser.")
else:
    print("Sorry, you can't ride the rollercoaster.")


# Modulo Operator
% -> Gives Remainder
number = int(input("Enter any Number:"))
if (number % 2 == 0):
    print("Even")
else:
    print("Odd")



# Nested if else
height = int(input("What is your height in cm? "))
if height > 120:
    age = int(input("What is your age? "))
    if (age < 12):
        print("Pay $5")
    elif age <= 18:
        print("Pay $7")
    else:
        print("Pay $15")
else:
    print("Sorry, you can't ride the rollercoaster.")

'''
