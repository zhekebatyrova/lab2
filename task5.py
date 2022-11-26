num = str(input())
degree = len(num)-1
res = 0
for i in range(len(num)):
    res += int(num[i]) * (2**degree)
    degree = degree - 1
print(res)
