"""
File: class_reviews.py
Name: Tom Liao
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
import sys


def main():
    sc101avg = 0
    sc101people = 0
    sc101high = 0
    sc101low = sys.maxsize
    sc001avg = 0
    sc001people = 0
    sc001high = 0
    sc001low = sys.maxsize
    while True:
        in1 = input('Which class? ').upper()

        if in1 == 'SC101':
            in2 = int(input('Score: '))
            sc101people += 1
            sc101avg += in2
            if in2 > sc101high:
                sc101high = in2
            if in2 < sc101low:
                sc101low = in2
        elif in1 == 'SC001':
            in2 = int(input('Score: '))
            sc001people += 1
            sc001avg += in2
            if in2 > sc001high:
                sc001high = in2
            if in2 < sc001low:
                sc001low = in2
        elif in1 == '-1':
            break
        else:
            print("Invalid Input !!!")
    if (sc101people + sc001people) != 0:
        print("=========================SC001============================")
        if sc001people > 0:
            print("Max (001):"+str(sc001high))
            if sc001low != sys.maxsize:
                print("Low (001):" + str(sc001low))
            else:
                print("Low (001): 0")
            if sc001people > 0:
                print("Avg (001):" + str(sc001avg / sc001people))
            else:
                print("Avg (001): 0")
        else:
            print("No score for SC001")

        print("=========================SC101============================")
        if sc101people > 0:
            print("Max (101):" + str(sc101high))
            if sc101low != sys.maxsize:
                print("Low (101):" + str(sc101low))
            else:
                print("Low (101): 0")
            if sc101people > 0:
                print("Avg (101):" + str(sc101avg / sc101people))
            else:
                print("Avg (101): 0")
        else:
            print("No score for SC101")
    else:
        print("No class scores were entered")

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #


if __name__ == '__main__':
    main()
