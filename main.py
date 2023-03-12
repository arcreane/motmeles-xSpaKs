from choose_difficulty import *
from set_gameboard import *
from print import *
from get_user_input import *


def menu(difficulty):
    difficulty = "2"
    option = int(input("\033[1;97m\nWhat do you want to do ?\n1 : Play a game\n2 : Options\n3 : \n"))

    while option != 1 and option != 2:
        print("\nPlease select a valid option")
        option = int(input("\nWhat do you want to do ?\n1 : Play a game\n2 : Options\n3 : \n"))

    if option == 1:
        if difficulty != "1" and difficulty != "2" and difficulty != "3":
            print("\033[1;91m\nPlease select a difficulty in the options\033[1;97m")
            menu(difficulty)
        else:
            play(difficulty)
    elif option == 2:
        options(difficulty)
    else:
        pass


def options(difficulty):
    option = int(input("\nWhat option do you want to select ?\n1 : Choose difficulty\n2 : Exit options\n3 : \n"))

    while option != 1 and option != 2:
        print("\033[1;91m\nPlease select a valid option\033[1;97m")
        option = int(input("\nWhat option do you want to select ?\n1 : Choose difficulty\n2 : Exit options\n3 : \n"))

    if option == 1:
        difficulty = choose_difficulty()
        options(difficulty)

    elif option == 2:
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
        x_temp, y_temp = x, y

        for i in range(len(word_attempt)):
            if word_attempt[i] == gameboard[x_temp][y_temp]:
                if i == len(word_attempt) - 1:
                    remaining_words.remove(word_attempt)
                    found_words.append(word_attempt)
                    print("\033[1;32m\nWell done ! You found a word\n\033[1;97m")
                    x_temp, y_temp = x, y

                    # If a word is found, change the color in the grid
                    for j in range(len(word_attempt)):
                        gameboard[x_temp][y_temp] = "\033[1;32m" + gameboard[x_temp][y_temp] + "\033[1;97m"
                        if direction == 0:
                            y_temp += 1
                        elif direction == 1:
                            x_temp += 1

                else:
                    if direction == 0:
                        y_temp += 1
                    elif direction == 1:
                        x_temp += 1
            else:
                print("\n\033[1;91mUnfortunate ! You did not find a word\033[1;97m\n")
                break

    name = input("\033[1;32mCongratulations, you managed to find every word ! How can we call you ?\n\033[1;97m")
    print("\033[1;32mYou will be remembered as a legend,", name, "!\033[1;97m")


menu(0)
