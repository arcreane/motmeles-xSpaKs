def print_gameboard(gameboard):
    print("      ", end="")
    for i in range(len(gameboard[0])):
        print(chr(i + 97), end="  ")
    print("", end="\n    ")
    for i in range(len(gameboard[0]) * 3):
        print("_", end="")
    print()
    for i in range(len(gameboard)):
        print("{0:2d}".format(i + 1), "|  ", end="")
        print("  ".join(gameboard[i]))
    print()


def print_remainingWords(remaining_words):
    print("List of remaining words : ", end="")
    for remaining_word in remaining_words:
        print(remaining_word, end="")
        if remaining_word != remaining_words[-1]:
            print(', ', end="")
    print("\n")


def print_foundWords(found_words):
    print("List of found words : ", end="")
    for remaining_word in found_words:
        print(remaining_word, end="")
        if remaining_word != found_words[-1]:
            print(', ', end="")
    print("\n")
