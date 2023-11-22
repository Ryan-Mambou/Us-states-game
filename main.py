from turtle import Screen, Turtle
from score_board import ScoreBoard
import pandas as pd

screen = Screen()
turtle = Turtle()
score_board = ScoreBoard()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []
missing_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{score_board.score}/50 States correct",
                              prompt="What's another state name ?").title()

    if answer == "Exit":
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
            new_data_frame = pd.DataFrame(missing_states, columns=["missing states"])
            new_data_frame.to_csv("missing_states.csv")
        break
    if answer in states:
        guessed_states.append(answer)
        score_board.increment_score()
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.hideturtle()
        x_coord = data[data["state"] == answer].x
        y_coord = data[data["state"] == answer].y
        print(x_coord, y_coord)
        t.goto(int(x_coord), int(y_coord))
        t.write(answer)

