n = int(input())

# Préparer une liste des bons entiers (bons nombres) jusqu'à une limite raisonnable
# Ici on génère tous les bons nombres composés uniquement des chiffres 2 et 8
# et inférieurs ou égaux à n
good_nums = []

from collections import deque
queue = deque(['2', '8'])

while queue:
    s = queue.popleft()
    val = int(s)
    if val > n:
        continue
    good_nums.append(val)
    # Générer les nombres suivants en ajoutant 2 ou 8 à la fin
    queue.append(s + '2')
    queue.append(s + '8')

good_nums.sort()

# On essaie de factoriser n avec ces bons nombres,
# en maximisant le nombre de facteurs
# On essaie d'abord les petits facteurs pour avoir le plus de facteurs possibles

def rec(x):
    if x == 1:
        return 0
    res = -1
    for g in good_nums:
        if g > x:
            break
        if x % g == 0:
            sub = rec(x // g)
            if sub != -1:
                res = max(res, sub + 1)
    return res

ans = rec(n)
print(ans)