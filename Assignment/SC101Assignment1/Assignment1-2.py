from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.graphics.gobjects import GOval, GLine

times = 0
window = GWindow()
ovalX = 0
ovalY = 0
oval = GOval(10, 10)


def main():
    # 判斷是否按滑鼠
    onmouseclicked(makeline)


def makeline(xy):
    global times, ovalY, ovalX, oval
    if times == 0:
        # 紀錄 x, y
        ovalX = xy.x
        ovalY = xy.y
        window.add(oval, x=xy.x-5, y=xy.y-5)
        times += 1
    elif times == 1:
        line = GLine(ovalX, ovalY, xy.x, xy.y)
        window.remove(oval)
        window.add(line)
        times = 0


if __name__ == '__main__':
    main()
