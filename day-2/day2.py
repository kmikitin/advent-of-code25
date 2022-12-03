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
results_part_1 = {
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

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
results_part_2 = {
    "A": {  # Rock
        "X": Score.LOSE.value + Shape.SCISSORS.value,  # Lose 3
        "Y": Score.DRAW.value + Shape.ROCK.value,  # Draw 4
        "Z": Score.WIN.value + Shape.PAPER.value,  # Win 8
    },
    "B": {  # Paper
        "X": Score.LOSE.value + Shape.ROCK.value,  # Lose 1
        "Y": Score.DRAW.value + Shape.PAPER.value,  # Draw 5
        "Z": Score.WIN.value + Shape.SCISSORS.value,  # Win 9
    },
    "C": {  # Scissors
        "X": Score.LOSE.value + Shape.PAPER.value,  # Lose 2
        "Y": Score.DRAW.value + Shape.SCISSORS.value,  # Draw 6
        "Z": Score.WIN.value + Shape.ROCK.value,  # Win 7
    },
}


with open("day_2_input.csv", "r") as csv_file:
    total_score = 0

    for row in reader(csv_file):
        opponent_throw, outcome = row[0].split()
        result = results_part_2[opponent_throw][outcome]
        total_score += result

    print(total_score)
