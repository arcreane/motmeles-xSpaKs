from choose_difficulty import *
from set_gameboard import *


def play():
    difficulty = choose_difficulty()
    gameboard = set_random_gameboard(get_words(difficulty), set_gameboard_size(difficulty))


play()
