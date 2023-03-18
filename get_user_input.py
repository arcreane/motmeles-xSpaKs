# Ask the word to be found informations to the player
def get_user_input(remaining_words, x_ids, y_ids):
    word_attempt = input("Select what word you found : ")
    while word_attempt not in remaining_words:
        word_attempt = input("Please select a valid word : ")

    line = input("Select line id : ")
    while line not in x_ids:
        line = input("Please select a valid line id : ")

    column = input("Select column id : ")
    while column not in y_ids:
        column = input("Please select a valid column id : ")

    direction = int(input("Select direction (0 for horizontal, 1 for vertical) : "))
    while direction != 1 and direction != 0:
        direction = int(input("Please select a valid direction (0 for horizontal, 1 for vertical) : "))

    return word_attempt, line, column, direction


# Ask the player what difficulty he wants to play in
def choose_difficulty():
    # Ask the player in what gamemode he wants to play
    difficulty = input("\nWhat difficulty do you want to choose ?\nType 1 for Easy (grid of 10*5, the words are 4 "
                       "letters long or less)\nType 2 for Medium (grid of 15*7, the words are between 4 and 6 letters "
                       "long)\nType 3 for Hard (grid of 30*15, the words are between 6 and 9 letters long)\n")

    # If the player types a wrong letter, ask to type again
    while difficulty != "1" and difficulty != "2" and difficulty != "3":
        print("\033[1;91m \nPlease choose a valid option", end="\n\033[1;97m")
        difficulty = input("\nWhat difficulty do you want to choose ?\nType 1 for Easy (grid of 10*5, the words are 4 "
                           "letters long or less)\nType 2 for Medium (grid of 15*7, the words are between 4 and 6 letters "
                           "long)\nType 3 for Hard (grid of 30*15, the words are between 6 and 9 letters long)\n")

    print("\033[1;32m\nYou have chosen to play in mode", difficulty, "\033[1;97m")
    return difficulty
