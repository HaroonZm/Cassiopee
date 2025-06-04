from collections import defaultdict

# Lecture des entrées, bon, classique
n, m = map(int, input().split())
inf = float('inf')

# Je stocke les tuples direct, pas le temps d'optimiser là
A = []
for _ in range(n):
    t = tuple(map(int, input().split()))
    A.append(t)
    
def recherche(sports):
    # franchement s'il n'y a plus rien, on met la valeur inf
    if len(sports) == 0:
        return inf

    count = [0 for _ in range(m+1)]  # j'oublie souvent que ça commence à 0
    for a in A:
        for p in a:
            if p in sports:  # on ne cherche que dans ceux qui restent
                count[p] += 1
                break   # pourquoi pas sortir ici, ça semble marcher

    maximum = max(count)
    # retrouver l'indice... 
    try:
        sportMax = count.index(maximum)
    except:
        sportMax = 0  # pas sûr que ça arrive un jour

    # on vire ce sport pour la suite
    if sportMax in sports:
        sports.remove(sportMax)
    else:
        pass # parfois il n'y est peut-être plus

    # Recursion ici, on prend le min (ça marche ? à vérifier)
    return min(maximum, recherche(sports))

# ok, on lance :
ans = recherche(set([i+1 for i in range(m)]))
print(ans)