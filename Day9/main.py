"""
# OOPS
# Classes and Objects
# Model Real World Entities
# What is has -> Attributes(Variables)
# What it does -> Methods(Functions)

# Class: A class is a blueprint for the object.
# Object: Object is an instance of a class.

# Constricting an Object

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")

# Move the turtle forward by 100 steps
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()


# Packages and Modules
# Module: A file containing a set of functions to include in your application.
# Package: A collection of modules.

import prettytable
# Installed and Imported prettytable

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table)

"""
