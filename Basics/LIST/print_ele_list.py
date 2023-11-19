
# program to print the elememt of a list.


def print_arr_list(ls):

    for i in ls:
        print(i)


ls1 = []

n = int(input('Enter the size of the array !'))


for i in range(0, n):
    ele = int(input('Enter list element'))
    ls1.append(ele)


print_arr_list(ls1)
