from sys import stdin
from functools import reduce

N = 200020
a = [0] * N
n = int(stdin.readline())
for _ in range(n):
    a[sum(map(int, stdin.readline().split()))] += 1

for i, v in enumerate(a[:-1]):
    carry, a[i] = divmod(a[i], 2)
    a[i+1] += carry
    if a[i]:
        print(i, 0)