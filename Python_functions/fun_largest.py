def largest(num1,num2,num3):

    if( num1 > num2 & num1 > num3):
        print('Greatest number is : ', num3)

    elif( num2 > num1 & num2 > num3):
        print('Greatest number is : ', num2)

    else:
        print('Greatest number is : ', num3)



a =  int(input('enter a num :'))
b =  int(input('enter a num :'))
c =  int(input('enter a num :'))


a = largest(a,b,c)

print(a)
          