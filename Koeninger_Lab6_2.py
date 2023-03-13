#My name is Max Koeninger
#This program is complete

#This function opens randfile.txt and reads each line, adding the integer
#values and number of lines. It then prints these and the numerical average.
#The function stops if it encounters an IOError, ValueError or other error.
def read():
    try:
        print("Reading the file...")
        try:
            rFile = open("randfile.txt","r")
        except IOError:
            print("This filename doesn’t exist. Program terminated.")
            return
        lineTotal = 0
        numTotal = 0
        for line in rFile:
            try:
                numTotal += int(line)
                lineTotal += 1
            except ValueError:
                print("Incorrect data type. Program terminated.")
                return
        try:
            print(f"Read from the file: {lineTotal} numbers.")
            print(f"Total of the numbers: {numTotal}")
            avgTotal = numTotal/lineTotal
            print(f"Average of the numbers: {avgTotal}")
        except ZeroDivisionError:
            print("Average of the numbers: can’t be calculated.")
    except:
        print("Other error occurred. Program terminated.")

if __name__ == "__main__":
    read()
