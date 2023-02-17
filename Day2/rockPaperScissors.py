rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
computer_choice = random.randint(0, 2)

print(choices[user_choice])
print("\n\nComputer Choose\n\n")
print(choices[computer_choice])


if user_choice == computer_choice:
    print("It's a Draw")
elif user_choice == 0:
    if computer_choice == 2:
        print("You Win")
    else:
        print("You Lose")
elif user_choice == 1:
    if computer_choice == 0:
        print("You Win")
    else:
        print("You Lose")
else:
    if computer_choice == 1:
        print("You Win")
    else:
        print("You Lose")