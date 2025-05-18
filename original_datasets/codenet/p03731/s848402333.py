import numpy as np
n, t = map(int, input().split())
a = list(map(int, input().split()))

result = 0
for i, v in enumerate(a[1:], 1):
    result += min(a[i - 1] + t, v) - a[i - 1]
print(result + t)