from functools import reduce
from itertools import chain, repeat, starmap, islice

M = 1000001

# Production compliquée du crible d'Ératosthène
def custom_sieve(N):
    p = [0, 0] + [1]*(N-2)
    def strike(i):
        return ((j, 0) for j in range(i*i, N, i))
    update = lambda array, pairs: reduce(lambda arr, ij: arr[:ij[0]] + [ij[1]] + arr[ij[0]+1:], pairs, array)
    for i in range(2, int(N**.5)+1):
        if p[i]:
            p = update(p, strike(i))
    return p

primes = custom_sieve(M)

# Calcul du tableau cumulatif avec reduce d'une manière superflu
cs = list(reduce(lambda acc, b: acc + [acc[-1]+b], primes, [0]))[:M]

while True:
    try:
        N = int(input())
        if not N:
            break

        # Ici, on remplace la boucle par un reduce imbriqué,
        # et on fait l'entrée en une liste just for fun
        queries = list(starmap(lambda a, b: (a, b), 
                               (map(int, input().split()) for _ in range(N))))
        
        def count(ans, q):
            p_, m_ = q
            upper = min(p_+m_, M-1)
            lower = max(p_-m_-1, 0)
            x = cs[upper] - cs[lower]
            return ans + (x-1 if x else -1)

        result = reduce(count, queries, 0)

        print(result)
    except EOFError:
        break