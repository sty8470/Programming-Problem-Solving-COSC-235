# 09-14-2016
# Tae Young Kevin Shin
# COSC 235 B , Dr. Christ

# Defining main function
def main():
     print("This program illustrates a chaotic function")      # Writing string(main sentence) in print section
     x = eval(input("Enter a number between 0 and 1: "))   # Putting input and turn the plugged input value into changeable numerical value by evaluation 
     y = eval(input("Enter a number between 1 and 2: "))   # Setting another variable within the same principle
     Number =eval(input("How many numbers should I print? ")) # Setting the Number of loops supposed to be plugged in below loop
     print("input", 0.25, "  |    ", 1.26)                                              #  Showing the prospective numerical value to users
     print("------------------------------")                                            # Making clear of dotted lines like p.18 textbook
     #Starting loop
     for i in range (Number):             
         x = 3.9 * x * (1-x)
         y = 2.3 * y * (2-y)
         print(x,"      |      ",y)
main()

     
     
         

         
          
