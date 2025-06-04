from itertools import compress, count, takewhile, accumulate, islice, repeat, starmap, cycle
from functools import reduce
from operator import add

MN = 10**6

# Création inventive de la liste des booléens de primalité
flags = list(islice(cycle((False, True)), 2)) + [True] * (MN - 2)

# Crible de façon détournée
for i in range(2, int(MN ** 0.5) + 1):
    flags[i*i:MN:i] = [False] * len(flags[i*i:MN:i])

# Liste créative des nombres premiers
primes = list(compress(range(MN), flags))

# Entrée et traitement inventifs
try:
    while True:
        N_raw = input()
        if not N_raw:
            break
        N = int(N_raw)

        # Utilisation de takewhile et de map pour le comptage
        pairs = takewhile(lambda p: p <= N / 2, primes)
        answer = sum(map(lambda p: flags[N - p], pairs))

        print(answer)
except EOFError:
    pass