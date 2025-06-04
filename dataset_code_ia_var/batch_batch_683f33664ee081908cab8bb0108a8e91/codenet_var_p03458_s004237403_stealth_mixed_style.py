import sys
from numpy import array, maximum

N, K = (int(a) for a in input().split())
lst = []
for _ in range(N):
    lst.append(input().split())

size = K * 2 + 1
mat = [[0] * size for _ in range(size)]

def sum_twod(a, b, c, d):
    mat[a][b] += 1
    mat[a][d] -= 1
    mat[c][b] -= 1
    mat[c][d] += 1

i = 0
while i < N:
    x, y, clr = lst[i]
    x = int(x)
    y = int(y)
    idx = (x + (K if clr == "B" else 0)) % (K * 2)
    jdx = y % (K * 2)
    p, q = idx % K, jdx % K
    if ((idx < K and jdx < K) or (idx >= K and jdx >= K)):
        sum_twod(0, 0, p, q)
        sum_twod(p + K, 0, K * 2, q)
        sum_twod(p, q, p + K, q + K)
        sum_twod(0, q + K, p, K * 2)
        sum_twod(p + K, q + K, K * 2, K * 2)
    else:
        sum_twod(p, 0, p + K, q)
        sum_twod(0, q, p, q + K)
        sum_twod(p + K, q, K * 2, q + K)
        sum_twod(p, q + K, p + K, K * 2)
    i += 1

# cumulative sum
AA = array(mat)
for i in range(len(AA) - 1):
    for j in range(len(AA)):
        AA[i+1, j] += AA[i, j]
for j in range(len(AA) - 1):
    for i in range(len(AA)):
        AA[i, j+1] += AA[i, j]

f = lambda arr: arr.max()
print(f(AA))