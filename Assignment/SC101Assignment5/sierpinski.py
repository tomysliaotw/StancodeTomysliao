"""
File: sierpinski.py
Name: 廖悠行
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 9  # Controls the order of Sierpinski Triangle
LENGTH = 600  # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150  # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100  # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950  # The width of the GWindow
WINDOW_HEIGHT = 700  # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
    """
    TODO:
    """
    sierpinski_triangle_helper(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle_helper(order, length, upper_left_x, upper_left_y):
    l1 = GLine(upper_left_x, upper_left_y, upper_left_x + 0.5 * length, upper_left_y + length * 0.886)
    l2 = GLine(upper_left_x + 0.5 * length, upper_left_y + length * 0.886, upper_left_x + length, upper_left_y)
    l3 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
    window.add(l1)
    window.add(l2)
    window.add(l3)
    sierpinski(order - 1, length / 2, upper_left_x + length / 4, upper_left_y)


def sierpinski(order, length, upper_left_x, upper_left_y):
    if order == 0:
        pass
    else:
        line1 = GLine(upper_left_x, upper_left_y + 0.886 * length, upper_left_x+length, upper_left_y + 0.886 * length)
        line2 = GLine(upper_left_x + length, upper_left_y + 0.886 * length, upper_left_x + length / 2, upper_left_y)
        line3 = GLine(upper_left_x + length / 2, upper_left_y, upper_left_x, upper_left_y + 0.886 * length)
        window.add(line1)
        window.add(line2)
        window.add(line3)
        sierpinski(order-1, length/2, upper_left_x-length/4, upper_left_y)
        sierpinski(order-1, length/2, upper_left_x+length/4, upper_left_y+0.886*length)
        sierpinski(order-1, length/2, upper_left_x+length/4*3, upper_left_y)


if __name__ == '__main__':
    main()
