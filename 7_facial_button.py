from graphics import *
 
class Face:
     
    def __init__(self,window,center,size):
         
        self.center = center
        self.size = size
        self.window = window
         
        eyeSize = 0.15*size
        eyeOff = size/3.0
         
        self.mouthSize = 0.8*size
        self.mouthOff =size/2.0
         
        self.head = Circle(center,size)
        self.head.setFill('yellow')
        self.head.draw(window)
         
        self.leftEye = Circle(center,eyeSize)
        self.leftEye.move(-eyeOff, eyeOff)
         
        self.rightEye = Circle(center,eyeSize)
        self.rightEye.move(eyeOff, eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
         
        p1 = center.clone()
        p1.move(-self.mouthSize/2,-self.mouthOff)
         
        p2 = center.clone()
        p2.move(self.mouthSize/2,-self.mouthOff)
         
        self.mouth = Line(p1,p2)
        self.mouth.draw(window)
         
          
         
    def smile(self):
        '''Smile expression'''
         
        self.mouth.undraw()
                 
        p1 = self.center.clone()
        p2 = self.center.clone()
        p3 = self.center.clone()
         
        p1.move(-self.mouthSize/1.5,-self.mouthOff)       
        p2.move(0,-self.mouthOff*1.5)
        p3.move(self.mouthSize/1.5,-self.mouthOff)
         
        self.mouth = Polygon(p1,p2,p3)
        self.mouth.setFill('black')
        self.mouth.draw(self.window)
         
    def shock(self):
        '''Shock expression'''
         
        self.mouth.undraw()
         
        p1 = self.center.clone()
        p1.move(0,-self.mouthOff)
         
        self.mouth = Circle(p1,self.mouthSize/3)
        self.mouth.setFill('black')
        self.mouth.draw(self.window)
         
    def flown(self):
         
        self.mouth.undraw()
                 
        p1 = self.center.clone()
        p2 = self.center.clone()
        p3 = self.center.clone()
        p4 = self.center.clone()
         
        p1.move(-self.mouthSize/1.5,-self.mouthOff)       
        p2.move(0,-self.mouthOff*0.6)
        p3.move(self.mouthSize/1.5,-self.mouthOff)
        p4.move(0,-self.mouthOff*0.4)
         
        self.mouth = Polygon(p1,p2,p3,p4)
        self.mouth.setFill('black')
        self.mouth.draw(self.window)
         
         
 
class Button:
 
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""
 
    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """
 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
 
    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)
 
    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()
 
    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True
 
    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
 
 
def main():
    '''Main algorithm'''
    win, x, smile, shock, flown, quit = setupGUI()
    playing(win, x, smile, shock, flown, quit)
    win.close()
     
     
def setupGUI():
    '''Drawing start screen'''
         
    #set up windows
    win = GraphWin('Face Expression',300,300)
    win.setCoords(0,0,100,100)
    win.setBackground('white')
     
    #draw first grim default face
    x = Face(win,Point(50,55),30)
     
    #draw 3 expression button and quit button    
    sm_button = Button(win,Point(16.665,7.5),33,15,'Smile')
    sm_button.activate()
     
    sh_button = Button(win,Point(49.995,7.5),33,15,'Shock')
    sh_button.activate()
     
    f_button = Button(win,Point(83.325,7.5),33,15,'Flown')
    f_button.activate()
     
    q_button = Button(win,Point(90,95),15,7,'Quit')
    q_button.activate()
     
    return win, x, sm_button, sh_button, f_button, q_button
 
 
def playing(win, x, smile, shock, flown, quit):
    '''Let user click on any expression button or quit program.'''
     
    p = win.getMouse()
     
    while not quit.clicked(p):
         
        if smile.clicked(p): x.smile()
        elif shock.clicked(p): x.shock()
        elif flown.clicked(p): x.flown()
         
        p = win.getMouse()
 
     
if __name__ == '__main__': main()
