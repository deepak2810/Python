n = int(input("Enter a positive integer: "))

print("Prime numbers between 1 and", n, "are:")


for num in range(2, n + 1):
    is_prime = True

    # Check if 'num' is divisible by any number from 2 to 'num - 1'
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break

    # If 'num' is prime, print it
    if is_prime:
        print(num, end=" ")
