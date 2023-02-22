"""

# Global Scope
player_health = 100


def game():
    # Local Scope
    player_health = 10
    print("Inside of game function")
    print(player_health)

    def drink_potion():
        # Local Scope
        player_health = 20
        print("Inside of drink_potion function")
        print(player_health)


drink_potion()
game()
print("Outside of game function")
print(player_health)


# No block scope

if player_health > 0:
    player_strength = 100
    print("Player is alive")

print(player_strength)


# How to use global scope

player_health = 100


def game():
    global player_health
    player_health = 10
    print("Inside of game function")
    print(player_health)

    def drink_potion():
        global player_health
        player_health = 20
        print("Inside of drink_potion function")
        print(player_health)

    drink_potion()


game()
print("Outside of game function")
print(player_health)


# Not a good practice to use global scope

# Use this instead

enemies = 1


def increase_enemies():
    print(f"Enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")

# Global Constants
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

## Any variable that is all caps is a global constant

"""
