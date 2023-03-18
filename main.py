from set_gameboard import *
from print import *
from get_user_input import *
from check_word import *


def menu(difficulty="0"):
    option = input("\033[1;97m\nWhat do you want to do ?\n1 : Play a game\n2 : Options\n")

    while option != "1" and option != "2":
        print("\033[1;91m\nPlease select a valid option\033[1;97m")
        option = input("\nWhat do you want to do ?\n1 : Play a game\n2 : Options\n")

    if option == "1":
        if difficulty != "1" and difficulty != "2" and difficulty != "3":
            print("\033[1;91m\nPlease select a difficulty in the options\033[1;97m")
            menu(difficulty)
        else:
            play(difficulty)
    elif option == "2":
        options(difficulty)


def options(difficulty):
    option = input("\nWhat option do you want to select ?\n1 : Choose difficulty\n2 : Exit options\n")

    while option != "1" and option != "2":
        print("\033[1;91m\nPlease select a valid option\033[1;97m")
        option = input("\nWhat option do you want to select ?\n1 : Choose difficulty\n2 : Exit options\n")

    if option == "1":
        difficulty = choose_difficulty()
        options(difficulty)

    elif option == "2":
        menu(difficulty)


def play(difficulty):
    print("\n\033[1;32mYou have started a game in difficulty mode", difficulty, "\033[1;97m\n")
    words = get_words(difficulty)
    remaining_words = words[:]
    found_words = []

    gameboard = set_random_gameboard(words, set_gameboard_size(difficulty))

    x_ids = [i.__str__() for i in range(1, len(gameboard) + 1)]
    y_ids = [chr(i + 97) for i in range(len(gameboard[0]))]

    while len(remaining_words) != 0:

        print_game(gameboard, remaining_words, found_words)

        user_input = get_user_input(remaining_words, x_ids, y_ids)
        word_attempt, line, column, direction = user_input[0], user_input[1], user_input[2], user_input[3]

        x, y = int(line) - 1, ord(column) - 97

        if check_word(gameboard, x, y, word_attempt, direction):
            remaining_words.remove(word_attempt)
            found_words.append(word_attempt)
            print("\033[1;32m\nWell done ! You found a word\n\033[1;97m")

            # If a word is found, change the color in the grid
            spot_word(gameboard, word_attempt, x, y, direction)
        else:
            print("\033[1;91m\nUnfortunate ! You did not find a word\n\033[1;97m")

    game_over()


def game_over():
    name = input("\033[1;32mCongratulations, you managed to find every word ! How can we call you ?\033[1;97m\n")
    print("\033[1;32mYou will be remembered as a legend,", name, "!\033[1;97m")


menu()
