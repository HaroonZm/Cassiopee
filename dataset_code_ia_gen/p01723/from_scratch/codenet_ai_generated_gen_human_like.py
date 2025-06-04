import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7

N = int(sys.stdin.readline())
edges = [[] for _ in range(N)]
indegree = [0]*N

for _ in range(N-1):
    a,b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    indegree[b] += 1

# DP to count the number of ways to merge subtrees with given order constraints
def modinv(a,m=MOD):
    return pow(a,m-2,m)

fact = [1]*(N+1)
invfact = [1]*(N+1)
for i in range(1,N+1):
    fact[i] = fact[i-1]*i % MOD
invfact[N] = modinv(fact[N],MOD)
for i in reversed(range(N)):
    invfact[i] = invfact[i+1]*(i+1)%MOD

def comb(n,r):
    if r>n or r<0:
        return 0
    return fact[n]*invfact[r]%MOD*invfact[n-r]%MOD

# memo[node]: (size_of_subtree, ways_to_arrange)
memo = [None]*N

def dfs(u):
    size = 1
    ways = 1
    children = []
    for v in edges[u]:
        s,w = dfs(v)
        size += s
        children.append((s,w))
    # The ways to merge children subtrees:
    # multinomial coefficient for possible interleavings multiplied by ways of children
    total = size - 1
    ways = 1
    for s,w in children:
        ways = ways * w % MOD
        ways = ways * comb(total,s) % MOD
        total -= s
    return size, ways

roots = [i for i,x in enumerate(indegree) if x==0]

if N==1:
    print(1)
    sys.exit()

# The graph is forest (N nodes, N-1 edges), so exactly one root.
# Problem states at least one solution exists, so there's exactly one root.
root = roots[0]

_, ans = dfs(root)
print(ans % MOD)