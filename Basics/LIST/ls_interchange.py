# python program to interchange the first and last element of a list.

ls = []

n = int(input('Please enter the size of the array ! '))

for i in range(0, n):
    a = int(input())
    ls.append(a)


var = ls[0]

ls[0] = ls[n-1]

ls[n-1] = var


print(ls)
