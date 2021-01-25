

#Tae Young Kevin Shin                               # 09-23-2016 
#Defining main function

def main():
    print("This program shows different values of your salary according to current exchange rate for Dollar, Pound and Won.")
  
    Dollar, Pound ,Won = eval(input("Enter your monthly stipend in each currency separately:"))
    Average1 = (Dollar + Pound + Won) / 3                                            
    print("The average of Dollars, Pound, and Won is ",Average1)    
    Yen = 0.009961 * Dollar
    Yuan = 0.114952 * Pound                                             
    Rupee = 16.5357 * Won
    Average2 = (Yen + Yuan + Rupee) / 3
    print("The average of Yen, Yuan, Rupee is", Average2) 
    
main()

  #($, £, and Won, are representative currency unit of each country - USA, UK, and Korea).
  #(Defining variables respectively by 'eval' and 'input' data types)
  #(Taking the average of three variables, these domain are given by user's typing)
  #(Printing out the average value of the three defined by Average1)
  #(Authentic exchange rate as of 09-23-2016 taken from http://www.xe.com/currencyconverter/convert/)
  #(Printing out the average value of the three defined by Average2)
                           
                     
