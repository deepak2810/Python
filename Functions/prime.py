# program to check if a given number is prime or not

def prime(n):

    if n == 1:
        print('The number is not a prime number. ')

    elif n > 1:

        for i in range(2, n):

            if (n % i == 0):
                print("this is not a prime number !")

            else:
                print(" This is a prime number ! ")
