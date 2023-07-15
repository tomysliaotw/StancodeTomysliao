"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE

Howework Assignment by Tom Liao
"""
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
from campy.graphics.gobjects import GOval, GLine, GLabel, GRect, GArc, GPolygon
from breakoutgraphics import BreakoutGraphics
import random

22
FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts
graphics = BreakoutGraphics()
paddle = graphics.paddle
vx = 0
vy = 0

start = True


def main():
    death = 0
    points = 0
    global graphics, vy, vx, start
    # Add the animation loop here!
    onmousemoved(paddleF)
    onmouseclicked(startF)

    while True:
        # Update
        graphics.ball.move(vx, vy)
        maybe = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        if maybe is not None:
            if maybe == paddle:
                vy = -vy
                print('paddle')
            elif maybe.width == graphics.brick.width and maybe.height == graphics.brick.height:
                graphics.window.remove(maybe)
                vy = -vy
                points += 1
        else:
            maybe = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
            if maybe is not None:
                if maybe == paddle:
                    vy = -vy
                    print('paddle')
                elif maybe.width == graphics.brick.width and maybe.height == graphics.brick.height:
                    graphics.window.remove(maybe)
                    vy = -vy
                    points += 1
            else:
                maybe = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.width)
                if maybe is not None:
                    if maybe == paddle:
                        vy = -vy
                        print('paddle')
                    elif maybe.width == graphics.brick.width and maybe.height == graphics.brick.height:
                        graphics.window.remove(maybe)
                        vy = -vy
                        points += 1
                else:
                    maybe = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                          graphics.ball.y + graphics.ball.width)
                    if maybe is not None:
                        if maybe == paddle:
                            vy = -vy
                            print('paddle')
                        elif maybe.width == graphics.brick.width and maybe.height == graphics.brick.height:
                            graphics.window.remove(maybe)
                            vy = -vy
                            points += 1

        # Check
        if graphics.ball.x <= 0 or (graphics.ball.x + graphics.ball.width) >= graphics.window.width:
            vx = -vx

        if graphics.ball.y <= 0 or (graphics.ball.y + graphics.ball.height) >= graphics.window.height:
            vy = -vy
        if (graphics.ball.y + graphics.ball.height) >= graphics.window.height:
            start = True
            death += 1
            vx = 0
            vy = 0
            graphics.ball.x = (graphics.window.width - graphics.ball.width) / 2
            graphics.ball.y = (graphics.window.height - graphics.ball.width) / 2

        # Pause(Frame Rate)
        pause(10)
        if death > 2:
            label = "Game over!" + str(points) + " points"
            over = GLabel(label)
            over.font = '-40'
            graphics.window.add(over, x=graphics.window.width / 2 - over.width / 2,
                                y=(graphics.window.height - over.height) / 2)
            break
        if points > 99:
            label = "You win!!!"
            over = GLabel(label)
            over.font = '-40'
            graphics.window.add(over, x=graphics.window.width / 2 - over.width / 2,
                                y=(graphics.window.height - over.height) / 2)
            break

            
def paddleF(move):
    px = move.x - paddle.x
    paddle.move(px, 0)


def startF(no):
    global vx, vy, start
    if start:
        vx = 1
        vy = 1
        if random.random() > 0.5:
            vx = -vx
        start = False


def traceF(x, y, window):
    trace = GOval(10, 10)
    window.add(trace, x=x, y=y)
    pause(1000)
    window.remove(trace)


if __name__ == '__main__':
    main()
