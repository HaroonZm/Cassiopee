import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import itertools
import numpy as np
from functools import lru_cache
from operator import itemgetter

X = list(map(int,readline().split()))
Y = list(map(int,readline().split()))

for i in [1,3,5]:
    X[i] += 1
    Y[i] += 1

X1 = X[:2]; X2 = X[2:4]; X3 = X[4:]
Y1 = Y[:2]; Y2 = Y[2:4]; Y3 = Y[4:]

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

U = 2 * 10 ** 6 + 10
MOD = 10**9 + 7
fact, fact_inv = make_fact(U,MOD)

@lru_cache(8)
def make_comb(n):
    return fact[n] * fact_inv[:n+1] % MOD * fact_inv[:n+1][::-1] % MOD

answer = 0
tasks = []
for p in itertools.product([0,1],repeat=6):
    x1,x2,x3,y1,y2,y3 = [A[i] for A,i in zip([X1,X2,X3,Y1,Y2,Y3],p)]
    sgn = (-1) ** sum(p)
    a,b,c,d = x2-x1, x3-x2, x2-x1+y2-y1, x3-x2+y3-y2
    c += 2; d += 2; sgn = -sgn
    tasks.append((a,b,c,d,sgn))

tasks.sort(key = itemgetter(2))

for a,b,c,d,sgn in tasks:
    # (1+A)^c(1+B)^d / (A-B)^2 における A^aB^b の係数
    # まずはa+b+2次式部分を抽出する：A側の次数で持つ
    D = a + b + 2
    # A^i B^j の寄与。
    L = max(0, D-d)
    R = min(c, D)
    if L > R:
        continue
    x = make_comb(c)[L:R+1]
    L,R = D-R,D-L
    y = make_comb(d)[L:R+1]
    x = x * y[::-1] % MOD
    # B=1と見立てる。(1-A)^2 で割って、A^(a-L)の係数
    np.cumsum(x,out=x)
    x %= MOD
    np.cumsum(x,out=x)
    x %= MOD
    L,R = D-R,D-L
    if 0 <= a-L < len(x):
        answer += sgn * x[a-L]

answer %= MOD
print(answer)