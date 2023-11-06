"""
Lost in a maze
Reeborg was exploring a dark maze and the battery in its flashlight ran out.
Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow
along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning
left as a last resort.

See
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
"""


def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    if wall_on_right() and front_is_clear():
        move()
    if not wall_on_right() and not front_is_clear():
        turn_right()
    else:
        if not at_goal():
            turn_left()
