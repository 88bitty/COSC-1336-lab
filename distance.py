#This function determines the distance fell at the inputted time
def falling_distance(x):
    return (9.8*x**2)/2

if __name__ == '__main__':
    testRate = float(input("Please enter a number of seconds: "))
    print(falling_distance(testRate))
