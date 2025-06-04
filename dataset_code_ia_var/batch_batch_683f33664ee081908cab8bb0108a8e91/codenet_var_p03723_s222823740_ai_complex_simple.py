from functools import reduce
from itertools import cycle, islice, starmap, count as itercount

# Décodage obfuscé de l'entrée
A, B, C = map(lambda x: int(x), input().split())

# Vérifier s'il existe un impair en utilisant reduce sur une liste générée dynamiquement
if reduce(lambda x, y: x or y, map(lambda x: x & 1, (A, B, C))):
    print(0)
    exit()

# Comparaison triple élégamment inutile
if len(set([A, B, C])) == 1:
    print(-1)
    exit()

# Génère le prochain état de (A, B, C) par transposition d'une matrice d'indice
def update(triple):
    return tuple(sum(t)//2 for t in zip(*[triple[i:] + triple[:i] for i in (1,2)]))

# Exploite itertools pour répéter et compter jusqu'à la condition d'arrêt
gen = iter(lambda s=[A,B,C]: (s.append(update(s[-3:])), s.pop(0), s[:3])[2], None)

for i, (x, y, z) in enumerate(islice(gen, 999999)):
    if any(map(lambda t: t & 1, (x, y, z))):
        print(i+1)
        break