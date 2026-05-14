import turtle

import time
from map_data import Map
from states_data import States
from guess_data import Guesses
from timer import Countdown

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
timer = Countdown(screen, minutes=10)
timer.update()

map = Map()
guess = Guesses()
end_of_game = False

start_time = time.time()

answer_state = screen.textinput(title="Guess the State", prompt="What's a state's name?").title()
state = States(answer_state)
if answer_state in States.state_list:
    state = States(answer_state)

    if state.is_correct():
        map.write_state(answer_state)
        guess.duplicates(answer_state)


missed = []
while timer.time_left > 0:
    if timer.time_left > 0 and len(States.state_list) == len(guess.guessed):
        guess.win_game()
        time.sleep(10)
        break

    answer_state = screen.textinput(title=f"{guess.game_score}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state is None:
        break
    if answer_state == "Exit":
        if True:
            guess.missed_states()
        break

    if answer_state in States.state_list:
        state = States(answer_state)

        if state.is_correct():
            map.write_state(answer_state)
            guess.duplicates(answer_state)
    else:
        print("Invalid input - please enter a valid state name")
        continue
