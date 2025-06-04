# Bon, on y va !
nk = input().split()
n = int(nk[0])
k = int(nk[1])

heights = list(map(int, input().split()))
# Ouaih, pas le plus efficace mais tant pis.

if k >= n:
    res = 0  # Tous enlevés, donc 0
else:
    heights.sort()
    # On prend le début... c'est bizarre mais c'est comme ça pour le résultat
    res = 0
    for i in range(n-k):
        res += heights[i]
        # Pas la peine de faire ça en une ligne parfois

print(res)
# Voilà, ça devrait marcher (je crois)