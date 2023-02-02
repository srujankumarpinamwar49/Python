#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
total_bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12, or 15?"))
tip_percentage = 1 + (tip/100 )
total_persons = int(input("How many people to split the bill?"))
bill_per_person =round( (total_bill / total_persons) * tip_percentage,2)
print(f"Each person should pay: ${bill_per_person}")
