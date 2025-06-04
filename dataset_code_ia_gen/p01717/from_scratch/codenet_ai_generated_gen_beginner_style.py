N, M, K = map(int, input().split())

bad_pairs = set()
friendship = {}

for _ in range(M):
    a, b, c = map(int, input().split())
    if c == 0:
        bad_pairs.add((min(a,b), max(a,b)))
    else:
        friendship[(min(a,b), max(a,b))] = c

# On cherche une combinaison de K monstres sans paire dangereuse (c=0)
# et avec la somme des c maximisée.
# Approche simple (non optimale) : essayer toutes les combinaisons n'importe comment
# serait trop lourd. Comme M ≤ N, et chaque monstre apparait maximum deux fois dans bad_pairs,
# on peut construire un graphe avec arêtes interdites.

# Construire une liste des monstres et leurs liens interdits pour vérifier facilement
adj_bad = [[] for _ in range(N+1)]
for a,b in bad_pairs:
    adj_bad[a].append(b)
    adj_bad[b].append(a)

# On essaiera une approche brutale :
# - chercher un sous-ensemble de taille K sans aucune paire interdite dans bad_pairs,
# - parmi toutes, choisir celle avec la somme max.

# Comme N,K jusqu'à 2000, on ne peut pas essayer toutes combinaisons.
# Alors on fait une heuristique simple :
# 1. On commence par enlever tous les monstres qui ont une arête interdite vers un autre qui ne peut pas être en même temps dans la même équipe de taille K.
# 2. Si l'on ne peut pas faire de groupe de taille K en évitant bad_pairs, output Impossible.
# 3. Sinon, on peut choisir K monstres qui ne violent pas les regles.
# 4. On calculera la somme des amitiés entre eux.

# Première idée simple :
# on note que si une paire a un c=0, ils ne peuvent pas être ensemble.
# donc on peut regarder la composante de graphe formée par interdits.
# si une arête interdit, ces deux ne peuvent pas être ensemble.

# Puisqu'il s'agit d'interdits, c'est comme un graphe d'interdits.
# Le problème est de trouver un ensemble indépendant de taille K (aucune arête entre eux),
# avec la somme des amities maximisée.

# Trouver un ensemble indépendant maximum pondéré est NP-difficile,
# faire une solution naïve.

# Ici, on fera une approche naïve :
# on trie les monstres par leur "score potentiel" qui est la somme des amitiés avec les autres,
# et on essaie de prendre les meilleurs monstres en ignorant ceux qui forment une arête interdite.

# Calculer pour chaque monstre la somme des amitiés avec tous les autres
sum_friendship = [0]*(N+1)
for i in range(1,N+1):
    for j in range(i+1,N+1):
        pair = (i,j)
        c = friendship.get(pair,0)
        sum_friendship[i] += c
        sum_friendship[j] += c

monstres = list(range(1,N+1))
monstres.sort(key=lambda x: sum_friendship[x], reverse=True)

chosen = []
def can_add(x):
    for y in chosen:
        p = (min(x,y), max(x,y))
        if p in bad_pairs:
            return False
    return True

for m in monstres:
    if len(chosen) == K:
        break
    if can_add(m):
        chosen.append(m)

if len(chosen) < K:
    print("Impossible")
else:
    # calculer la somme d'amitié pour ce groupe
    total = 0
    for i in range(K):
        for j in range(i+1,K):
            p = (min(chosen[i], chosen[j]), max(chosen[i], chosen[j]))
            total += friendship.get(p,0)
    print(total)