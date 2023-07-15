from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import math

times = 0
xs = 50
ys = 50
size = 30
on = False
window = GWindow()
ball = GOval(size, size)


def main():
    window.add(ball, x=xs, y=ys)
    onmouseclicked(play)



def play(xy):
    global times, on
    print(times)
    if on == False:
        if times < 3:
            times+=1
            on = True
            vx =2
            delay = 50
            gravity = 1
            reduce = 0.7
            down = True
            speed = 0.5
            while True:
                pause(delay)
                if ball.x >= window.width + 10:
                    ball.x = xs
                    ball.y = ys
                    break
                if down == True:
                    speed = speed*1.1
                    gravity *= 1.1

                    if ball.y+30 >=window.height:
                        gravity *= -1
                        down = False
                        gravity = gravity*reduce
                else:
                    gravity *= 0.9
                    if round(gravity) ==    0:
                        down = True
                        gravity*=-1
                ball.move(vx, gravity)
            on = False



if __name__ == '__main__':
    main()
