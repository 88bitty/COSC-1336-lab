#My name is Max Koeninger
#This program is complete

SAUCE = 0.5
PASTE = 0.08325
CLOVES = 0.5
OREGANO = 0.25

def saucecalc():
    servings = int(input("How many servings of spaghetti sauce do you want to make? "))
    print(
    f'''To make {servings} servings of spaghetti sauce, you will need:\n
    {SAUCE*servings:.2f} cups of tomato sauce,
    {PASTE*servings:.2f} cups of tomato paste,
    {CLOVES*servings:.2f} cloves of garlic,
    and {OREGANO*servings:.2f} tablespoons of oregano.'''
    )

saucecalc()
