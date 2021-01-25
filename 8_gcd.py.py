#Tae Young Kevin Shin
#11-22-2016 COSC 235B
#Dr. Christ / Python Programming of GCD function

#Defining GCD function
def GCD(x,y):

    #Input two values
    
    #Classifying each variable by each case
    if x==0 or y == 0:
            print("GCD does not deal with domain of 0")

    elif x<0 or y <0:
        print("GCD does not deal with domain of negative numbers")

    else:

        while x != y:
            
            if x>y:
                x = x-y
                
            elif x<y:
                y = y-x

        print(x)

#Passing two parameter values to GCD function
a = eval(input("Enter 1st natural number: "))
b = eval(input("Enter 2nd natural number: "))

GCD(a,b)
    
        
