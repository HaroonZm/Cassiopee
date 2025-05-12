import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import depth_first_order

MOD = 10**9 + 7

N = int(readline())
XY = list(map(int,read().split()))

graph = csr_matrix(([1]*(N-1),(XY[::2],XY[1::2])),(N+1,N+1))
dfs_order, par = depth_first_order(graph,1,directed=False)
dfs_order = dfs_order.tolist()
par = par.tolist()

subtree_size = [1] * (N+1)
is_cent = [True] * (N+1)

for v in dfs_order[::-1]:
    if subtree_size[v] < (N+1)//2:
        is_cent[v] = False
    p = par[v]
    if p < 0:
        break
    if subtree_size[v] > N//2:
        is_cent[p] = False
    subtree_size[p] += subtree_size[v]

centroid = [v for v in range(1,N+1) if is_cent[v]]
Ncent = len(centroid)

if Ncent == 1:
    c = centroid[0]
    sizes = [N-subtree_size[c]] + [subtree_size[v] for v in range(1,N+1) if par[v] == c]
else:
    sizes = [N//2,N//2]

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

fact,fact_inv = make_fact(N+100,MOD)

def create_component_arr(n):
    x = np.full(n+1,fact[n],dtype=np.int64)
    x *= fact_inv[n::-1]; x %= MOD
    x *= x; x %= MOD
    x *= fact_inv[:n+1]; x %= MOD
    x[1::2] *= (-1); x %= MOD
    return x

def convolve(x,y):
    Lx = len(x); Ly = len(y)
    if Lx < Ly:
        Lx,Ly = Ly,Lx
        x,y = y,x
    z = np.zeros(Lx+Ly-1,np.int64)
    for n in range(Ly):
        z[n:n+Lx] += x*y[n]%MOD
    return z%MOD

x = np.array([1],np.int64)
for s in sizes:
    x = convolve(x,create_component_arr(s))

if Ncent == 1:
    answer = (x * fact[N:0:-1] % MOD).sum() % MOD
else:
    answer = (x * fact[N::-1] % MOD).sum() % MOD
print(answer)