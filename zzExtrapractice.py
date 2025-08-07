import turtle
from turtle import Turtle, Screen
import colorgram #library to extract colours from any picture
import random

turtle.colormode(255)

colors = colorgram.extract('spotpainting.jpg', 36) #You have to upload your image file into your project so that it can be accessible here
color_list = []
for color in colors:
    color_tuple = (color.rgb[0], color.rgb[1], color.rgb[2])
    color_list.append(color_tuple)

cursor = Turtle()
cursor.penup()

y_pos = -310

for _ in range(10):
    y_point += 50
    cursor.goto(-260, y_point)
    cursor.setheading(90)
    cursor.forward(50)
    for _ in range(10):
        cursor.dot(20, random.choice(color_list))
        cursor.penup()
        cursor.setheading(0)
        cursor.forward(50)

screen = Screen()
screen.exitonclick()



