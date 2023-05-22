# write a program to print the prime numbers between 1 to N.

n = int(input())

for i in range(1,n+1):
    if i > 1:
        for i in range(2,n+1):
            if (n % i == 0):
                break

            else:
                print(n)