from collections import Counter
from sys import exit

n = int(input())
a = list(map(int, input().split()))
cnt = Counter(a)
items = sorted(cnt.items())

MOD = 10**9 + 7

def invalid():
    print(0)
    exit()

if n & 1 == 0:
    if any(x != 2*i + 1 or c != 2 for i, (x, c) in enumerate(items)):
        invalid()
else:
    if items[0] != (0, 1):
        invalid()
    if any(x != 2*i or c != 2 for i, (x, c) in enumerate(items[1:], 1)):
        invalid()

print(pow(2, n // 2, MOD))