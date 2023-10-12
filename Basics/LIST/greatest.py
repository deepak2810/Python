# program to fin the greatest element.

ls = []

n = int(input('please enter a number : '))

for i in range(0, n):
    ele = int(input())
    ls.append(ele)


max = ls[0]
for i in range(len(ls)):
    if ls[i] >= max:
        max = ls[i]

print('Greatest element is:  ', max)
