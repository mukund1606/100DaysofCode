from art import logo
from os import system, name


def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


print(logo)
bidders_list = []
print("Welcome to the secret auction program.")
while True:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    bidders_list.append({"name": bidder_name, "amount": bid_amount})
    clear()
    if others == "no":
        break
highest_bid = bidders_list[0]
for bidder in bidders_list:
    if bidder["amount"] > highest_bid["amount"]:
        highest_bid = bidder
print(f'The winner is {highest_bid["name"]} with a bid of ${highest_bid["amount"]}.')
