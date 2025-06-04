import numpy as np

n = int(input())
a = np.zeros(n, dtype=int)
b = np.zeros(n, dtype=int)
buf1 = input().split()
buf2 = input().split()
for i in range(n):
    a[i] = int(buf1[i])
    b[i] = int(buf2[i])

r = 0

if np.sum(a) < np.sum(b):
    r = -1
else:
    c = a - b
    c = np.sort(c)
    if c[0] >= 0:
        r = 0
    else:
        ii = -1
        for i in range(n):
            if c[i] >= 0:
                ii = i
                break
        debt = 0
        for j in range(ii):
            debt += c[j]
        for k in range(n):
            debt += c[n - 1 - k]
            if debt >= 0:
                r = ii + (k + 1)
                break

print(r)