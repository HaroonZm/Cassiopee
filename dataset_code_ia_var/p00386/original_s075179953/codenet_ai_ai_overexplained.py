import sys  # Importation du module sys, qui permet d'accéder à certaines variables et fonctions interagissant fortement avec l'interpréteur Python

# Remplacement de la limite maximale de récursion autorisée dans le programme.
# Par défaut, la limite est autour de 1000, ce qui est peu pour les arbres très profonds.
# Cela sert principalement à se prémunir contre un dépassement de pile lors d’appels récursifs.
sys.setrecursionlimit(1000000)

# Définition de la fonction principale du programme, qui sera appelée à la fin
def main():
    # Lecture de deux entiers depuis l'entrée standard, représentant respectivement :
    # n : nombre de sommets (noeuds) dans l'arbre
    # q : nombre de requêtes à traiter
    n, q = map(int, input().split())
    # Initialisation d'une liste de listes vides de taille n pour stocker les arêtes du graphe
    # edges[i] contiendra une liste des tuples (voisin, poids) connectés au noeud i
    edges = [[] for _ in range(n)]
    # On lit n-1 lignes (car un arbre avec n noeuds possède n-1 arêtes)
    for _ in range(n - 1):
        # Lecture des entiers u, v, w : arête entre u et v de poids w
        u, v, w = map(int, input().split())
        u -= 1  # Transformation des indices en indices à base 0 (Python commence à 0)
        v -= 1
        edges[u].append((v, w))  # On ajoute (v, poids) à la liste d'adjacence de u
        edges[v].append((u, w))  # Idem pour v, car l'arbre est non orienté

    # Initialisation d'une liste contenant la hauteur (= profondeur depuis la racine) de chaque noeud
    # A l'initialisation, aucune hauteur n'est connue, donc on met None pour chaque noeud.
    height = [None] * n
    # Initialisation d'une liste contenant la distance cumulée depuis la racine jusqu'à chaque noeud
    # On utilise None pour indiquer une distance encore indéfinie (non visitée)
    dist = [None] * n
    # Construction d'un tableau pour la remontée binaire ("binary lifting") de chaque noeud
    # parent[i][j] contiendra le parent à 2^j niveaux au-dessus du noeud i
    # On met None partout pour l'instant
    parent = [[None] * 20 for _ in range(n)]
    # On utilise une pile pour parcourir l'arbre sans récursion (DFS itératif)
    # Chaque élément de la pile est un tuple (noeud courant, sa profondeur, sa distance depuis la racine)
    stack = [(0, 0, 0)]  # On commence par le noeud racine (ici le 0)
    while stack:
        # On dépile un élément
        x, h, d = stack.pop()
        # On attribue la profondeur et la distance à ce noeud
        height[x] = h
        dist[x] = d
        # On parcourt tous les voisins du noeud x
        for to, w in edges[x]:
            # Si le fils 'to' n'est pas encore visité (sa hauteur est None)
            if height[to] == None:
                parent[to][0] = x  # On note que son parent direct est x (pour la montée binaire)
                stack.append((to, h + 1, d + w))  # On l'ajoute à la pile avec sa profondeur et distance

    # Prétraitement pour la montée binaire (remplir le tableau parent[][] pour toutes puissances de 2 jusqu'à 2^19)
    for j in range(1, 20):
        for i in range(1, n):  # On peut sauté le noeud racine (i=0) car il n'a pas de parent
            # Vérification qu’il existe un ancêtre à cette profondeur
            if height[i] >= 2 ** j:
                # On met à jour le parent à distance 2^j à partir du parent à distance 2^(j-1)
                parent[i][j] = parent[parent[i][j - 1]][j - 1]

    # Fonction permettant de remonter n niveaux au-dessus du noeud x dans l'arbre
    def adj_height(x, n):
        if n == 0:  # Si on ne doit pas remonter, on retourne simplement x
            return x
        acc = 1  # acc servira à repérer la puissance de 2 courante qu'on doit franchir
        for i in range(20):  # On peut aller jusqu'à 2^19 niveaux
            if acc > n:  # Si la puissance de 2 courante dépasse la hauteur à remonter
                # On appelle récursivement la fonction pour finir la montée
                return adj_height(parent[x][i - 1], n - acc // 2)
            acc *= 2  # On passe à la puissance de 2 suivante

    # Fonction auxiliaire calculant le LCA (Lowest Common Ancestor, plus proche ancêtre commun) entre x et y
    # Suppose que x et y sont déjà à la même profondeur
    def _lca(x, y):
        if x == y:
            return x  # Le LCA de deux noeuds identiques est eux-mêmes
        for i in range(1, 20):
            # Si les parents à 2^i sont les mêmes, c'est qu'on peut s'arrêter juste avant
            if parent[x][i] == parent[y][i]:
                # On recommence la recherche un cran en dessous (2^(i-1)), de façon récursive
                return _lca(parent[x][i - 1], parent[y][i - 1])

    # Fonction générale de calcul du LCA entre deux noeuds quelconques
    def lca(x, y):
        diff = height[x] - height[y]  # On calcule la différence de hauteur entre les deux noeuds
        if diff < 0:
            # Si y est plus bas que x, on remonte y pour l’aligner à la profondeur de x
            y = adj_height(y, -diff)
        elif diff > 0:
            # Si x est plus bas, on le remonte pour l’aligner à la profondeur de y
            x = adj_height(x, diff)
        # Une fois à la même hauteur, on calcule leur LCA commun
        return _lca(x, y)

    # Fonction binaire pour trouver un noeud sur la chaîne des parents dont la distance cumulée est >= target
    # index : noeud de départ ; target : distance recherchée depuis la racine
    def bs(index, target):
        if index == 0:
            return 0  # Si on atteint la racine, c'est le plus haut
        # Si le noeud courant est dans l’intervalle recherché
        if dist[index] >= target >= dist[parent[index][0]]:
            return index
        # On cherche la puissance de 2 la plus grande tout en restant >= target
        for i in range(1, 20):
            if parent[index][i] == None or dist[parent[index][i]] <= target:
                # On recule d’une puissance de 2 et on continue la recherche récursive
                return bs(parent[index][i - 1], target)

    # Fonction de calcul de la distance maximale entre trois noeuds x, y, z et un point r sur l'arbre
    # Utilisée dans les calculs du score
    def max_dist(x, y, z, r):
        # On calcule le LCA de chacun avec r
        xr = lca(x, r)
        yr = lca(y, r)
        zr = lca(z, r)
        # On retourne la plus grande distance entre r et les trois noeuds testés
        # La distance entre deux noeuds u et v dans l'arbre = dist[u] + dist[v] - 2*dist[lca(u, v)]
        return max(dist[x] + dist[r] - dist[xr] * 2,
                   dist[y] + dist[r] - dist[yr] * 2,
                   dist[z] + dist[r] - dist[zr] * 2)

    # Fonction interne calculant le score d'un trio (x, y, z) dans l'ordre, avec deux LCAs fournis
    def _score(x, y, z, xy, yz):
        dist_x = dist[x]
        dist_y = dist[y]
        dist_z = dist[z]
        dist_xy = dist[xy]
        dist_yz = dist[yz]
        dx = dist_x + dist_yz - dist_xy * 2
        dy = dist_y - dist_yz
        dz = dist_z - dist_yz
        # De nombreux cas à traiter selon les relations entre dx, dy, dz
        if dx >= dy >= dz:
            # On compare les distances pour choisir où placer le point r puis on utilise la recherche binaire
            if dist_x >= dist_y:
                r = bs(x, dist_xy + (dist_x - dist_y) / 2)
                if r == 0:
                    return dist_x
                # Retourne le minimum des deux maximums obtenus par les deux endroits potentiels
                return min(max(dist_x - dist[r], dist_y + dist[r] - dist_xy * 2),
                           max(dist_x - dist[parent[r][0]], dist_y + dist[parent[r][0]] - dist_xy * 2))
            else:
                r = bs(yz, dist_xy + (dist_y - dist_x) / 2)
                if r == 0:
                    return dist_y
                return min(max(dist_y - dist[r], dist_x + dist[r] - dist_xy * 2),
                           max(dist_y - dist[parent[r][0]], dist_x + dist[parent[r][0]] - dist_xy * 2))

        elif dx >= dz >= dy:
            if dist_x >= dist_z:
                r = bs(x, dist_xy + (dist_x - dist_z) / 2)
                if r == 0:
                    return dist_x
                return min(max(dist_x - dist[r], dist_z + dist[r] - dist_xy * 2),
                           max(dist_x - dist[parent[r][0]], dist_z + dist[parent[r][0]] - dist_xy * 2))
            else:
                r = bs(yz, dist_xy + (dist_z - dist_x) / 2)
                if r == 0:
                    return dist_z
                return min(max(dist_z - dist[r], dist_x + dist[r] - dist_xy * 2),
                           max(dist_z - dist[parent[r][0]], dist_x + dist[parent[r][0]] - dist_xy * 2))

        elif dy >= dx >= dz:
            r = bs(y, dist_yz + (dy - dx) / 2)
            if r == 0:
                return dist_y
            return min(max(dist_y - dist[r], dist_x + dist[r] - dist_xy * 2),
                       max(dist_y - dist[parent[r][0]], dist_x + dist[parent[r][0]] - dist_xy * 2))

        elif dy >= dz >= dx:
            r = bs(y, dist_yz + (dy - dz) / 2)
            if r == 0:
                return dist_y
            return min(max(dist_y - dist[r], dist_z + dist[r] - dist_yz * 2),
                       max(dist_y - dist[parent[r][0]], dist_z + dist[parent[r][0]] - dist_yz * 2))

        elif dz >= dx >= dy:
            r = bs(z, dist_yz + (dz - dx) / 2)
            if r == 0:
                return dist_z
            return min(max(dist_z - dist[r], dist_x + dist[r] - dist_xy * 2),
                       max(dist_z - dist[parent[r][0]], dist_x + dist[parent[r][0]] - dist_xy * 2))

        elif dz >= dy >= dx:
            r = bs(z, dist_yz + (dz - dy) / 2)
            if r == 0:
                return dist_z
            return min(max(dist_z - dist[r], dist_y + dist[r] - dist_yz * 2),
                       max(dist_z - dist[parent[r][0]], dist_y + dist[parent[r][0]] - dist_yz * 2))

    # Fonction générale calculant le score principal pour trois sommets a, b, c (indices 1-based à l'entrée)
    def score(a, b, c):
        a -= 1  # On convertit en indices 0-based
        b -= 1
        c -= 1
        ab = lca(a, b)  # LCA de a et b
        ac = lca(a, c)  # LCA de a et c
        bc = lca(b, c)  # LCA de b et c
        # On choisit l'ordre des paramètres et lesquels passer à _score pour chaque cas
        if ab == ac:
            return _score(a, b, c, ab, bc)
        elif ab == bc:
            return _score(b, a, c, ab, ac)
        else:
            return _score(c, a, b, ac, ab)

    # Traitement de chaque requête : on lit a, b, c puis on affiche le score associé
    for _ in range(q):
        a, b, c = map(int, input().split())
        print(score(a, b, c))

# Appel de la fonction principale afin d'exécuter le code si ce fichier est lancé indépendamment
main()