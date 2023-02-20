def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
def moveup():
    turn_left()
    move()
    turn_right()
    if wall_in_front():
        moveup()
    else:   
        movedown()
        
def movedown():
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        moveup()
    else:
        move() 
