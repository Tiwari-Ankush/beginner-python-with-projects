# predefined functions in hurdle
def turn_left():
    pass
def carries_object():
    pass
def is_facing_north():
    pass
def wall_on_right():
    pass
def move():
    pass
def front_is_clear():
    pass
def right_is_clear():
    pass
def at_goal():
    pass
def wall_in_front():
    pass

print("""
            ESCAPING THE MAZE
               CODE LOGIC
""")
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()