from decimal import *
import sys
import copy

getcontext().prec = 1000
input = sys.stdin.readline
n, k = input().split()
n = int(n)
k = Decimal(k)
a = []
for i in range(n):
    a.append(Decimal(input()))
if Decimal(0) in a:
    print(n)
    sys.exit()
if k == Decimal(0):
    print(0)
    sys.exit()
left = copy.copy(a)
right = copy.copy(a)
for i in range(n - 1):
    left[i + 1] *= left[i]
for i in reversed(range(n - 1)):
    right[i] *= right[i + 1]
mul = left[-1]
right.append(Decimal(1))
r = []
for i, x in enumerate(right):
    while r and r[-1][1] <= x:
        r.pop()
    r.append((i, x))
l = [(-1, Decimal(1))]
for i, x in enumerate(left):
    if not l or l[-1][1] < x:
        l.append((i, x))
ans = 0
at = -1
for i, x in l:
    while at + 1 < len(r) and x * r[at + 1][1] * k >= mul:
        at += 1
    if at >= 0 and ans < r[at][0] - i - 1:
        ans = r[at][0] - i - 1
print(ans)