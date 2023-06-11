# data structure in python.

# program to remove duplicates from the given list.


def remove_duplicates(lst):
    return list(set(lst))

numbers =  [1,2,3,1,3,5,6,6,7,8]

unique_num = remove_duplicates(numbers)

print(unique_num)