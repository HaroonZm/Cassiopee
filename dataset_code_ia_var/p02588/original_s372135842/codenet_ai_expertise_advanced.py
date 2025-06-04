import sys
from functools import partial
from itertools import pairwise, starmap
from operator import add

input = sys.stdin.readline

MOD = 10**9 + 7
INF = float('inf')

def I():
    return int(input())

def LI():
    return list(map(int, input().split()))

def parse_number(s):
    if '.' not in s:
        return int(s) * 10**9
    int_part, dec_part = s.split('.')
    dec_part = (dec_part + '0' * 9)[:9]
    return int(int_part + dec_part)

def count_factor(x, p):
    cnt = 0
    while x and x % p == 0:
        x //= p
        cnt += 1
    return cnt

n = I()
lst = [parse_number(input().strip()) for _ in range(n)]

two = [count_factor(x, 2) for x in lst]
five = [count_factor(x, 5) for x in lst]

from collections import Counter

limit = 40  # 18+18+buffer, enough as only cnt<=27 matters
a = [[0] * limit for _ in range(limit)]
for i, j in zip(two, five):
    a[min(i, limit-1)][min(j, limit-1)] += 1

# 2D imos/prefix sum
for i in range(limit):
    for j in range(1, limit):
        a[i][j] += a[i][j-1]
for j in range(limit):
    for i in range(1, limit):
        a[i][j] += a[i-1][j]

ans = 0
for i, j in zip(two, five):
    x = max(0, 18 - i)
    y = max(0, 18 - j)
    total = a[limit-1][limit-1]
    up = a[limit-1][y-1] if y else 0
    left = a[x-1][limit-1] if x else 0
    diag = a[x-1][y-1] if x and y else 0
    ans += total - up - left + diag
    if i + i >= 18 and j + j >= 18:
        ans -= 1

print(ans // 2)