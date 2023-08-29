# print the factors of a number.

num = int(input('please enter a num : '))

if num == 0:
    print(" 0, 1")


else:
    for i in range(1, num+1):
        if num % i == 0:
            print(i)
