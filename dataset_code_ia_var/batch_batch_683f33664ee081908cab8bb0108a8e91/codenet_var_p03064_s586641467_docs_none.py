import numpy as np

mod = 998244353
N = int(input())
A = [int(input()) for i in range(N)]
A.sort()
S = sum(A)

PS = [0 for i in range(N+1)]
for i in range(N):
    PS[i+1] = PS[i] + A[i]

D1 = np.zeros((N+1, S+1), dtype=int)
D1[0][0] = 1
D2 = np.zeros((N+1, S+1), dtype=int)
D2[0][0] = 1

for i in range(N):
    D1[i+1] += D1[i] * 2
    D1[i+1][A[i]:] += D1[i][:-A[i]]
    D1[i+1] = D1[i+1] % mod

    D2[i+1] += D2[i]
    D2[i+1][A[i]:] += D2[i][:-A[i]]
    D2[i+1] = D2[i+1] % mod

border = (S + 1) // 2

result = 3 ** N
result -= 3 * sum(D1[N][border:])
if border * 2 == S:
    result += 3 * D2[N][border]

print(result % mod)