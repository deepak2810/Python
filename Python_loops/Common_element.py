# program to find the common element between two given list.

ls1 = [10,20,30,40,50]

ls2 = [20,10,50,60,80]

common_elements  = 0 

for i in ls1:
    for j in ls2:
        if i == j:
            common_elements += 1



print(common_elements)