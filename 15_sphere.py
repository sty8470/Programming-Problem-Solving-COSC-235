#Tae Young Kevin Shin
#12-09-2016
#COSC 235 Dr. Christ
#sphere's area and volume assignment


import math

#defining class Sphere
class Sphere:
    def __init__(self, radius):
        self.radius = radius
   
    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4*(math.pi)* pow(self.radius,2)

    def volume(self):
        return (4/3)*(math.pi)* pow(self.radius,3)

#defining main function        
def main():
    r = eval(input("Enter a raidus>>> "))
    mySphere = Sphere(r)
    print("Surface area of the sphere is: ", mySphere.surfaceArea())
    print("Volume of the sphere is", mySphere.volume())

if __name__ == '__main__': main()

