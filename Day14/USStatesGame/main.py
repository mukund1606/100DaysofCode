import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = list(data.state)

guessed_states = []
while True:
    answer_state = screen.textinput(
        f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    )
    if answer_state != None:
        answer_state = answer_state.title()
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame({"States To Learn": missing_states})
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        x_coor = int(data[data.state == answer_state].x)
        y_coor = int(data[data.state == answer_state].y)
        coordinates = (x_coor, y_coor)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(coordinates)
        t.write(answer_state)

# "states_to_learn.csv"
