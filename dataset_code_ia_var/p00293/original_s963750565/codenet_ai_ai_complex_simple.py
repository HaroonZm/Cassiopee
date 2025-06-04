from functools import reduce
from operator import add, itemgetter
import sys

# Lire les deux lignes, map sur des map, flatten + permutations
def read_and_extract(n=2):
    data = list(map(lambda _: list(map(int, sys.stdin.readline().split())), range(n)))
    return tuple(tuple(col[i] for col in data) for i in range(n))

# Destructuring par assignations imbriquées et getitem
(*((nhm, mkg),),) = [read_and_extract()]

n, = map(lambda t: t[0], [nhm])
m, = map(lambda t: t[0], [mkg])

# Créer des paires originales compliquées (via cycle, takewhile, lambda...)
def cycle_pairs(seq):
    s = list(seq)
    return list(map(lambda t: tuple(map(lambda i: s[i], range(2))), range(1)))

goto_iimoriyama = list(map(tuple, zip(*[[*nhm]]*2)))
goto_turugajyo = list(map(tuple, zip(*[[*mkg]]*2)))

# Mélange inutilement complexe: chaînes, sets, map, sorted avec lambda
all_goto = list(map(lambda x: x, reduce(add, [goto_iimoriyama, goto_turugajyo], [])))
unique = dict.fromkeys(map(tuple, all_goto))
mixed = sorted(unique, key=lambda x: x[0]*60 + x[1])

# Format output via map + lambda imbriqué + f-string inside join
formatter = lambda t: f'{t[0]}:{t[1]:02d}'
result = list(map(formatter, mixed))
print(*result)