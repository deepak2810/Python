# python program to insert the element at given index in a list.


ls = []

n = int(input('Enter size of list ! '))

for i in range(0, n):
    ele = int(input())
    ls.append(ele)


print(ls)
ls.insert(0, 'CHECK_KAR')
print(ls)
