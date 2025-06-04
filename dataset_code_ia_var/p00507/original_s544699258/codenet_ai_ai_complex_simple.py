from functools import reduce
from operator import mul

# Entrée et triage malin
sz = int(input())
lst = list(map(int, map(lambda _: input(), range(sz))))
quatuor = reduce(lambda x, y: x if x < y else y, [sorted(lst)[i:] for i in range(2)], sorted(lst))[:4]

# Génération non triviale de toutes les combinaisons de paires distinctes
indices = list(map(lambda x: (x//4,x%4), filter(lambda z: (z//4)!=(z%4), range(16))))
nums = list(map(lambda idx: reduce(lambda s, t: str(s)+str(t), (quatuor[idx[0]], quatuor[idx[1]])), indices))
ints = list(map(int, nums))

# Récupération du troisième entier trié, magic !
magique = sorted(ints)[2]
print(magique)