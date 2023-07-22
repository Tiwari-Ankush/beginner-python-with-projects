
print("""
Move gift to destination 

    |           |           |       |      
    |       |   |           |       |      
🎁_ | _ | _ | _ | _ _ | _ _ | _ _ _ |🚩 

""")
# use while loop and functions

# there is some inbuilt conditions in the  reeborgs hudle world
'''
at_goal()
front_is_clear()
right_is_clear()
wall_in_front()
wall_on_right()
object_here()
carries_object()
is_facing_north()

'''

# code >>
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

# actual code >>
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
        turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

   
   
