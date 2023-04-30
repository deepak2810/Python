num = int(input('Please eneter a number: '))

#initialize an empty list
ls = []

for i in range(num):
    element = input('Enter element {}: '.format(i+1))
    ls.append(element)


print('The list is: ', ls)