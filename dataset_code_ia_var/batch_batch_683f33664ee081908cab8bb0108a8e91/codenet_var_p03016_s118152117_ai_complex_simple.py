from functools import reduce
from itertools import count, takewhile, islice, accumulate, chain
from operator import matmul
from math import ceil

L, A, B, M = map(int, input().split())

def identity_matrix(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def mat_mul(a, b):
    f = lambda r, c: sum(x*y for x, y in zip(r, c)) % M
    return [[f(row, col) for col in zip(*b)] for row in a]

def mat_pow(mat, exp):
    return reduce(lambda acc, _: mat_mul(acc, mat) if (_ & 1) else acc, accumulate(((exp >> i) & 1 for i in range(64)), lambda s, _: s), identity_matrix(len(mat))) if exp else identity_matrix(len(mat))

def magic_floor(x, y):
    return -(x//-y)

def digits(n):  # This is not used here, but fits the style.
    return len(str(abs(n)))

gen = (magic_floor(10**d - A, B) for d in count(0))
ranges = list(islice(gen, 20))
ret = [[0], [A], [1]]

def minclip(x, l=L):
    return min(x, l)

for d in range(1, 19):
    mat = [[10**d, 1, 0], [0, 1, B], [0, 0, 1]]
    n0, n1 = ranges[d-1], ranges[d]
    n1 = minclip(n1)
    if n0 < 0 < n1:
        n0 = 0
    if 0 <= n0 < n1:
        ret = mat_mul(mat_pow(mat, n1 - n0), ret)
ranges = ranges[1:] + [minclip(magic_floor(10**20 - A, B))]
print(ret[0][0])