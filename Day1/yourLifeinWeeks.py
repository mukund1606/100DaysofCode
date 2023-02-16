age = input("What is your current age?\n")

age_as_int = int(age)

years_remain = 90 - age_as_int
days_remain = years_remain * 365
months_remain = years_remain * 12
weeks_remain = years_remain * 52

print(
    f"You have {days_remain} days, {weeks_remain} weeks, and {months_remain} months left.")
