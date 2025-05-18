import math

n = int(input())
a = list(map(int, input().split()))
a.sort()
d = []
flag = a[0]
for i in range(1, n):
    if a[i] == flag:
        d.append(a[i])
    else:
        flag = a[i]

ans = n - 2 * math.ceil(len(d) / 2)
print(ans)