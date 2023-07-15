"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def draw_fixed_lines(canvas):
    canvas.delete('all')  # delete all existing lines from the canvas
    # ----- Write your code below this line ----- #
    canvas.create_line(0, GRAPH_MARGIN_SIZE, canvas.winfo_width(), GRAPH_MARGIN_SIZE)
    canvas.create_line(0, canvas.winfo_height() - GRAPH_MARGIN_SIZE, canvas.winfo_width(),
                       canvas.winfo_height() - GRAPH_MARGIN_SIZE)
    x = GRAPH_MARGIN_SIZE
    for i in range(len(YEARS)):
        canvas.create_line(x, 0, x, canvas.winfo_height())
        canvas.create_text(x + 15, canvas.winfo_height() - GRAPH_MARGIN_SIZE + 10, text=YEARS[i], offset=tkinter.NW)
        x += canvas.winfo_width() / len(YEARS)


def draw_names(canvas, name_data, lookup_names):
    draw_fixed_lines(canvas)  # draw the fixed background grid
    # ----- Write your code below this line ----- #
    length = (canvas.winfo_height()-GRAPH_MARGIN_SIZE*2) / 1000
    for i in lookup_names:
        data = name_data[i]
        first = 0
        x = GRAPH_MARGIN_SIZE
        for k in range(len(YEARS)):
            try:
                second = float(data[str(YEARS[k])])
            except KeyError:
                second = 1001
            # print(second)
            if second == 1001:
                canvas.create_text(x + 30, GRAPH_MARGIN_SIZE+1000*length-20, text=i + '.')
            else:
                canvas.create_text(x + 30, second * length+10, text=i + str(int(second)))
            if first == 0:
                first = second
            else:
                y1 = second*length+GRAPH_MARGIN_SIZE
                y2 = first*length+GRAPH_MARGIN_SIZE
                canvas.create_line(x, y1, x-canvas.winfo_width() / len(YEARS), y2)
                first = second
            x += canvas.winfo_width() / len(YEARS)




# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
