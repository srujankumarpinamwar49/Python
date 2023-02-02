print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


turn = input('You are at a cross road. where do you want to go? Type "left" or "Right"').lower()
print(turn)

if turn == 'left':
    wait_or_swim = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if wait_or_swim == 'wait':
        color = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?').lower()
        if color == 'yellow':
            print('You found the treasure! You Win!')
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")   
