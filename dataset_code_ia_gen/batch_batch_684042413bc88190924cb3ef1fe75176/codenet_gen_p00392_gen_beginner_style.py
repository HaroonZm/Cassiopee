import sys
sys.setrecursionlimit(10**7)

N = int(input())
A = list(map(int, input().split()))

MAX_A = 10**5

# Crée un tableau pour le crible des plus petits facteurs premiers
spf = [0] * (MAX_A + 1)
def sieve_spf():
    spf[1] = 1
    for i in range(2, MAX_A +1):
        spf[i] = i
    for i in range(2, int(MAX_A**0.5)+1):
        if spf[i] == i:
            for j in range(i*i, MAX_A+1, i):
                if spf[j] == j:
                    spf[j] = i
sieve_spf()

def get_prime_factors(x):
    factors = set()
    while x > 1:
        factors.add(spf[x])
        x //= spf[x]
    return factors

parent = [i for i in range(N)]
rank = [0]*N

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] +=1

# On construit des groupes (composantes connexes) en reliant les indices qui ont des nombres partageant un facteur premier commun.
# Pour cela, on utilise un dictionnaire qui map un facteur premier à un indice rencontré.

prime_to_index = dict()
for i in range(N):
    factors = get_prime_factors(A[i])
    for p in factors:
        if p in prime_to_index:
            union(i, prime_to_index[p])
        else:
            prime_to_index[p] = i

# On crée la copie triée
sorted_A = sorted(A)

# Pour que ce soit possible, pour chaque position i, A[i] et sorted_A[i] doivent appartenir au même groupe.
for i in range(N):
    if find(i) != find(A.index(sorted_A[i])):
        print(0)
        exit()

print(1)