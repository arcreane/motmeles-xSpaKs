from choose_difficulty import *
from set_gameboard import *


def play():
    difficulty = choose_difficulty()
    remaining_words = get_words(difficulty)
    gameboard = set_random_gameboard(remaining_words, set_gameboard_size(difficulty))


play()
