# python program to separate the even and odd numbers from a given list.

ls = []

n = int(input('Please enter a number ! '))


for i in range(0, n):
    ele = int(input('Enter list element ! '))
    ls.append(ele)


print(ls)

# declare two empty list one for odd and another for even.

odd = []
even = []

for i in ls:
    if i % 2 == 0:
        even.append(i)

    else:
        odd.append(i)


# print both odd and even lists.

print(odd)
print(even)
