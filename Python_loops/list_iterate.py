numbers =  [ 12, 75, 150, 180, 145, 525, 50]

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop.

for i in numbers:
    if i % 5 == 0:
        if(i>=150):
            continue
        else:
            print(i)
        
        elif(i>500):
            break


