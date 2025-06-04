from sys import stdin
from collections import defaultdict

n, m = map(int, stdin.readline().split())
defs = [tuple(map(int, stdin.readline().split())) for _ in range(m)]

# On regroupe les contraintes pour chaque position
pos_constraints = defaultdict(set)
for pos, digit in defs:
    pos_constraints[pos - 1].add(digit)

# Vérifier les contradictions
if any(len(digits) > 1 for digits in pos_constraints.values()):
    print(-1)
    exit()

# Générer la solution
num = [None] * n

for i in range(n):
    if i in pos_constraints:
        num[i] = next(iter(pos_constraints[i]))

# Gestion du premier chiffre (pas de zéro en tête si n > 1)
if n == 1:
    num[0] = num[0] if num[0] is not None else 0
else:
    if num[0] is not None:
        if num[0] == 0:
            print(-1)
            exit()
    else:
        num[0] = 1
    for i in range(1, n):
        if num[i] is None:
            num[i] = 0

print(''.join(map(str, num)))