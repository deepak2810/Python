num = int(input('Please eneter a number: '))

if num>0:
    print('number is psoitive! ')

    if (num % 2 == 0):
        print('Number is even.')

    else:
        print('Number is odd.')

elif(num == 0):
    print('Number is zero.')

else:
    print('Number is negative.')