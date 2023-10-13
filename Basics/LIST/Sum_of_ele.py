# python program to add all the elements of a list.

ls = []

n = int(input('Please enter the size of list'))

sum = 0

for i in range(0, n):

    a = int(input())
    ls.append(a)
    sum += ls[i]


print(ls)
print(sum)
