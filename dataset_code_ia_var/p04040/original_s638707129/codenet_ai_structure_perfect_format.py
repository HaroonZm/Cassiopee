from sys import exit
from itertools import count

def read():
    return [int(x) for x in input().split()]

P = 10**9 + 7

def inv(x):
    return pow(x, P - 2, P)

def comb(n, r):
    res = 1
    for i in range(r):
        res = (res * (n - i) * inv(i + 1)) % P
    return res

H, W, A, B = read()

result = 0

c1 = comb(H - A - 1 + B, B)
c2 = comb(W - B - 1 + A, A)

for i in range(1, min(H - A + 1, W - B + 1)):
    result = (result + c1 * c2) % P
    c1 = (c1 * (H - A - i) * inv(B + i)) % P
    c2 = (c2 * (W - B - i) * inv(A + i)) % P

print(result)