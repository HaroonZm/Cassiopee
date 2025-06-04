def root(i):
    """
    Trouve la racine de l'ensemble auquel appartient l'élément i.
    Parcourt récursivement le tableau des parents jusqu'à atteindre la racine.
    
    Args:
        i (int): Indice de l'élément dont on souhaite connaître la racine.

    Returns:
        int: Indice de la racine de l'ensemble contenant i.
    """
    if par[i] < 0:
        # Si par[i] est négatif, i est la racine de son ensemble
        return i
    else:
        # Sinon, retourne récursivement la racine du parent de i
        return root(par[i])

def size(a):
    """
    Calcule la taille de l'ensemble auquel appartient l'élément a.
    
    Args:
        a (int): Indice de l'élément dont on veut la taille de l'ensemble.

    Returns:
        int: Taille de l'ensemble contenant a.
    """
    # La taille est stockée sous forme négative dans par[root(a)]
    return -par[root(a)]

def union(a, b):
    """
    Fusionne les ensembles auxquels appartiennent a et b.
    Utilise l'union par taille pour minimiser la profondeur des arbres.
    
    Args:
        a (int): Indice du premier élément.
        b (int): Indice du second élément.

    Returns:
        bool: True si une fusion a eu lieu, False si a et b appartenaient déjà au même ensemble.
    """
    a = root(a)
    b = root(b)
    if a == b:
        # Les deux éléments sont déjà dans le même ensemble, aucune fusion
        return False
    # Toujours attacher le plus petit arbre au plus grand pour limiter la profondeur
    if size(a) < size(b):
        a, b = b, a
    # Ajoute la taille de l'ensemble b à celui de a (stocké sous forme négative !)
    par[a] += par[b]
    # Définit le parent de l'ensemble b vers la racine de a, fusionnant les deux ensembles
    par[b] = a
    return True

# Lecture des entrées : nombre de noeuds n et de ponts m
n, m = map(int, input().split())

# Lecture des connexions (ponts) entre les îles, sous forme de liste d'adjacence avec indices 0-based
bridge = []
for i in range(m):
    bridge.append([int(j) - 1 for j in input().split()])

# Initialisation : au départ, le nombre de paires d'îles non connectées est n*(n-1)//2
ans = [n * (n - 1) // 2]
# Initialisation de la structure Union-Find : chaque île est dans son propre ensemble (racines -1)
par = [-1 for _ in range(n)]

# On considère les ponts en ordre inverse (on construit le graphe par ajout progressif)
for a, b in bridge[::-1]:
    # Si les deux îles sont déjà connectées, le nombre de paires non connectées ne change pas
    if root(a) == root(b):
        ans.append(ans[-1])
    else:
        # Sinon, on retire du total actuel le nombre de nouvelles connexions générées par la fusion
        ans.append(ans[-1] - size(a) * size(b))
        # On fusionne les deux ensembles
        union(a, b)
# Les réponses ont été construites dans le sens inverse, on les remet dans le bon ordre
ans = ans[::-1]

# Affichage du résultat, en ignorant la première valeur (initiale)
for i in ans[1:]:
    print(i)