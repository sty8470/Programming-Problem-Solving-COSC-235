#Cosc 235B course of Dr. Christ
# Tae Yong Kevin Shin
# 09-30-2016

#Summoning math library
import math

#defining main function
def main():

    #defining variables
    x = eval(input("Enter any hypothecial number that you want to put:"))
    guess = x/2
    num_times= eval(input("How many times do  you want to loop?:"))

    #applying Newton's method with counted loop
    for i in range(num_times):
        guess = (guess + (x/guess)) / 2
    print(guess)

    #showing users the difference of my guess and real sqrt(x)         
    print("The difference between the my estimate value and math.sqrt(x) is", guess - math.sqrt(x))

#finishing my main function    
main()

