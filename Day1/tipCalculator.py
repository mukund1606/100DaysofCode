print("Welcome to the tip Calculator.")


bill = float(input("What was the total bill? $"))
tip_percent = int(
    input("What percentage tip would you like to give? 10, 12 or 15? "))
num_people = int(input("How many people to split the bill?"))

total = bill + tip_percent*bill/100
per_person = total/num_people

print(f"Each person should pay: ${round(per_person, 2)}")
