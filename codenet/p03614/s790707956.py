n =int(input())
xs = [int(i) for i in input().split()]
a = 0
ret = 0
for i in range(n):
    ind = i + 1
    if ind == xs[i]:
        a += 1
    elif a > 0:
        ret += a // 2
        ret += a % 2
        a = 0
if a > 0:
    ret += a // 2
    ret += a %2
print(ret)