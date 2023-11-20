# program to remove duplicate element from a list.

# 1 - Given list.

ls = [10, 20, 20, 30, 40, 50, 60]


# declare a empty list.


emp = []

for n in ls:
    if n not in emp:
        emp.append(n)
