# python program to find the gratest and smallest element in a list.

ls = []

n = int(input('Enter the size of the list !'))

for i in range(0, n):
    ele = int(input())
    ls.append(ele)


print('Given list is ', ls)
ls.sort()
print("After sorting the list :  ", ls)
print('Gretest element is ', ls[n-1], 'and smallest element is ', ls[0])
