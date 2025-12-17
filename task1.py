#Given variables
party_pizza_mini = 14
large = 8
medium = 6
people = 6 # friends

#Do Not use crtl+A to select code.  Only copy the code below this line.
#------------------------------------------------------------------------------------------------
total_pizza = large + medium
print(f'{total_pizza}')

people += 1
share = total_pizza // people
leftover = total_pizza % people
print(f'Each person gets : {share}')
print(f'Leftover pizza : {leftover}')

people += 2
share = total_pizza // people
leftover = total_pizza % people
print(f'Each person gets : {share}')
print(f'Leftover pizza : {leftover}')
#Mom says "Wait, Brandon’s coming. We’re going to need more pizza. I’ll upgrade the mini to a party_pizza instead. It’s the same as 2 minis. Hopefully the leftovers will be enough to fill his hollow leg.”

people += 1
share = total_pizza // people
leftover = total_pizza % people
print(f'Each person gets : {share}')
print(f'Leftover pizza : {leftover}')
print("...for Mr. Hollow Leg")
