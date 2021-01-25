#Tae Young Kevin Shin
#12-07-2016
#COSC 235 Dr. Christ
#sphere's area and volume assignment

from graphics import *
from button import Button 

#defining Face class
class Face:
    def __init__(self,window,center,size):

        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0

        #defining constructor(instance variables)
        self.window = window
        self.center = center
        self.mouthSize = mouthSize
        self.mouthOff = mouthOff
        
        self.head = Circle(center, size)
        self.head.setFill("Yellow")
        self.head.draw(window)

        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff-15, -eyeOff+50)
        self.leftEye.setFill("Black")
        self.leftEye.draw(window)
        
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff+15, -eyeOff+50)
        self.rightEye.setFill("Black")
        self.rightEye.draw(window)

        self.nose = Circle(center, (3/4)*eyeSize)
        self.nose.setFill("Green")
        self.nose.draw(window)
        
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff-100)
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff-100)

        self.mouth = Line(p1,p2)

        titleDomain = Rectangle(Point(0,500), Point(500,460))
        titleDomain.setFill("Light Green")
        titleDomain.draw(window)
        title = Text(Point(250,480),"Facial Expression by clicks")
        title.draw(window)
        titleline = Line(Point(0,460), Point(500,460))
        titleline.draw(window)

    #defining smile method
    def shock(self):
        '''Being shocked'''

        self.mouth.undraw()        
        p1 = self.center.clone()
        p1.move(0,-50)

        self.mouth = Circle(p1, 30)
        self.mouth.setFill('blue')
        self.mouth.draw(self.window)

    #defining depressed method
    def depressed(self):
        '''depressed mood'''
         
        self.mouth.undraw()
         
        p1 = self.center.clone()
        p2 = self.center.clone()
        p1.move(-self.mouthSize/0.5+100, self.mouthOff/0.5-150)
        p2.move(self.mouthSize/0.5-100, self.mouthOff/0.5-150)
         
        self.mouth = Line(p1,p2)
        self.mouth.setFill('black')
        self.mouth.draw(self.window)

    #defining grumpy method    
    def grumpy(self):
        '''being grumpy'''
             
        self.mouth.undraw()
                 
        p1 = self.center.clone()
        p2 = self.center.clone()
        p3 = self.center.clone()
         
        p1.move(-self.mouthSize/1.5,-self.mouthOff)       
        p2.move(0,-self.mouthOff*0.6)
        p3.move(self.mouthSize/1.5,-self.mouthOff)
         
        self.mouth = Polygon(p1,p2,p3)
        self.mouth.setFill('black')
        self.mouth.draw(self.window)

#defining main function
def  main():
        #Create a window
        window = GraphWin("Face", 500,500)
        window.setCoords(0.0,0.0,500.0, 500.0)
        window.setBackground("White")
        face = Face(window, Point(250,250), 100)
        button = Button(window, Point(100,100), 100, 80, "Surprise")
        button2 = Button(window, Point(250,100), 100, 80, "Depressed")
        button3 = Button(window, Point(400,100), 100, 80, "Grumpy")
        closebutton = Button(window,Point(450,420), 100, 80, "Quit")

        button.activate()
        button2.activate()
        button3.activate()
        closebutton.activate()
        

        p = window.getMouse()    

        #starting a while loop
        while not closebutton.clicked(p):
            if button.clicked(p):
                face.shock()

            elif button2.clicked(p):
                face.depressed()

            elif button3.clicked(p):
                face.grumpy()

            p = window.getMouse()

        window.close()
        print("Facial experimentation is done")

if __name__ == '__main__': main()
