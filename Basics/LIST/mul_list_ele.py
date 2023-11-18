def mul_list(ls):
    product = 1

    for i in ls:
        product *= i

    return product


demo_ls = []

n = int(input('Please enter the size of list !'))

for j in range(0, n):
    ele = int(input('enter a element for list'))
    demo_ls.append(ele)


ans = mul_list(demo_ls)

print(ans)
