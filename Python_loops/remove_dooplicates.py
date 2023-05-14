# python program to remove the duplicates from the list.

ls = [10,20,30,40,50,60,20,30]

unique_ls = []

for i in ls:
    if i not in unique_ls:
        unique_ls.append(i)


# print the new list.

print(unique_ls)