#My name is Max Koeninger
#This program is complete

#This function appends user input to a list a number of times the user specifies.
#It checks for ValueErrors and other errors in both user inputs.
def main():
    nums = []
    try:
        size = int(input("Enter the number of elements in the list: "))
    except ValueError:
        print("Incorrect data type. Program terminated.")
        return
    except:
            print("Unexpected error. Program terminated.")
            return
    for num in range(size):
        try:
            tempNum = int(input("Enter a number: "))
            nums.append(tempNum)
        except ValueError:
            print("Incorrect data type: a number was expected. Program terminated.")
            return
        except:
            print("Unexpected error. Program terminated.")
            return
    display_larger(nums)

#This function takes a list and user input for a number, and creates new list with all numbers
#from the original list that are larger than the input number. It checks for valueErrors and other errors.
def display_larger(numList):
    newList = []
    try:
        testNum = int(input("Enter the number you wish to test if the list elements are greater than: "))
    except ValueError:
        print("Incorrect data type. Program terminated.")
        return
    except:
        print("Unexpected error. Program terminated.")
        return
    for num in numList:
        if num > testNum:
            newList.append(num)
        else:
            pass
    print(f"These numbers are greater than {testNum}: {newList}")

if __name__ == "__main__":
    main()

