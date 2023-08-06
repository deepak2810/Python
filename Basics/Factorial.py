# write a program for factorial of program.


num = int(input('Please enter a num : '))


fact = 1


# Check if num is negative, positive or zero.
if num < 0:
    print('SOrry factorial does not exist for the -ve numbers.')

elif num == 0:
    print('1')


else:

    for i in range(1, num+1):
        fact *= i

    print(fact)
