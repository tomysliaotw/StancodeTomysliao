"""
File: anagram.py
Name:廖悠行
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop
dic = []
answer = []


def main():
    read_dictionary()
    while True:

        i = input(f'Find anagrams for({EXIT} to quit):')
        if i == EXIT:
            break
        else:
            start = time.time()
            find_anagrams(i, '')
            end = time.time()
            print('----------------------------------')
            print(len(answer), 'anagrams:', answer)
            print(f'The speed of your anagram algorithm: {end - start} seconds.')
            answer.clear()


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            dic.append(line.strip())


def find_anagrams(s, ans):
    if len(ans) >= len(s):
        if ans in dic:
            print(f'Found:{ans}')
            answer.append(ans)
    else:
        ok = s
        for k in range(len(ans)):
            h = ok.index(ans[k])
            ok = ok[:h] + ok[h + 1:]
        for i in s:
            if i in ok:
                if ans+i not in answer:
                    find_anagrams(s, ans + i)


if __name__ == '__main__':
    main()
