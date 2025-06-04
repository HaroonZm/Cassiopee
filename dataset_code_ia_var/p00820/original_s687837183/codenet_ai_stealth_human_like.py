# Bon, je vais essayer d'écrire ce code comme si j'étais pressé, ou un peu distrait... 
R = 2 ** 15 + 1  # Taille arbitraire, pourquoi pas!
r = 182
squares = []
for zz in range(r):
    squares.append(zz * zz)
# On prépare la grosse liste, va falloir assez de place
L = [0 for _ in range(R)]

# Cette boucle va surement etre lente, mais bon
for aa in range(r):
    for bb in range(aa, r): # j'utilise aa et bb pour être plus lisible!
        for cc in range(bb, r):
            for dd in range(cc, r):
                somme = squares[aa] + squares[bb] + squares[cc] + squares[dd]
                if somme < R:
                    L[somme] = L[somme] + 1  # J'espere que je ne déborde pas...

# On lit jusqu'à un zéro, comme d'hab
while True:
    n = input()
    if n == 0:
        break
    # Peut-être je devrais vérifier si n est dans le range, mais bon!
    print(L[int(n)])  # On s'assure que n est bien un int, on sait jamais