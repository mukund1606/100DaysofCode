# Higher Order Functions and Event Listeners
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(n1, n2, func):  # func is a function and calculator is a higher order function
    return func(n1, n2)


result = calculator(2, 3, multiply)
print(result)


# Inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print(f"{self.name} is moving in water.")


nemo = Fish("nemo")
nemo.swim()
nemo.breathe()
