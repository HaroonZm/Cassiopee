import sys

MAX = 151200

# Pré-calcul des cubes et tétraèdres
cubes = []
n = 0
while True:
    c = n**3
    if c > MAX:
        break
    cubes.append(c)
    n += 1

tetrahedrals = []
n = 0
while True:
    t = n*(n+1)*(n+2)//6
    if t > MAX:
        break
    tetrahedrals.append(t)
    n += 1

# Générer tous les nombres possibles somme d'un cube + d'un tétraèdre
sums = set()
for c in cubes:
    for t in tetrahedrals:
        s = c + t
        if s <= MAX:
            sums.add(s)
        else:
            break

# Transformer en liste triée pour faire une recherche rapide
sorted_sums = sorted(sums)

# Fonction recherche binaire pour trouver le plus grand nombre <= val
def binary_search(val):
    low, high = 0, len(sorted_sums) - 1
    res = 0
    while low <= high:
        mid = (low + high) // 2
        if sorted_sums[mid] <= val:
            res = sorted_sums[mid]
            low = mid + 1
        else:
            high = mid - 1
    return res

for line in sys.stdin:
    line = line.strip()
    if line == '0':
        break
    x = int(line)
    print(binary_search(x))