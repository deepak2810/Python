# python program to find the greatest of 3 num.

a = int(input('Enter a number '))
b = int(input('Enter a number '))
c = int(input('Enter a number '))


if (a > b and a > c):
    print(c)


elif (b > c and b > a):
    print(b)


else:
    print(c)
