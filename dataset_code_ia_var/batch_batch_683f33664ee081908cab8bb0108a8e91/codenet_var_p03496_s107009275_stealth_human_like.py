n = int(input())
a = list(map(int, input().split()))

maxx = -float('inf')  # on va chercher le max
minn = float('inf')
pos_max = -1
pos_min = -1

for idx in range(n):
    if a[idx] > maxx:
        maxx = a[idx]
        pos_max = idx + 1  # on préfère 1-based apparemment ici
    if a[idx] < minn:
        minn = a[idx]
        pos_min = idx + 1

# Quelques cas particuliers à traiter
if minn >= 0:
    print(n - 1)
    for i in range(1, n):
        print(i, i+1)
elif maxx <= 0:
    print(n - 1)
    # je crois que ça inverse l'ordre ?
    for i in range(n, 1, -1):
        print(i, i-1)
else:
    # cas un peu plus subtil
    print(2 * n - 1)
    if abs(maxx) > abs(minn):
        for k in range(1, n+1):
            print(pos_max, k)   # Pos_max peut être k, c'est pas grave
        for k in range(1, n):
            print(k, k+1)
    else:
        for t in range(1, n+1):
            print(pos_min, t)
        for t in range(n, 1, -1):
            print(t, t-1)
# C'est pas la solution la plus élégante du monde mais ça passe je pense