
from turtle import Turtle
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    STARTING_MOVE_DISTANCE = 5
    MOVE_INCREMENT = 5
    all_cars = []

    def move(self):
        for car in self.all_cars:
            car.backward(self.STARTING_MOVE_DISTANCE)

    def reset(self):
        for car in self.all_cars:
            car.hideturtle()
            car.clear()
        self.all_cars = []

    def speed_up(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT

    def level_up(self):
        self.reset()
        self.speed_up()

    def create_car(self):
        for car in self.all_cars:
            if car.xcor() < -300:
                self.all_cars.remove(car)
                car.hideturtle()
                car.clear()
        random_color = random.choice(colors)
        new_car = Turtle("square")
        new_car.color(random_color)
        new_car.penup()
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        self.all_cars.append(new_car)
