#My name is Max Koeninger
#This program is incomplete

import determine_stars

totalRating = 0

#This function accepts an input for a rating
#It then validates that it is between 0 and 10
def getRating():
    global totalRating
    rating = float(input("Enter critic's score between 0 and 10: "))
    if (rating >= 0 and rating <=10):
        totalRating += rating
    else:
        print("Error: the score must be from 0 to 10.")
        getRating()
        
for i in range(5):
    getRating()

totalRating /= 5
stars = determine_stars.starCalc(totalRating)

if (stars==""):
    print(f"Your score of {totalRating} gives no star rating should be shown.")
else:
    print(f"Your score of {totalRating:.2f} gives the rating {stars}")

    


