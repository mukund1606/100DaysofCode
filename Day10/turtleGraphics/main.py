# Ways to import modules
# Basic import
# Ex. import turtle

# from module import class -> imports only the class
# Ex. from turtle import Turtle

# from module import * -> imports all classes
# Ex. from turtle import *

# Aliasing
# Ex. import turtle as t

# Installing external modules
# Ex. pip install heroes

import turtle as t
import random

tim = t.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# Challenge - 1, Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Challenge - 2, Draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# Challenge - 3, Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# Challenge - 4, Draw a random walk
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(500):
#     tim.forward(30)
#     tim.color(random.choice(colors))
#     tim.setheading(random.choice(directions))


# Python Tuple -> Immutable
# my_tuple = (1, 2, 3)
# print(my_tuple[0])

# t.colormode(255)
# tim.pensize(15)
# tim.speed("fastest")
# directions = [0, 90, 180, 270]
#
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# Challenge - 5, Draw a Spirograph
tim.speed("fastest")
t.colormode(255)


def draw_spirograph(step):
    for _ in range(int(360/step)):
        tim.color(random_color())
        tim.setheading(tim.heading() + step)
        tim.circle(100)


draw_spirograph(3)

screen = t.Screen()
screen.exitonclick()

