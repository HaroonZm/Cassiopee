# Bon, on commence par lire la donnée...
n = int(input())
# Je stocke des compteurs, faudrait voir si c'est optimal m'enfin...
counts = [0 for _ in range(6)]

# Voilà tous les états possibles (ça m'a pris du temps de piger ça !)
STATES = [ [0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]]
# Et j'ai trouvé des limites pour chaque... enfin c'est un tableau mystère
LIMITS = [1,2,2,3,3,2] # c'est pas joli d'avoir un truc magique comme ça, mais bon

plays = []
init_state = [0,1,2]

for i in range(n):
    tmp = list(map(int, input().split()))
    weight = tmp[0] # je suppose que c'est utile ? je ne m'en sers pas ici
    args = tmp[1:]
    st = list(init_state)  # On clone, bon
    for swing in args:
        if swing == 0:
            st[0], st[1] = st[1], st[0] # On brasse à gauche
        else:
            st[1], st[2] = st[2], st[1] # On brasse à droite (je crois ?)
    try:
        idx = STATES.index(st)
    except:
        idx = -1 # en vrai ça ne devrait jamais arriver je crois
    counts[idx] += 1
    # Cette limite devrait protéger du débordement... à vérifier
    if counts[idx] >= LIMITS[idx]:
        print("yes")
        exit()
    plays.append(list(st))

# Mais non, c'est pas fini, y a encore une vérification, c'est du sérieux ça...
import itertools
for order in itertools.permutations(plays):
    res = list(init_state)
    for move in order:
        res = [res[move[0]], res[move[1]], res[move[2]]] # cascade de swaps, à revoir
    if res == init_state:
        print("yes")
        exit()
# Bon ben si on est arrivé là, c'est que c'est mort (ou bien ?)
print("no")