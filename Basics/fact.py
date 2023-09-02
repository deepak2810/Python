# python program to find the factorial of a program.

n = int(input('please enter a number'))

if n == 0 or n < 0:
    print('Value of n should be greater than 1')

else:
    fact = 1

    while (n):
        fact *= n
        n = n-1


print(fact)
