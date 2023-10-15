# python program to remove duplicate element from a list.

ls = []

N = int(input('Please enter the size of the element ! '))


for i in range(0, N):
    a = int(input())
    ls.append(a)


unique_ls = []


for i in ls:
    if i not in unique_ls:
        unique_ls.append(i)


print('Original ls was ' + str(ls))
print('After removing the duplicate element ' + str(unique_ls))
