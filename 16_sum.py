#Tae Young Kevin Shin
#COSC 235 Dr. Christ
#11-04-2016

import math

#Defining the formula for sum of n numbers
def sumN(n):
    print("This funtion returns the sum of the first n natural numbers")
    sum =n*(n+1) / 2
    return(sum)

#Defining the formula for sum of cubes of n numbers
def sumNcubs(n):
    print("This function returns the sum of the cubes of the first n natural numbers")
    sum_cubes = pow ((n*(n+1)/2),2)
    return(sum_cubes)

#Defining main function to operate with parameters related to two functions above 
def main():
    num = eval(input("Please enter any natural number: "))
    a = sumN(num)
    b = sumNcubs(num)

    print("\nThe results for each function are ", a,"and",b)
             
main()

                

    
