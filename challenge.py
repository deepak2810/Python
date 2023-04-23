print('Welcome to the tip calculaor.')
bill = float(input('What was the total bill? '))
percentage = int(input('What percentage of tip would you like to give? 10, 12, or 15?'))

if percentage==10:
    total_amount = bill + bill * (percentage/100)

elif percentage == 12:
    total_amount = bill+  bill * (percentage/100)

elif percentage == 15:
    total_amount = bill + bill * (percentage/100)


total_amount = round(total_amount,2)
person = int(input('How many people to split the bill?'))

each_pay = total_amount / person
each_pay = round(each_pay,2)

print(f'Each person should pay: {each_pay}')


