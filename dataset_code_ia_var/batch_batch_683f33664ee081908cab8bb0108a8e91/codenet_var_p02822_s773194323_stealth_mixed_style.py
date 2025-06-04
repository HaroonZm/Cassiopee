import collections as C
import heapq, bisect, random, sys, string, math
from itertools import permutations as perms, accumulate, combinations as comb, product as prod
from operator import mul as opmul
from functools import reduce

sys.setrecursionlimit(99999999)
INF = float('inf')

def readints(): return list(map(int, sys.stdin.readline().split()))
I = lambda : int(sys.stdin.readline())
def gets(): return sys.stdin.buffer.readline().rstrip().decode()
ls = lambda : sys.stdin.buffer.readline().rstrip().decode().split()
def nread(fn, n): return [fn() for _ in range(n)]
MOD = 1000000007

n = I()
Gr = [[] for _ in range(n)]
for k in range(n-1):
    uu, vv = readints()
    for x, y in ((uu-1,vv-1),(vv-1,uu-1)):
        Gr[x].append(y)

parents = [-99]*n
sizes = [None for _ in range(n)]
def dfs(node):
    sizes[node] = 1
    for child in Gr[node]:
        if parents[node]==child: continue
        parents[child]=node
        sizes[node] += dfs(child)
    return sizes[node]

dfs(0)
P2 = [1]*(n+7)
for idx in range(1,len(P2)):
    P2[idx]=P2[idx-1]*2%MOD

answer=0
q = C.deque([0])
while len(q)>0:
    now=q.popleft()
    subtotal = (P2[n-1] - 1)
    for ch in Gr[now][:]:
        if ch==parents[now]: continue
        subtotal -= (P2[sizes[ch]]-1)
        q.append(ch)
    subtotal -= (P2[n-sizes[now]] - 1)
    answer += subtotal
    answer %= MOD

print(answer * pow(P2[n],MOD-2,MOD) % MOD)