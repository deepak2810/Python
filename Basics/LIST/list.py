# python program to take list as input from user.


lst = []

n = int(input('Please enter no. of  elements'))


for i in range(0, n):
    ele = int(input())
    lst.append(ele)


print(lst)
