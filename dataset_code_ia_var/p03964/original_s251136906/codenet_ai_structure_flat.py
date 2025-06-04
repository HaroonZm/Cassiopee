from math import ceil
from decimal import Decimal

N = int(input())
T = 1
A = 1
i = 0
while i < N:
    s = input()
    lst = s.split()
    t = int(lst[0])
    a = int(lst[1])
    n = Decimal(max(ceil(T / t), ceil(A / a)))
    T = n * t
    A = n * a
    i += 1
print(T + A)