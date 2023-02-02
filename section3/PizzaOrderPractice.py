print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

pizza = 0

if size == "S":
    pizza = 15
elif size == "M":
    pizza = 20
elif size == "L":
    pizza = 25
if add_pepperoni == 'Y':
    if size == 'S':
        pizza +=  2
    else:
        pizza +=  3
else:
    pizza = pizza
if extra_cheese == 'Y':
    pizza += 1

print(f"Your final bill is: ${pizza}.")
