# print prime num from 1 to N.

N = int(input('Please enter a num: '))

for i in range(2, N+1):
    Flag = True

    for divisior in range(2, N+1):

        if i % divisior == 0:

            Flag = False
            break

    if Flag:
        print(i)
