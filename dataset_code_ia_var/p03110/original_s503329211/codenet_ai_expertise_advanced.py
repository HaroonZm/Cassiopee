from sys import stdin
from functools import reduce

n = int(stdin.readline())
rates = {'JPY': 1, 'BTC': 380000}
s = 0

for _ in range(n):
    x, u = stdin.readline().split()
    s += float(x) * rates[u]

print(s)