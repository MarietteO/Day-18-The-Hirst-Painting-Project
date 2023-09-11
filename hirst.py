from turtle import Turtle, Screen
import random

screen = Screen()
screen.screensize(400, 400)
screen.colormode(255)
screen.tracer(0)

colour_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
               (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
               (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186),
               (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82),
               (46, 73, 62), (47, 66, 82)]


def draw_new_circle():
    random_colour = random.choice(colour_list)
    turtle = Turtle("circle")
    turtle.color(random_colour)
    turtle.penup()
    return turtle


y_pos = -260
for _ in range(10):
    num = 0
    y_pos += 60 # Increase the y position for the next row
    x_pos = -280 # Reset the x position for each row
    screen.update()
    for _ in range(10):
        draw_new_circle().setposition(x_pos+(60*num), y_pos)
        num += 1

screen.exitonclick()
