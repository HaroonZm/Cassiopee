from functools import reduce
from operator import xor

def xor_upto(n):
    return (n, 1, n + 1, 0)[n % 4]

a, b = map(int, input().split())
print(xor_upto(b) ^ xor_upto(a - 1))