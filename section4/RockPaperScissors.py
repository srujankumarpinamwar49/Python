import random

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

rps = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(rps[choice])

computer_chose = random.randint(0,2)
print("Computer chose: \n")
print(rps[computer_chose])

if  rps[choice] == rock:
    if rps[computer_chose] == scissors:
        print("Win")
    elif rps[computer_chose] == paper:
        print("loose")
    else:
        print("draw")
elif rps[choice] == paper:
    if rps[computer_chose] == rock:
        print("Win")
    elif rps[computer_chose] == scissors:
        print("loose")
    else:
        print("draw")
elif rps[choice] == scissors:
    if rps[computer_chose] == paper:
        print("Win")
    elif rps[computer_chose] == rock:
        print("loose")
    else:
        print("draw")

