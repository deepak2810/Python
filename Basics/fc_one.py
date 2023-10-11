# program to write a factorial of a number.

N = int(input('Please enter a number ! '))

fact = 1

for i in range(2, N+1):
    fact *= i


print(fact)
