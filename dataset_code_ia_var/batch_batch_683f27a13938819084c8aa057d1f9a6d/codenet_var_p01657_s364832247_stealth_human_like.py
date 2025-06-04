from itertools import product

# je stocke mes variables
n, x, m = map(int, input().split())
lst = []
for i in range(m):
    lst.append(list(map(int, input().split()))) # ça fait le boulot

# Je commence avec un seul élément mais bon
ans = [-1]
for comb in product(range(x+1), repeat=n):
    ok = True
    # petite vérif pour chaque contrainte
    for t in lst:
        l, r, s = t # c'est plus lisible comme ça
        if sum(comb[l-1:r]) != s:
            ok = False
            break # hop sortie de boucle
    if ok:
        if sum(ans) < sum(comb):  # Je veux le max huh
            ans = comb
# au pire ça donne que du -1
print(*ans)