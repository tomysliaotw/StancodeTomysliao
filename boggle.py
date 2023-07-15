# import time
import copy

'''
Global variables that's outside of Recursive Routines
to save memory
'''
FILE = 'dictionary.txt'
LEVEL_LIMIT = 6


class Remember:
    def __init__(self):
        self.wordList = set()

    def append(self, word):
        if word not in self.wordList:
            print("Found:" + word)
            self.wordList.add(word)

    def total(self):
        print("There are " + str(len(self.wordList)) + " words in total")


def main():
    # matrix1 = [['a', 'f', 't', 'r'],  # input('L1:').split(' ')
    #           ["b", "e", "a", "s"],  # input('L2:').split(' ')
    #           ["o", "i", "p", "l"],  # input('L3:').split(' ')
    #           ["w", "v", "n", "m"]]  # input('L4:').split(' ')

    # matrix2 = [['f', 'y', 'c', 'l'],  # input('L1:').split(' ')
    #            ["i", "o", "m", "g"],  # input('L2:').split(' ')
    #            ["o", "r", "i", "l"],  # input('L3:').split(' ')
    #            ["h", "j", "h", "u"]]  # input('L4:').split(' ')
    while True:
        matrix = []
        go = True
        for i in range(4):
            line = input("line:").lower()
            line = line.split()
            if len(line) != 4:
                print("wrong input, please re-enter matrix")
                go = False
                break
            for k in range(len(line)):
                if line[k].isalpha() and len(line[k]) == 1:
                    pass
                else:
                    print("wrong input, please re-enter matrix")
                    go = False
                    break
            if not go:
                break
            matrix.append(line)
        if go:
            game_start(matrix)
            break


def read_dictionary():
    dic = []
    with open(FILE, 'r') as f:
        for line in f:
            dic.append(line.strip())
    return dic


def game_start(matrix):

    mind = Remember()
    dic = read_dictionary()
    for y in range(4):
        for x in range(4):
            find_string(1, x, y, '', matrix, mind, dic)

    mind.total()


def find_string(level, x, y, curr_str, matrix, mind, dic):

    new_str = curr_str + str(matrix[y][x])
    new_matrix = copy.deepcopy(matrix)
    new_matrix[y][x] = ""

    if level < 4:
        find_all_neighbors(level, x, y, new_str, new_matrix, mind, dic)

    elif 4 <= level < LEVEL_LIMIT:
        if new_str in dic:
            # if not (new_str in words_list):
            mind.append(new_str)
            # words_list.append(new_str)
            find_all_neighbors(level, x, y, new_str, new_matrix, mind, dic)

    elif LEVEL_LIMIT <= level:
        if new_str in dic:
            mind.append(new_str)
        return new_str


def find_all_neighbors(level, x, y, new_str, new_matrix, mind, dic):  # Find in Neighbors
    # UP
    if 0 <= y - 1 <= 3 and new_matrix[y - 1][x] != "":
        find_string(level + 1, x, y - 1, new_str, new_matrix, mind, dic)
    # DOWN
    if 0 <= y + 1 <= 3 and new_matrix[y + 1][x] != "":
        find_string(level + 1, x, y + 1, new_str, new_matrix, mind, dic)
    # LEFT
    if 0 <= x - 1 <= 3 and new_matrix[y][x - 1] != "":
        find_string(level + 1, x - 1, y, new_str, new_matrix, mind, dic)
    # RIGHT
    if 0 <= x + 1 <= 3 and new_matrix[y][x + 1] != "":
        find_string(level + 1, x + 1, y, new_str, new_matrix, mind, dic)

    # UP-LEFT
    if 0 <= y - 1 <= 3 and 0 <= x - 1 <= 3 and new_matrix[y - 1][x - 1] != "":
        find_string(level + 1, x - 1, y - 1, new_str, new_matrix, mind, dic)
    # UP-RIGHT
    if 0 <= y - 1 <= 3 and 0 <= x + 1 <= 3 and new_matrix[y - 1][x + 1] != "":
        find_string(level + 1, x + 1, y - 1, new_str, new_matrix, mind, dic)
    # DOWN-LEFT
    if 0 <= y + 1 <= 3 and 0 <= x - 1 <= 3 and new_matrix[y + 1][x - 1] != "":
        find_string(level + 1, x - 1, y + 1, new_str, new_matrix, mind, dic)
    # DOWN-RIGHT
    if 0 <= y + 1 <= 3 and 0 <= x + 1 <= 3 and new_matrix[y + 1][x + 1] != "":
        find_string(level + 1, x + 1, y + 1, new_str, new_matrix, mind, dic)


'''
Check if this file is not called as subroutine, run main
'''
if __name__ == '__main__':
    main()
