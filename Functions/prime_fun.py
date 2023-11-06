# pyhton program to find the prime numbers.

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    # Return True only if the loop completes without finding any factors
    return True


a = int(input('Enter a number !'))

if is_prime:
    print('it is a prime number.')

else:
    print('it is not a prime number !')
