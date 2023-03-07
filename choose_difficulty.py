def choose_difficulty():

    # Ask the player in what gamemode he wants to play
    difficulty = input("What difficulty do you want to choose ?\nType 1 for Easy (grid of 10*5, the words are 4 letters long or less)\nType 2 for Medium (grid of 15*7, the words are between 4 and 6 letters long)\nType 3 for Hard (grid of 30*15, the words are between 6 and 9 letters long)\n")

    # If the player types a wrong letter, ask to type again
    while difficulty != "1" and difficulty != "2" and difficulty != "3":
        print("Please choose a valid option")
        choose_difficulty()

    print("You have chosen to play in mode", difficulty)
    return difficulty



