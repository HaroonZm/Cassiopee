from sys import exit
from functools import reduce
from operator import mul

n = int(input())
A = sorted(map(int, input().split()))
mod = 10 ** 9 + 7

def valid_pairs(offset):
    for i in range(n // 2):
        idx = i * 2 + offset
        val = i * 2 + 1 - offset
        if A[idx] != A[idx + 1] or A[idx] != val:
            print(0)
            exit()
    return pow(2, n // 2, mod)

if n & 1:
    if A[0] != 0:
        print(0)
        exit()
    print(valid_pairs(1))
else:
    print(valid_pairs(0))