from choose_difficulty import *
from set_gameboard import *
from print import *


def play():
    difficulty = choose_difficulty()

    words = get_words(difficulty)
    remaining_words = words[:]
    found_words = []

    gameboard = set_random_gameboard(words, set_gameboard_size(difficulty))

    x_ids = [i.__str__() for i in range(1, len(gameboard) + 1)]
    y_ids = [chr(i + 97) for i in range(len(gameboard[0]))]
    print(y_ids)

    while len(remaining_words) != 0:

        print_gameboard(gameboard)
        print_remainingWords(remaining_words)

        line = input("Select line id : ")
        while line not in x_ids:
            line = input("Please select a valid line id : ")

        column = input("Select column id : ")
        while column not in y_ids:
            column = input("Please select a valid column id : ")

        direction = int(input("Select direction (0 for horizontal, 1 for vertical) : "))
        while direction != 1 and direction != 0:
            direction = int(input("Please select a valid direction (0 for horizontal, 1 for vertical) : "))

        x, y = int(line) - 1, ord(column) - 97

        print(x, y)


play()
