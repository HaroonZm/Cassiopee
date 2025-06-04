n = int(input())
xs = [int(i) for i in input().split()]
a = 0
ret = 0
i = 0
while i < n:
    ind = i + 1
    if ind == xs[i]:
        a = a + 1
    else:
        if a > 0:
            ret = ret + a // 2
            ret = ret + a % 2
            a = 0
    i = i + 1
if a > 0:
    ret = ret + a // 2
    ret = ret + a % 2
print(ret)