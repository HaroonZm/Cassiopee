from functools import reduce
from operator import mul as op_mul
from typing import List

k = int(input())
l, r = 0, k

# Fast integer binary search with PEP 465 matrix multiplication for later
while r - l > 1:
    m = (l + r) // 2
    if m * (m + 1) < k:
        l = m
    else:
        r = m

b = l
ad = k - b * (b + 1)
d = ((ad - 1) % (b + 1)) + 1
x = 2 * b + 1
y = 1
if ad - d > 0:
    x += 1

if d <= (b + 2) // 2:
    dd = d * 2 - 1
else:
    dz = (b + 1 - d)
    dd = dz * 2 + 2

x -= (dd - 1)
y += (dd - 1)

MOD = 10 ** 9 + 7

def mat_mult(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    size = len(a)
    return [[sum((a[i][k] * b[k][j]) % MOD for k in range(size)) % MOD for j in range(size)] for i in range(size)]

def mat_pow(mat: List[List[int]], power: int) -> List[List[int]]:
    result = [[1 if i == j else 0 for j in range(len(mat))] for i in range(len(mat))]
    while power:
        if power & 1:
            result = mat_mult(result, mat)
        mat = mat_mult(mat, mat)
        power >>= 1
    return result

def fib(n: int) -> int:
    if n <= 0:
        return 0
    F = [[1, 1], [1, 0]]
    return mat_pow(F, n - 1)[0][0]

ans = (fib(x - 1) * fib(y - 1)) % MOD
print(ans)