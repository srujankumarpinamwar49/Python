age = input("What is your current age? ")

int_age = int(age)
days = int_age * 365
days_left = (90*365) - days
weeks = int_age * 52
weeks_left = (90*52) - weeks
months = int_age * 12
months_left = (90*12) - months

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")



