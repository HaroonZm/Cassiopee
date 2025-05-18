import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

MOD = 924844033

def cumprod(arr,MOD):
    L = len(arr); Lsq = int(L**.5+1)
    arr = np.resize(arr,Lsq**2).reshape(Lsq,Lsq)
    for n in range(1,Lsq):
        arr[:,n] *= arr[:,n-1]; arr[:,n] %= MOD
    for n in range(1,Lsq):
        arr[n] *= arr[n-1,-1]; arr[n] %= MOD
    return arr.ravel()[:L]

def make_fact(U,MOD):
    x = np.arange(U,dtype=np.int64); x[0] = 1
    fact = cumprod(x,MOD)
    x = np.arange(U,0,-1,dtype=np.int64); x[0] = pow(int(fact[-1]),MOD-2,MOD)
    fact_inv = cumprod(x,MOD)[::-1]
    return fact,fact_inv

# mod (2K) ごとに、「反例として決めうつ個数」 -> 「合法な決め打ち方」を求める。
# 項数・両端の選択肢の有無でdp

N,K = map(int,readline().split())

dp_0 = np.zeros((N+1,N+1),np.int64) # 両端がともに使えない
dp_1 = np.zeros((N+1,N+1),np.int64) # 両端が片方だけ使える → 右側だけ使えるとして
dp_2 = np.zeros((N+1,N+1),np.int64) # 両端がともに使える
dp_0[0,0] = 1
dp_1[0,0] = 1
dp_2[0,0] = 1
for n in range(1,N+1):
    # 最後の項を右側でとる
    dp_1[n,1:] += dp_1[n-1,:-1]
    dp_2[n,1:] += dp_2[n-1,:-1]
    # 最後の項を左側でとる
    if n >= 2:
        dp_0[n,1:] += dp_0[n-1,:-1]
        dp_1[n,1:] += dp_0[n-1,:-1]
    dp_2[n,1:] += dp_1[n-1,:-1]
    # 最後の項を放置する
    dp_0[n] += dp_1[n-1]
    dp_1[n] += dp_1[n-1]
    dp_2[n] += dp_2[n-1]
    dp_0[n] %= MOD
    dp_1[n] %= MOD
    dp_2[n] %= MOD

def F(N,K,n):
    # mod 2Kでnのものたち
    items = (N-n)//(2*K)+1
    last = n + (items-1)*(2*K)
    x = (n-K>0) + (last+K<=N)
    arr = dp_0 if x == 0 else (dp_1 if x == 1 else dp_2)
    return arr[items][:items+1]

def convolve(x,y):
    Lx = len(x)
    Ly = len(y)
    if Lx < Ly:
        x,y = y,x
        Lx,Ly = Ly,Lx
    arr = np.zeros(Lx+Ly-1,np.int64)
    for n in range(Ly):
        arr[n:n+Lx] += y[n] * x % MOD
    arr %= MOD
    return arr

x = np.array([1],np.int64)
for n in range(1,2*K+1):
    if n > N:
        break
    x = convolve(x,F(N,K,n))

fact, _ = make_fact(N+100,MOD)

L = len(x)
x[1::2] *= (-1)
answer = (x[::-1] * fact[N-L+1:N+1] % MOD).sum() % MOD
print(answer)