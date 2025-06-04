from functools import reduce
from itertools import compress, count, takewhile, islice
from operator import itemgetter

# Génération du crible via reduce et lambda sur une compréhension de liste
size = 50000
p = reduce(
    lambda acc, curr: [
        acc[i] if i < curr**2 - 1 or i % curr != curr**2 % curr else False
        for i in range(size)
    ] if acc[curr-1] else acc,
    range(2, int(size**0.5) + 2),
    [True] * size
)
p[0] = False

# Liste des nombres premiers via compress et count
prime = list(compress(count(1), p))

# Boucle d'entrée infinie superflue avec un try-except pour fin de fichier
from sys import stdin
for ligne in stdin:
    try:
        n = int(ligne.strip())
        if not n:
            break
        half = n // 2
        # On utilise takewhile pour limiter aux premiers inférieurs à half
        candidates = takewhile(lambda x: x <= half, prime)
        # Calcul compliqué avec sum et itemgetter
        count = sum(map(itemgetter(n - i - 1), [p for i in candidates]))
        print(count)
    except:
        break