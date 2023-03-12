import random


def randomize_coordinates(gameboard, direction, word):
    if direction == "horizontal":
        x = random.randint(0, len(gameboard) - 1)
        y = random.randint(0, len(gameboard[0]) - 1 - len(word))
    elif direction == "vertical":
        x = random.randint(0, len(gameboard) - 1 - len(word))
        y = random.randint(0, len(gameboard[0]) - 1)

    return x, y


# Return 10 words from a list, depending on the difficulty
def get_words(difficulty):
    # Open the file and collect every word from the list
    with open("french_list.txt", "r") as f:
        words_list = [word.strip() for word in f.readlines()]

    # Get 10 unique words whose length depend on the difficulty
    words = []
    while len(words) < 10:

        word = random.choice(words_list)

        if difficulty == "1":
            if len(word) <= 4 and word not in words:
                words.append(word)

        elif difficulty == "2":
            if 4 <= len(word) <= 6 and word not in words:
                words.append(word)

        elif difficulty == "3":
            if 6 <= len(word) <= 9 and word not in words:
                words.append(word)

    return words


# Return a matrix whose size depends on the difficulty
def set_gameboard_size(difficulty):
    if difficulty == "1":
        a, b = 10, 5
    elif difficulty == "2":
        a, b = 15, 7
    elif difficulty == "3":
        a, b = 30, 15

    gameboard = [["_" for j in range(a)] for i in range(b)]

    return gameboard


# Add words to the gameboard
def set_random_gameboard(words, gameboard):
    remaining_words = words
    while len(remaining_words) != 0:
        word = remaining_words[0]

        # Randomize the direction of the word
        direction = random.choice(["horizontal", "vertical"])

        # Randomize coordinates of the word
        x, y = randomize_coordinates(gameboard, direction, word)[0], randomize_coordinates(gameboard, direction, word)[
            1]

        offset_x, offset_y = {"horizontal": (0, 1), "vertical": (1, 0)}[direction]

        temp_gameboard = gameboard
        remove = False
        i = 0

        # If every letter of the current word can be placed correctly, place it
        while not remove:
            for i in range(len(word)):

                if gameboard[x][y] == "_":
                    temp_gameboard[x][y] = word[i]



                    # If the last letter of the word can be placed, trigger the removal of the word
                    if i == len(word) - 1:
                        remove = True
                    else:
                        i += 1
                        x, y = x + offset_x, y + offset_y


                # If a letter of the word cannot be placed, try again with other coordinates
                else:
                    i = 0
                    x, y = randomize_coordinates(gameboard, direction, word)[0], \
                           randomize_coordinates(gameboard, direction, word)[
                               1]
                    remove = False
                    break

        # Once the word is certain to be correctly placed, remove it from words to place and update the gameboard
        remaining_words.remove(word)
        gameboard = temp_gameboard

    # Fill the grid with random letters
    for i in range(len(gameboard[0])):
        for j in range(len(gameboard)):
            if gameboard[j][i] == "_":
                #gameboard[j][i] = chr(random.randint(97, 122))
                pass
    return gameboard

