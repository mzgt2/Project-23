# Project-23

# U.S. States Guessing Game

An interactive Python game that challenges users to name all 50 U.S. states within a time limit using the Turtle graphics library.

---

## Features

- Interactive U.S. map using Turtle graphics
- Timed gameplay with countdown timer
- Tracks correct guesses
- Prevents duplicate scoring
- Displays guessed states directly on the map
- Exports missed states to a CSV file for studying
- Win condition when all 50 states are guessed

---

## Technologies Used

- Python 3
- Turtle Graphics
- Pandas
- Object-Oriented Programming (OOP)

---

## Project Structure

```bash
Project/
│
├── main.py
├── map_data.py
├── states_data.py
├── guess_data.py
├── timer.py
├── 50_states.csv
├── blank_states_img.gif
│
└── states_to_learn.csv   # Generated after exiting the game
```

---

## How the Game Works

1. The player is prompted to enter U.S. state names.
2. Correct guesses are:
   - displayed on the map
   - added to the score tracker
3. Incorrect guesses are ignored.
4. Duplicate guesses do not increase the score.
5. The game ends when:
   - all 50 states are guessed
   - the timer expires
   - the player types:
     ```text
     Exit
     ```
6. Any missed states are exported to:
   ```bash
   states_to_learn.csv
   ```

---

## Main Components

### main.py
Controls:
- game loop
- user input
- win/lose conditions
- timer integration

### states_data.py
Handles:
- loading state data from CSV
- validating state names
- retrieving map coordinates

### map_data.py
Responsible for:
- writing state names onto the map
- turtle positioning

### guess_data.py
Tracks:
- guessed states
- game score
- missed states
- CSV export for missed answers

### timer.py
Creates:
- countdown timer
- time-up display

---

## Required Files

### 50_states.csv

Must contain:

```csv
state,x,y
Alabama,139,-77
Alaska,-204,-166
...
```

### blank_states_img.gif

Blank U.S. map image used as the game background.

---

## How to Run

1. Install dependencies:

```bash
pip install pandas
```

2. Make sure all project files are in the same directory.

3. Run the game:

```bash
python main.py
```

---

## Example Gameplay

```text
Guess the State: Florida
```

Correct guesses appear on the map.

To quit early:

```text
Exit
```

---

## Concepts Practiced

- Object-Oriented Programming
- Classes and Objects
- File Handling
- CSV Data Processing
- Turtle Graphics
- Timers and Event Handling
- Game Logic
- Data Validation

---

## Future Improvements

- Add difficulty levels
- Add sound effects
- Add score leaderboard
- Add hints system
- Improve UI styling
- Add multiplayer mode

---

