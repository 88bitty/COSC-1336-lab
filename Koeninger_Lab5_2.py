#My name is Max Koeninger
#This program is complete

import distance

#This function gets a number of seconds, validates that number is above 0,
#and then prints the result of the falling_distance function for each second
def main():
    seconds = int(input("Enter falling time in seconds: "))
    if (seconds == 0):
        print("The value must be positive")
        main()
    else:
        pass
    print("Time\tFalling Distance")
    print("------------------------")
    for second in range(1,seconds+1):
        fDistance = distance.falling_distance(second)
        print(f"{second}\t{fDistance:.2f}")

main()
