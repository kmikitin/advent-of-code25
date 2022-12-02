from csv import reader
from enum import Enum

# (0 if you lost, 3 if the round was a draw, and 6 if you won)
class Score(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6


# (1 for Rock, 2 for Paper, and 3 for Scissors)
class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
results = {
    "A": {  # Rock
        "X": Score.DRAW.value + Shape.ROCK.value,  # Rock 4
        "Y": Score.WIN.value + Shape.PAPER.value,  # Paper 8
        "Z": Score.LOSE.value + Shape.SCISSORS.value,  # Scissors 3
    },
    "B": {  # Paper
        "X": Score.LOSE.value + Shape.ROCK.value,  # Rock 1
        "Y": Score.DRAW.value + Shape.PAPER.value,  # Paper 5
        "Z": Score.WIN.value + Shape.SCISSORS.value,  # Scissors 9
    },
    "C": {  # Scissors
        "X": Score.WIN.value + Shape.ROCK.value,  # Rock 7
        "Y": Score.LOSE.value + Shape.PAPER.value,  # Paper 2
        "Z": Score.DRAW.value + Shape.SCISSORS.value,  # Scissors 6
    },
}


with open("day_2_input.csv", "r") as csv_file:
    csv_reader = reader(csv_file)
    total_score = 0

    for row in csv_reader:
        opponent_throw, my_throw = row[0].split()
        result = results[opponent_throw][my_throw]
        total_score += result

    print(total_score)
