import sys
import numpy as np

n, q = list(map(int, input().split()))
MOD = 10 ** 9 + 7
INV2 = (MOD + 1) // 2
lines = sys.stdin.readlines()
aaa = np.fromiter(map(int, lines[:n]), dtype=np.int)
mat = (aaa.reshape(1, -1) < aaa.reshape(-1, 1)).astype(np.int64)
# print(mat)
for line in lines[n:]:
    x, y = map(int, line.split())
    x -= 1
    y -= 1
    tmp = (mat[x, y] + mat[y, x]) * INV2 % MOD
    mat[x] = mat[y] = (mat[x] + mat[y]) * INV2 % MOD
    mat[:, x] = mat[:, y] = (mat[:, x] + mat[:, y]) * INV2 % MOD
    mat[x, x] = mat[y, y] = 0
    mat[x, y] = mat[y, x] = tmp

ans = int(np.triu(mat).sum() % MOD)
ans = (ans << q) % MOD
print(ans)