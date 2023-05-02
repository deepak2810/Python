height = int(input('please enter your height '))

if height > 120:
    print('You can ride the rollercoster! ')

    age = int(input('please enter your age : '))

    if age <= 18:
        print('Please pay &7.')
    
    else:
        print('Please pay $12.')

else:
    print('sorry you have to grow taller! ')        