A=[]
for _ in range(3):
    A.append(input())
from functools import reduce
res = ''
for idx, a in enumerate(A):
    res += a[idx]
print(res)