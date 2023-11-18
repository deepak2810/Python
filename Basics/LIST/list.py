# python program to multiply all the elements within a list.

def multiply_list(list_nums):
    product = 1

    for num in list_nums:
        product *= num

    return product


list_numbers = []

n = int(input('Please enter a number ! '))

for i in range(0, n):
    ele = int(input())
    list_numbers.append(ele)


ans = multiply_list(list_numbers)

print(ans)
