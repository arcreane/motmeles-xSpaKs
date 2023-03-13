def check_word(gameboard, x, y, word_attempt, direction):
    x_temp, y_temp = x, y

    for i in range(len(word_attempt)):
        if word_attempt[i] == gameboard[x_temp][y_temp]:
            if i == len(word_attempt) - 1:
                return True

            else:
                if direction == 0:
                    y_temp += 1
                elif direction == 1:
                    x_temp += 1
        else:
            return False


def spot_word(gameboard, word, x, y, direction):
    for j in range(len(word)):
        gameboard[x][y] = "\033[1;32m" + gameboard[x][y] + "\033[1;97m"
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
