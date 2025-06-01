import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
sortedA = sorted(A)

MAX = 10**5
spf = [0]*(MAX+1)
def build_spf():
    for i in range(2, MAX+1):
        if spf[i] == 0:
            spf[i] = i
            for j in range(i*i, MAX+1, i):
                if spf[j] == 0:
                    spf[j] = i
build_spf()

def prime_factors(x):
    factors = set()
    while x > 1:
        factors.add(spf[x])
        x //= spf[x]
    return factors

parent = list(range(N))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x

factor_map = dict()
for i,v in enumerate(A):
    for p in prime_factors(v):
        if p in factor_map:
            union(i, factor_map[p])
        factor_map[p] = i

components = dict()
for i in range(N):
    r = find(i)
    components.setdefault(r,[]).append(i)

for indices in components.values():
    original_vals = [A[i] for i in indices]
    target_vals = [sortedA[i] for i in indices]
    if sorted(original_vals) != sorted(target_vals):
        print(0)
        exit()
print(1)