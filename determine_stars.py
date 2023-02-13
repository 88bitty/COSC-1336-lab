#This function gets a rating and returns a star value based on the rating
def starCalc(rating):
    if (rating<5):
        return ""
    elif (rating<6):
        return "*"
    elif (rating<7):
        return "**"
    elif (rating<8):
        return "***"
    elif (rating<9):
        return "****"
    else:
        return "*****"

if __name__ == '__main__':
    testRate = float(input("Please enter a rating: "))
    print(starCalc(testRate))
