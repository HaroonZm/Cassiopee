import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

MAX_A = 10**5
spf = [0]*(MAX_A+1)  # smallest prime factor
for i in range(2, MAX_A+1):
    if spf[i] == 0:
        spf[i] = i
        for j in range(i*i, MAX_A+1, i):
            if spf[j] == 0:
                spf[j] = i

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
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x

prime_to_index = dict()
for i, v in enumerate(A):
    for p in prime_factors(v):
        if p in prime_to_index:
            union(i, prime_to_index[p])
        prime_to_index[p] = i

B = sorted(A)
comp_A = [[] for _ in range(N)]
comp_B = [[] for _ in range(N)]

for i, v in enumerate(A):
    comp_A[find(i)].append(v)
for i, v in enumerate(B):
    comp_B[find(i)].append(v)  # safe because ordering by index wouldn't matter as union find keys by original indices

for i in range(N):
    if sorted(comp_A[i]) != sorted(comp_B[i]):
        print(0)
        break
else:
    print(1)