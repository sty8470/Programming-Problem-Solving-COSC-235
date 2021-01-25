#Tae Young Kevin Shin
#Dr. Christ COSC 235
#10-10-2016
#Chapter 4: Drawing my house

from graphics import*

#Calling main function to design code with graphics module
def main():

    win = GraphWin("Kevin's House")
    #Changing my coordiens from 200 x 200 pixels to 100 x 100 pixels
    win.setCoords(0.0, 0.0, 100.0, 100.0)

    #Drawing first rectangular(basic surface of the wall)
    p1 = win.getMouse()
    a = p1.getX()
    b = p1.getY()
    p1.draw(win)
    p2 = win.getMouse()
    c = p2.getX()
    d = p2.getY()
    p2.draw(win)
    rectangle = Rectangle(p1,p2)
    rectangle.setFill("Yellow")
    rectangle.draw(win)

    #Drawing a door with its width 1/5 of the width of entire base.
    p3 = win.getMouse()
    x = p3.getX()
    y = p3.getY()
    p3.draw(win)
    doorPoint1 = Point(x-((c-a)/10), ((b+d)/2))
    doorPoint2 = Point(x+((c-a)/10),b)
    rectangle1 = Rectangle(doorPoint1, doorPoint2)
    rectangle1.setFill("Orange")
    rectangle1.draw(win)
    #Drawing a window of which width is one half of the door
    p4 = win.getMouse()
    e=p4.getX()
    f= p4.getY()
    windowpoint1 = Point(e-((c-a)/10), f-((c-a)/10))
    windowpoint2 = Point(e+((c-a)/10), f+((c-a))/10)
    rectangle2 = Rectangle(windowpoint1,windowpoint2)
    rectangle2.setFill("Black")
    rectangle2.draw(win)
    #Drawing a rooftop
    p5= win.getMouse()
    xx = p5.getX()
    yy= p5.getY()
    rooftop = Polygon(Point(a,d), Point(c,d), Point(xx,yy))
    rooftop.setFill("Green")
    rooftop.draw(win)

main()



    
