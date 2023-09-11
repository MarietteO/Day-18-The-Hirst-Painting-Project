from turtle import Turtle, Screen
import random

screen = Screen()
screen.screensize(400, 400)
screen.colormode(255)
screen.tracer(0)

colour_list = [(26, 27, 20), (90, 87, 80), (27, 30, 27), (41, 42, 46), (35, 32, 34), (80, 80, 87),
             (162, 158, 153), (91, 87, 90), (68, 68, 51), (160, 155, 158), (75, 78, 75), (61, 61, 69),
             (152, 150, 156), (66, 61, 65), (133, 130, 117), (61, 66, 61),
             (126, 124, 134), (152, 154, 152), (68, 62, 60), (131, 125, 129), (196, 193, 183), (133, 125, 124),
             (197, 189, 187), (195, 189, 192), (60, 65, 66), (191, 189, 197)]

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
