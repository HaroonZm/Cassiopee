import sys
sys.setrecursionlimit(10**7)

MOD = 1000003

def mod_inv(x):
    return pow(x, MOD - 2, MOD)

fact = [1]
for i in range(1, 50001):
    fact.append(fact[-1] * i % MOD)
inv_fact = [0] * 50001
inv_fact[-1] = mod_inv(fact[-1])
for i in range(49999, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def comb(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD

def dfs(u, graph, visited):
    visited[u] = True
    size = 1
    for v in graph[u]:
        if not visited[v]:
            size += dfs(v, graph, visited)
    return size

def solve_case(n, m, edges):
    if n % 2 != 0:
        return 0

    graph = [[] for _ in range(n)]
    for i in range(n):
        graph[i].append((i+1)%n)
        graph[(i+1)%n].append(i)
    for a,b in edges:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    visited = [False]*n
    res = 1
    for i in range(n):
        if not visited[i]:
            size = dfs(i, graph, visited)
            if size % 2 != 0:
                return 0
            # number of perfect matchings in a bridged component of size 2k is k-th Catalan number
            k = size // 2
            # Catalan(k) = C(2k,k)/(k+1)
            c = comb(2*k, k)
            inv_k1 = mod_inv(k+1)
            res = res * (c * inv_k1 % MOD) % MOD
    return res

def main():
    input = sys.stdin.readline
    while True:
        n,m = map(int,input().split())
        if n == 0 and m == 0:
            break
        edges = [tuple(map(int,input().split())) for _ in range(m)]
        print(solve_case(n,m,edges))

main()