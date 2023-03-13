#My name is Max Koeninger
#This program is complete

#This function appends user input to a list a number of times the user specifies.
#provided the input is 1 or greater. It also accepts input for a number to be used for value tests.
#It checks for ValueErrors and other errors, and validates that all inputs are numbers and 1 or above.
def main():
    nums = []
    valid = False
    try:
        while valid == False:
            try:
                size = round(float(input("Enter the number of elements in the list: ")))
                if(size>=1 and type(size)==int):
                    valid = True
                else:
                    print("The number must be 1 or more.")
            except ValueError:
                print("Your input must be a number")
        for num in range(size):
            valid = False
            while valid == False:
                try:
                    tempNum = round(float(input("Enter a number: ")))
                    if(type(tempNum) == int):
                        valid = True
                    else:
                        print("Your input must be a number")
                except ValueError:
                    print("Your input must be a number")
            nums.append(tempNum)
        valid = False
        while valid == False:
            try:
                testNumber = round(float(input("Enter the number you wish to test if the list elements are greater than: ")))
                if(type(testNumber) == int):
                    valid = True
                else:
                    print("Your input must be a number")
            except ValueError:
                print("Your input must be a number")
    except ValueError:
        print("Incorrect data type. Program terminated.")
        return
    except:
        print("Unexpected error. Program terminated.")
        return
    display_larger(nums, testNumber)

#This function accepts a list and a testing number, and appends all numbers in the list
#to a new list, provided they are above the testing number.
def display_larger(numList,testNum):
    newList = []
    for num in numList:
        if num > testNum:
            newList.append(num)
        else:
            pass
    print(f"These numbers are greater than {testNum}: {newList}")

if __name__ == "__main__":
    main()

