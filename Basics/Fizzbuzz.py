# Fizzbuzz is a game, if a num is divisble by 3 then print "Fizz" and if the num is divisible by 5 then print 'Buzz" and if a number is divisible by both 3 and 5 then print "Fizz_Buzz."


# print from 1 to 100.


for i in range(1, 101):
    if i % 3 == 0:
        print('Fizz')

    if i % 5 == 0:
        print('Buzz')

    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')

    else:
        print(i)
