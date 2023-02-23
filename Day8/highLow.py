from art import logo, vs
from game_data import data
import random


def clear():
    print("\033c", end="")


print(logo)
score = 0
game_should_continue = True
item1 = random.choice(data)
item2 = random.choice(data)
if item1 == item2:
    while item1 == item2:
        item2 = random.choice(data)


def compare(item1, item2):
    if item1["follower_count"] > item2["follower_count"]:
        return "a"
    else:
        return "b"


while game_should_continue:
    print(
        f"Compare A: {item1['name']}, a {item1['description']}, from {item1['country']}."
    )
    print(vs)
    print(
        f"Against B: {item2['name']}, a {item2['description']}, from {item2['country']}."
    )
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == compare(item1, item2):
        clear()
        print(logo)
        score += 1
        print(f"You're right! Current score: {score}.")
        item1 = item2
        item2 = random.choice(data)
        if item1 == item2:
            while item1 == item2:
                item2 = random.choice(data)
    else:
        clear()
        print(logo)
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
