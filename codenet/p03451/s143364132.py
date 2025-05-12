import numpy as np
n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, reversed(input().split())))
cs1 = np.cumsum(a1)
cs2 = np.cumsum(a2)
income = [cs1[i]+cs2[n-1-i] for i in range(n)]
print(max(income))