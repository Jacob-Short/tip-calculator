# If the bill was 150.00, split between 5 people, with 12 % tip.
# Each person should pay (150.00 / 5) * 1.12 == 33.6
# Round the result 2 decimal places == 33.60

import os 

def console_clear():
    os.system('clear')


print('Welcome to the calculator')

bill = float(input('What was the total bill? $'))

tip = int(input('What % would you like to tip?'))

people = int(input('How many people are splitting the bill?'))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = '{:.2f}'.format(bill_per_person)
console_clear()
print('Calculating. . . .')
print(f'Each person should pay: ${final_amount}')
print('Thank you for using the tip calculator!')