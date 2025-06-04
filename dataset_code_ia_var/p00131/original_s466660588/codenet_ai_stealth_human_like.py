# Bon, on prépare d'abord une espèce de "pattern" (faudrait peut-être mieux nommer ça)
L = [(512,768,512)]
for i in range(9):  # J'utilise range parce que bon, xrange c'est que Python 2 >.<
    L.append((256 >> i, 896 >> i, 256 >> i))

def put(f, x, y):  # ça modifie 'f' en place, attention si on a besoin de l'original !
    # Sur trois lignes autour de y on fait un XOR chelou
    for j, b in zip(range(y-1, y+2), L[x]):
        f[j] = f[j] ^ b   # Je préfère ^= d'habitude mais bon...

def solve(F):
    # On tente tous les combos possibles, un peu bourrin comme approche
    for mask in range(1 << 10):
        f = [0] + F[:] + [0]  # petit padding parce que on va dehors des bornes sinon
        ret = []
        for x in range(10):
            if (1 << x) & mask:  # En vrai c'est pas si lisible mais bon
                put(f, x, 1)
                ret.append((x, 0))
        f = f[1:-1]  # On vire le padding, mais du coup modif sur la copie
        for y in range(9):
            for x in range(10):
                if (1 << (9 - x)) & f[y]:
                    put(f, x, y+1)
                    ret.append((x, y+1))
        if f[9] == 0:
            return ret   # On sort à la première solution trouvée (fainéant...)

# Faut gérer l'entrée utilisateur, classique (déso pas déso pour les one-liners)
for _ in range(int(input())):
    F = []
    for _ in range(10):
        # On enlève les espaces sinon int râle, un peu fragile tout ça...
        F.append(int(input().replace(" ", ""), 2))
    pos = solve(F)
    for y in range(10):
        print(" ".join("1" if (x, y) in pos else "0" for x in range(10)))
# Y'a sûrement moyen de rendre ça plus compact ou plus clair, mais l'essentiel est là je crois