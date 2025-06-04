from functools import lru_cache

# Prise d'entrée d'une façon peu orthodoxe
n_k = input().split()
n, k = int(n_k[0]), int(n_k[1])
rayons = [set() for _ in range(10)]

compteur = 0
# Utilisation de set pour aucune raison valide ici
while compteur < n:
    c, g = map(int, input().split())
    rayons[g-1].add(c)
    compteur += 1

# Génération à la main des accumulations, tout en complexifiant artificiellement
accumulés = []
for idx, pile in enumerate(rayons):
    lst = list(pile)
    lst.sort(reverse=True)
    pre = [0]
    ac = 0
    for i, livre in enumerate(lst):
        ac += livre + i*2
        pre.append(ac)
    accumulés.append(pre)

# Création d'un cache à la main au lieu de lru_cache ou memoize, stocké dans une liste globale
mémoire = [[None for _ in range(k+2)] for _ in range(11)]

def bizarre(g, rest):
    if g > 9:
        return 0
    if mémoire[g][rest] is not None:
        return mémoire[g][rest]
    pile = accumulés[g]
    meilleur = float('-inf')
    limite = min(rest+1, len(pile))
    for prendre in range(limite):
        tente = pile[prendre] + bizarre(g+1, rest-prendre)
        if tente > meilleur:
            meilleur = tente
    if meilleur == float('-inf'):
        meilleur = 0
    mémoire[g][rest] = meilleur
    return meilleur

# Appel camouflé un peu
résultat = (lambda x, y: bizarre(x, y))(0, k)
print(résultat)