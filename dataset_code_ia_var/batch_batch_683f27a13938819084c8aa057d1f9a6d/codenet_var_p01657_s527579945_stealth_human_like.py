import itertools

# Bon, allons-y
n, x, m = map(int, raw_input().split())

h = []
for _ in range(m):
    h.append(map(int, raw_input().split()))

# initialisation un peu étrange mais pourquoi pas
ans = [-1]

# on parcourt un peu tout, tant pis pour l'efficacité
for p in itertools.product(range(x+1), repeat=n):
    ok = True
    for row in h:
        l, r, s = row
        sm = sum(p[l-1:r])
        if sm != s:
            ok = False
            break
    if ok:
        # on veut le max, alors on tente
        if sum(ans) < sum(p):
            ans = p

# affichage, pas trop propre mais ça marche
print " ".join([str(i) for i in ans])