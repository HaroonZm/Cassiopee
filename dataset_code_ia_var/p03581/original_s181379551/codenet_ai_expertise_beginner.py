import numpy as np

A, B = map(int, input().split())
MOD = 10 ** 9 + 7
U = 2001

C = np.zeros((U, U), dtype=np.int64)
C[0][0] = 1

for n in range(1, U):
    for k in range(U):
        # C[n][k] = C[n-1][k] + C[n-1][k-1]
        if k > 0:
            C[n][k] += C[n-1][k-1]
        C[n][k] += C[n-1][k]
        C[n][k] %= MOD

S = np.zeros_like(C)
for n in range(U):
    for k in range(U):
        # Sum S[n][k] = sum(C[n-1][0..k])
        if n == 0:
            S[n][k] = 1 if k == 0 else 0
        else:
            S[n][k] = S[n][k-1] + C[n-1][k]
            S[n][k] %= MOD

result = 0
for k in range(A+1):
    term = C[B-1][k]
    sum_s = 0
    for i in range(A-k+1):
        sum_s = (sum_s + S[k][i]) % MOD
    result = (result + term * sum_s) % MOD

print(result)