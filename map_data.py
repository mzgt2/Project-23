import turtle
from states_data import States

class Map(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def write_state(self, answer_state):
        state = States(answer_state)
        self.goto(state.x_cor, state.y_cor)
        self.write(answer_state, align="center", font=("Arial", 8, "normal"))
