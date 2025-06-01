def check_conflict(n, x):
    # petite fonction pour tester si n et x ont des valeurs incompatibles
    for idx in range(9):
        if n[idx] != -1 and n[idx] != x[idx]:
            return True
    return False

import itertools

digits = [1,2,3,4,5,6,7,8,9]
count = 0
n = list(map(int, input().split()))  # on récupère la liste des contraintes

for perm in itertools.permutations(digits):
    if check_conflict(n, perm):
        continue
    # la condition un peu compliquée à vérifier
    val = perm[0] + perm[2] + perm[5] - perm[8] + (perm[1] + perm[4] - perm[7]) * 10 + (perm[3] - perm[6]) * 100
    if val == 0:
        count += 1

print(count)