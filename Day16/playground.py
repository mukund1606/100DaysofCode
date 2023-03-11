# Advanced Python Arguments


# Arguments with default values
# def my_function(a=1, b=2, c=3):
#     print(a, b, c)


# my_function(10, 20, 30)
# my_function(b=20, c=30)
# my_function(b=30)
# my_function()

## *args -> Tuple


def add(*args: int) -> int:
    total = 0
    for n in args:
        total += n
    return total


# print(add(1, 2, 3, 4))

## **kwargs -> Dictionary


def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")  # get method returns None if key doesn't exist


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)
