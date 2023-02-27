#My name is Max Koeninger
#This program is complete

import random

#Write random numbers between range1 and range2 to a file,
#with the amount being controlled by num
def write(num,range1,range2):
    randFile = open("randfile.txt","w")
    for number in range(num):
        randNum = str(random.randint(range1,range2))
        randFile.write(f"{randNum}\n")
    print("The file was created successfully")

#Get input of num, range1, and range2 for write()
#and validates the input follows protocol
def main():
    validInput = False
    while validInput == False:
        numGen = int(input("How many random numbers to generate (1-100)? "))
        if not (numGen >= 1 and numGen <= 100):
            print("The number must be in the range 1-100.")
        else:
            validInput = True
        
    validInput = False
    while validInput == False:
        rangeOne = int(input("Minimum random number value (0-500): "))
        if not (rangeOne >= 0 and rangeOne <= 499):
            print("The number must be in the range 0-500.")
        else:
            validInput = True

    validInput = False
    while validInput == False:
        rangeTwo = int(input("Maximum random number value (0-500): "))
        if not (rangeTwo > rangeOne and rangeTwo <= 500):
            print("The value must be greater than the minimum one and less than 500.")
        else:
            validInput = True

    write(numGen,rangeOne,rangeTwo)

if __name__ == "__main__":
    main()
