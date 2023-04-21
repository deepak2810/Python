num = int(input('Enter your score: '))

if(num>=90):
    grade = 'A'

elif(num<= 80):
    grade = 'B'

elif(num <= 70):
    grade = 'C'

elif(num <= 60):
    grade = 'D'

else:
    grade = 'F'

print(f'Your grade is {grade}')