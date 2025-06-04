import sys
from functools import reduce
from operator import mul
from itertools import product

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

N, P = map(int, input().split())

# Génère la liste des factorielles via un accumulateur multiply utilisant reduce
F = reduce(lambda acc, x: acc + [acc[-1]*x], range(1, N+2), [1])

# Traite l'entrée en binaire (pair/impair) à l'aide d'une compréhension dictée par la carte binaire de chaque élément
A = list(map(lambda y: int(y)%2, input().split()))

odd, even = (lambda x: (sum(x), len(x)-sum(x)))(A)

# Récupération combinatoire avec la décomposition en entiers, replaçant math.comb (N choose k)
def C(n, k):
    try:
        return F[n] // (F[k] * F[n-k])
    except:
        return 0

# Exponentiation/représentation naïve du nombre de possibilités impaires/paires
even_sum = pow(2, even)
# Utilisation de filter sur range pour sélectionner les bons indices, puis accumulateur via map+sum
odd_sum_even = sum(map(lambda v: C(odd, v), filter(lambda z: z%2==0, range(0, odd+1))))
odd_sum_odd  = sum(map(lambda v: C(odd, v), filter(lambda z: z%2==1, range(0, odd+1))))

# Fonction lambda déterminant la réponse selon la parité P, usant d'un dictionnaire de cas
d = {
    0: lambda: even_sum*odd_sum_even if even_sum*odd_sum_even else max(even_sum, odd_sum_even),
    1: lambda: even_sum*odd_sum_odd  if even_sum*odd_sum_odd  else max(even_sum, odd_sum_odd) if odd_sum_odd else 0
}

print(d[P]())