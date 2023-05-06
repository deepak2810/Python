N = int(input("Enter a number: "))

for num in range(1, N+1):
    # check if the number is prime
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            # number is prime, print it
            print(num)