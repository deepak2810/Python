numbers = [10, 20,30,40,50]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("The largest number is : ", largest)