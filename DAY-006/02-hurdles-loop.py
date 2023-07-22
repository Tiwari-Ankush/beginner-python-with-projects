
# hurdles loop challenge, move player to its destination >>
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


def turn_right():
    turn_left()
    turn_left()
    turn_left()

for block in range(1,14):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
