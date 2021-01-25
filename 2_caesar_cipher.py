#Tae Young Kevin Shin
#10-23-2016
#COSC 235 Dr. Christ
#Caesar Cipher Assignment


#Encrpytion: Text strings to Unicode numbers with key shifting value
def main():
    print("This program converts a string of text into a sequence of Unicode numbers")
    print("of which each character in the original message is replaced and shifted by 'key' characters in the Unicode Chracter set.")

    #Get the sayings to encode / Setting key value in a file
    sayings = input("Please type any words or sentence that you want to say: ")
    secretKey = open("key.secret.txt", "r")
    key = secretKey.read()
    key = int(key)

    #Loop through each substring and build Unicode message shifted by key characters
    message = " "
    for unit in sayings:
        numSaying= ord(unit)
        message = message + chr(numSaying + key) 
    print("The decoded message is:", message + ".")
main()

print()

#Caesar Cipher code within the alphabet scope regardless of Unicode
def main2():
    print("This program makes a circular shift over my entire sequence of my sayings")

    #user inputs message to be encrypted
    sayings = input("Please type any words or sentence that you want to say: ")

    #key to be used for the encryption by calling key.secret file
    secretKey = open("key.secret.txt", "r")
    key = secretKey.read()
    key = int(key)

    #Including every alphabet letter in one string
    alphabetList = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz. ")
    message  = " "
    for item in sayings:
        y = alphabetList.find(item)+key
        z = alphabetList[(alphabetList.find(item)+key) % 54]
        message = message + z
    print(message)
main2()


        
