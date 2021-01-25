#Tae Young Kevin Shin
#11-22-2016 Comsc 235B
#Dr. Christ / Chaning color image to grayscale image

#import graphics
from graphics import*


#Defining main function
def main():

    #Drawing / Pulling up given picture on graphic window
    win = GraphWin("Grayscale",600,600)
    image = Image(Point(300,300), "pikachu.gif")
    image.draw(win)

    row = 0
    column = 0

    win.getMouse()

    #Starting for-loop of row and column consecutively
    for row in range(image.getWidth()):
        for column in range(image.getHeight()):
            r, g, b = image.getPixel(row, column)
            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            image.setPixel(row, column, color_rgb(brightness, brightness, brightness))
        win.update()


    #Closing the window after one-more mouse click
    win.getMouse()
    win.close()

main()

