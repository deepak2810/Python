# python program to find the largest number of three.

def largest(a,b,c):
    if(a>b and a>c):
        return a

    elif(b>a and b>c):
        return b

    elif(c>a and c>b):
        return c


a = int(input('enter a number: '))
b = int(input('enter a number: '))
c = int(input('enter a number: '))
        
ans = largest(a,b,c)

print(ans)
