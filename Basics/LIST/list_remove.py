# removing duplicate element from the list.

ls = [10, 20, 10, 20, 30, 40, 50, 60, 70]


# step 1: declare another list.

ls1 = []


for n in ls:
    if n not in ls1:
        ls1.append(n)


# print original list.

print(ls)

print('After removing elememnt: ',  ls1)
