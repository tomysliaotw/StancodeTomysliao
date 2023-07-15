from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GLine, GLabel, GRect, GArc, GPolygon
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

def main():

    window = GWindow(800, 500)
    onmouseclicked(show)
    backgrond = GRect(800, 500)
    backgrond.filled = True
    backgrond.fill_color = 'darkgreen'
    window.add(backgrond)
    label1 = GLabel('Volks Wagen Beetle')
    label1.font = '-50'
    label1.color = 'ivory'
    window.add(label1, x=150, y=label1.height+10)
    mainbody = GArc(1700, 900, 0, 80, x=-100, y=175)
    mainbody.filled = True
    mainbody.fill_color = 'ivory'
    window.add(mainbody)
    front = GArc(800, 500,80, 100)
    front.filled = True
    front.fill_color = 'ivory'
    front.color = 'ivory'
    window.add(front, x=180, y=270)
    window1 = GPolygon()
    window1.add_vertex((392,269))
    window1.add_vertex((416,194))
    window1.add_vertex((514,212))
    window1.add_vertex((513 , 267))
    window1.filled = True
    window1.fill_color = 'lightgray'
    window.add(window1)
    window2 = GArc(380, 220, 0, 90)
    window2.filled = True
    window2.fill_color = 'lightgray'
    window.add(window2, x=430, y=215)
    wheel11 = GOval(120, 120, y=310, x=250)
    wheel11.filled = True
    wheel11.fill_color = 'black'
    wheel11.color = 'white'
    window.add(wheel11)
    wheel21 = GOval(120, 120, y=310, x=580)
    wheel21.filled = True
    wheel21.fill_color = 'black'
    wheel21.color = 'white'
    window.add(wheel21)
    wheel12 = GOval(70, 70, x=275, y=335)
    wheel12.filled = True
    wheel12.fill_color = 'silver'
    wheel22 = GOval(70, 70, x=605, y=335)
    wheel22.filled = True
    wheel22.fill_color = 'silver'
    window.add(wheel22)
    window.add(wheel12)
    bumper = GRect(70,20, x=162 , y=365)
    bumper.filled = True
    bumper.fill_color = 'silver'
    bumper.color = 'silver'
    window.add(bumper)
    # bumper2 = GRect(10,60, x=161, y=323)
    # bumper2.filled = True
    # bumper2.fill_color = 'silver'
    # bumper2.color = 'silver'
    # window.add(bumper2)
    light2 = GRect(10,25)
    light2.filled = True
    light2.fill_color = 'silver'
    light2.color = 'silver'
    window.add(light2, x=230, y=310)
    lighty = GPolygon()
    lighty.add_vertex((229 , 312))
    lighty.add_vertex((229 , 334))
    lighty.add_vertex((0 , 380))
    lighty.add_vertex((0 , 216))
    lighty.filled = True
    lighty.fill_color = 'yellow'
    lighty.color = 'yellow'
    window.add(lighty)
    backlight = GOval(25, 50)
    backlight.color = 'red'
    backlight.filled = True
    backlight.fill_color = 'red'
    window.add(backlight, x=688, y=287)
    while True:
        lighty.filled = True
        lighty.fill_color = 'yellow'
        lighty.color = 'yellow'
        backlight.filled = False
        backlight.color = 'ivory'
        pause(1000)
        lighty.filled = False
        lighty.color = 'darkgreen'
        backlight.filled = True
        backlight.color = "red"
        backlight.fill_color = 'red'
        pause(1000)



def show(xy):
    print(xy.x,',', xy.y)



if __name__ == '__main__':
    main()
