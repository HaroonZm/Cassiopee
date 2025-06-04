import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)
MOD = 924844033

N, K = map(int, readline().split())

dp_0 = np.zeros((N+1, N+1), np.int64)
dp_1 = np.zeros((N+1, N+1), np.int64)
dp_2 = np.zeros((N+1, N+1), np.int64)
dp_0[0, 0] = 1
dp_1[0, 0] = 1
dp_2[0, 0] = 1

for n in range(1, N+1):
    dp_1[n, 1:] += dp_1[n-1, :-1]
    dp_2[n, 1:] += dp_2[n-1, :-1]
    if n >= 2:
        dp_0[n, 1:] += dp_0[n-1, :-1]
        dp_1[n, 1:] += dp_0[n-1, :-1]
    dp_2[n, 1:] += dp_1[n-1, :-1]
    dp_0[n] += dp_1[n-1]
    dp_1[n] += dp_1[n-1]
    dp_2[n] += dp_2[n-1]
    dp_0[n] %= MOD
    dp_1[n] %= MOD
    dp_2[n] %= MOD

def cumprod(arr, MOD):
    L = len(arr)
    Lsq = int(L ** .5 + 1)
    arr = np.resize(arr, Lsq ** 2).reshape(Lsq, Lsq)
    for nn in range(1, Lsq):
        arr[:, nn] *= arr[:, nn-1]
        arr[:, nn] %= MOD
    for nn in range(1, Lsq):
        arr[nn] *= arr[nn-1, -1]
        arr[nn] %= MOD
    return arr.ravel()[:L]

U = N + 100
x_fact = np.arange(U, dtype=np.int64)
x_fact[0] = 1
fact = cumprod(x_fact, MOD)
x_inv = np.arange(U, 0, -1, dtype=np.int64)
x_inv[0] = pow(int(fact[-1]), MOD-2, MOD)
fact_inv = cumprod(x_inv, MOD)[::-1]

x = np.array([1], np.int64)
nval = 1
while nval <= 2 * K:
    if nval > N:
        break
    n = nval

    items = (N-n)//(2*K)+1
    last = n + (items-1)*(2*K)
    use_left = (n-K > 0)
    use_right = (last+K <= N)
    xval = use_left + use_right
    arr = dp_0 if xval == 0 else (dp_1 if xval == 1 else dp_2)
    y = arr[items][:items+1]

    Lx = len(x)
    Ly = len(y)
    if Lx < Ly:
        x, y = y, x
        Lx, Ly = Ly, Lx
    arrc = np.zeros(Lx + Ly - 1, np.int64)
    for nn in range(Ly):
        arrc[nn:nn + Lx] += y[nn] * x % MOD
    arrc %= MOD

    x = arrc
    nval += 1

L = len(x)
x[1::2] *= (-1)
ans = (x[::-1] * fact[N-L+1:N+1] % MOD).sum() % MOD
print(ans)