# pyhton program to print multiplaction table.

def mul_table(num):

    for i in range(1,11):
        print("{multiplier} * {multiplicand} = {multiplication}".format(
            multiplier = num,
            multiplicand = i,
            multiplication = num *i))
        

mul_table(9)