from collections import Counter
import sys

# Pré-calcul avec Counter et itertools.product + map(sum, ...)
com_counter = Counter(map(sum, itertools.product(range(10), repeat=4)))

# Liste prête avec compréhension de liste et accès direct
com = [com_counter.get(i, 0) for i in range(51)]

# Lecture & affichage optimisés
print('\n'.join(str(com[int(line)]) for line in sys.stdin))