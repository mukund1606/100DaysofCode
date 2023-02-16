print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
ch1 = input(
    "You're at a crossroad, where do you want to go? Type 'left' or 'right'.\n").lower()
if (ch1 == 'right'):
    print("You fell into the hole. Game Over.")
else:
    ch2 = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for the boat. Type \"swim\" to swim across.\n").lower()
    if (ch2 == "swim"):
        print("You got attacked by angry trout. Game Over")
    else:
        ch3 = input(
            "You arrived at island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which one do you prefer?\n").lower()
        if ch3 == "red":
            print("It's a room full of fire. Game Over")
        elif ch3 == "yellow":
            print("You found a tresure. You Win")
        elif ch3 == "blue":
            print("You entered room full of beasts. Game Over")
