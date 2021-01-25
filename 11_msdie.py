from random import randrange

class MSDie:
    ''' Models a multi-sided die '''

    def __init__(self, sides):  #[two underscores+init+ two underscores] to define new "constructors" in python
        ''' Constructs a new die with x sides '''
        self.sides = sides
        self.value = 1

    def roll(self):
        ''' Simulates a roll of a die '''
        self.value = randrange(1,self.sides+1)

    def getValue(self):
        return self.value

    def setValue(self,value):
        self.value = value

        
        
        
