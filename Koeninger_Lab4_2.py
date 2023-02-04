#My name is Max Koeninger
#This program is complete

budget = 0
expenseTotal = 0

while True:
    budget = float(input('What is your monthly budget? '))
    if(budget > 0):
        break
    else:
        print('Your budget must be above 0')

while True:
    expense = float(input('Please enter an expense(0 to stop): '))
    expenseTotal += expense
    if(expense == 0):
        break
    else:
        pass

print(f'Your monthly budget is: ${budget:,.2f}')
print(f'Your monthly expenses are: ${expenseTotal:,.2f}')

budget -= expenseTotal
if(budget > 0):
    print(f'Your remaining money is: ${budget:,.2f}')
else:
    print(f'You are ${abs(budget):,.2f} over budget')
