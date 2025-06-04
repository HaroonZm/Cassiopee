"""
Ce script construit des matrices de blocs liés à des plans projectifs finis dits "plans de Fano généralisés" (ou systèmes de blocs de Steiner S(2,K,N)),
où chaque élément apparaît dans K blocs, chaque paire apparaît dans exactement un bloc, et chaque bloc contient K éléments.
Ici, K=38 (modifiable), et N=K^2-K+1.
"""

K = 38  # Ordre du plan projectif, modifiable pour d'autres solutions

# Calcul du nombre total de points/blocs selon la formule du plan projectif fini
N = K**2 - K + 1

# Affiche la valeur de N et K, utile pour diagnostiquer ou informer l'utilisateur
print(N, K)

# _res: matrice intermédiaire qui stocke les (K-1) éléments supplémentaires pour chaque bloc hors les "points de base"
# Elle sera de taille (K-1)^2 x (K-1)
_res = [[-1 for _ in range(K-1)] for _ in range((K-1)**2)]

# rest: tableau stockant des versions transposées partielles de _res pour la construction finale de la matrice d'incidence
rest = [[-1 for _ in range(K-1)] for _ in range(K-1)]

# Génération des identifiants pour chaque point/bloc ajoutés lors du processus itératif
id = K    # Commence à K, car 0..K-1 déjà utilisés pour points de base
start = 0 # Décalage cyclique pour éviter les répétitions et remplir _res de manière combinatoire

# Algorithme principal pour remplir _res de façon contrôlée.
# Ce bloc garantit que chaque nouvelle "ligne"/bloc aura K éléments distincts,
# construisant ainsi une structure d’incidence correcte
while N > id:
    for j in range(K-1):
        # Calcul indexé pour garantir l'unicité et éviter collisions
        idx = (K-1)*j + (start + j * ((id-1)//(K-1))) % (K-1)
        _res[idx][(id-1)//(K-1)-1] = id
    id += 1
    start = (start + 1) % (K-1)

# Construction de la partie transposée de _res pour l’assemblage final
rest = [[_res[j][i] for j in range(K-1)] for i in range(K-1)]

# Construction finale :
# 1. On commence par la première ligne/bloc, correspondant à [0, 1, ..., K-1]
ans = [[i for i in range(K)]]

# 2. Ajout des (K-1)^2 blocs principaux, chacun comprenant un élément "base" et les (K-1) associés depuis _res
for i in range(K-1):
    for j in range(K-1):
        tmp = [i] + _res[(K-1)*i + j]
        ans.append(tmp)

# 3. Ajout des K-1 derniers blocs, chacun commence par (K-1) et complète avec les lignes de rest
for i in range(K-1):
    tmp = [K-1] + rest[i]
    ans.append(tmp)

# À ce stade, ans contient N lignes, chacune avec K éléments entre 0 et N-1 (sous forme d'indices).
# On convertit les indices en numéros humains (1-based).
for i in range(N):
    ans[i] = [ans[i][j] + 1 for j in range(K)]

# Affichage de chaque bloc, chaque ligne contient K éléments
for i in range(N):
    print(*ans[i])

def check():
    """
    Vérifie que la matrice finale 'ans' constitue un design de blocs de paramètres (N, K) correct.
    Les vérifications sont les suivantes :
      - Les indices sont bien dans l'intervalle [1, N] (après normalisation).
      - Chaque bloc a K éléments distincts.
      - Chaque élément (point) figure exactement dans K blocs.
      - Chaque paire de blocs partagent au plus un point (i.e. chaque paire de points apparaît dans exactement un bloc).
    Si une condition échoue, une erreur spécifique est affichée.
    """
    # Initialisation d'un tableau associant à chaque élément la liste des indices de blocs dans lesquels il apparaît
    ids = [[] for _ in range(N)]
    for i in range(N):
        ans[i].sort()
        # Vérifie qu'aucun indice n’est hors de l’intervalle et qu’il n’y a pas de doublons dans chaque bloc
        if ans[i][0] < 1 or ans[i][-1] > N:
            exit(print("WA1"))
        for j in range(1, K):
            if ans[i][j] == ans[i][j-1]:
                exit(print("WA2"))
        for j in range(K):
            ids[ans[i][j] - 1].append(i)  # -1 pour revenir à l'index 0-based

    # Vérifie que chaque élément appartient exactement à K blocs
    for i in range(N):
        if len(ids[i]) != K:
            exit(print("WA3"))
    
    # Vérification finale : chaque paire de blocs partage au plus un point
    p = set([])
    for i in range(N):
        for j in range(len(ids[i])):
            for k in range(j):
                a, b = ids[i][j], ids[i][k]
                if (a, b) in p:  # la paire de blocs (a,b) partage déjà cet élément
                    print("WA4")
                    print(ans[a])
                    print(ans[b])
                    exit()
                p.add((a, b))

# Pour vérifier la correction de la structure après construction, décommentez :
# check()