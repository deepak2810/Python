# Deleting list element from a liat.


ls = []

n = int(input('Please enter a size of the array !'))


for i in range(0, n):
    ele = int(input('Please enter array element '))
    ls.append(ele)

print('Your input list is ', ls)

# Delete element from index 1 to 3.

del ls[1:3]

print(" After deleting the list element ", ls)
