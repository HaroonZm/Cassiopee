import math
import sys

input = sys.stdin.readline

k = int(input())

n = 512
a = []
for i in range(n):
    val = math.factorial(7 + i) // math.factorial(i) // math.factorial(7)
    a.append(val)
a.reverse()

ans = ["FESTIVA" for _ in range(n)]
for i, item in enumerate(a):
    ans[i] += "L" * (k // item)
    k %= item
ans.reverse()
print("".join(str(item) for item in ans))