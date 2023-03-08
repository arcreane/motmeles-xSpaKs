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
        gameboard = [["_" for j in range(10)] for i in range(5)]
    elif difficulty == "2":
        gameboard = [["_" for j in range(15)] for i in range(7)]
    elif difficulty == "3":
        gameboard = [["_" for j in range(30)] for i in range(15)]

    return gameboard


# Add words the the gameboard
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

        while word in remaining_words:

            # Check if every letter of the word can be placed correctly

            # If every letter can be placed correctly, do it
            for letter in word:
                gameboard[x][y] = letter
                x, y = x + offset_x, y + offset_y
            remaining_words.remove(word)

        # Fill the grid with random letters
        for i in range(len(gameboard[0])):
            for j in range(len(gameboard)):
                if gameboard[j][i] == "_":
                    # gameboard[j][i] = chr(random.randint(97, 122))
                    pass

    for line in gameboard:
        print(" ".join(line))
