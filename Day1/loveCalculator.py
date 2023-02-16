print("Welcome to Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


combined_name = name1 + name2

t = combined_name.lower().count('t')
r = combined_name.lower().count('r')
u = combined_name.lower().count('u')
e = combined_name.lower().count('e')
true = t + r + u + e

l = combined_name.lower().count('l')
o = combined_name.lower().count('o')
v = combined_name.lower().count('v')
e = combined_name.lower().count('e')
love = l + o + v + e

print(f"Your Love Score is {str(true) + str(love)}")
