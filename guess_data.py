from states_data import States
import pandas
from turtle import Turtle

class Guesses:
    def __init__(self):
        self.guessed = []
        self.game_score = 0
        self.missed = []


    def duplicates(self, answer_state):
        state = States(answer_state)
        if state.is_correct() and answer_state not in self.guessed:
            self.guessed.append(answer_state)
            self.game_score += 1

    def missed_states(self):
        for item in States.state_list:
            if item not in self.guessed:
                self.missed.append(item)
        missed_data = pandas.DataFrame(self.missed)
        missed_data.to_csv("states_to_learn.csv")

    def win_game(self):
           turtle = Turtle()
           turtle.penup()
           turtle.color("black")
           turtle.hideturtle()
           turtle.goto(0,0)
           turtle.write("You win!", align="center", font=("Arial", 24, "bold"))
