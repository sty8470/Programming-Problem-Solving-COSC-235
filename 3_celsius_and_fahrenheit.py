def main():
    celsius = eval(input("What is the Celsius temeperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit")

    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")
    if fahrenheit < 30:
        print("Brrrr. Be sure to dress warmly!")
    

main()

