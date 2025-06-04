def root(x):
    """
    Trouve le représentant (la racine) de l'ensemble auquel appartient x.
    Applique la compression de chemin pour accélérer les recherches futures.

    Args:
        x (int): Le nœud dont on cherche la racine.

    Returns:
        int: L'indice du parent racine de x.
    """
    if x == parent[x]:
        return x
    parent[x] = root(parent[x])  # Compression de chemin
    return parent[x]

def unite(x, y):
    """
    Fusionne les ensembles contenant x et y (union par ordre croissant d'index).

    Args:
        x (int): Premier nœud à unir.
        y (int): Deuxième nœud à unir.
    """
    px = root(x)
    py = root(y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

while True:
    A = []  # Liste des arêtes de type 'A'
    B = []  # Liste des arêtes de type 'B'
    n, m, k = map(int, raw_input().split())  # n: nombre de sommets, m: nombre d'arêtes, k: nombre minimal d'arêtes de type A obligatoires
    if n == m == k == 0:  # Signal de fin d'entrée
        break
    parent = range(n)  # Initialisation des parents pour Union-Find
    for i in xrange(m):
        u, v, w, l = raw_input().split()
        u = int(u) - 1  # Passage à un index base 0
        v = int(v) - 1
        w = int(w)
        if l == 'A':
            A.append((w, u, v))  # Arête de type A
        else:
            B.append((w, u, v))  # Arête de type B
    A.sort()  # Trie des arêtes par poids croissant
    B.sort()
    E = [[] for _ in xrange(n)]  # Liste d'adjacence pondérée du graphe
    ans = 0  # Coût total de l'arbre couvrant final
    cnt = 0  # Nombre d'arêtes utilisées dans l'arbre couvrant

    # 1. Ajout prioritaire des arêtes de type A pour en sélectionner au moins k
    for w, u, v in A:
        if root(u) != root(v):
            unite(u, v)
            ans += w
            # Le pointeur p indique le type d'arête ajouté : [1] pour A
            p = [1]
            E[u].append((v, w, p))
            E[v].append((u, w, p))
            cnt += 1
    if cnt < k:  # Impossible de sélectionner k arêtes de type A
        print -1
        continue
    used = [0] * len(B)  # Indique si une arête B a été utilisée
    rest = n - k - 1     # Nombre d'arêtes B nécessaires pour compléter l'arbre couvrant

    # 2. Ajout de certaines arêtes B pour terminer l'arbre couvrant
    for i, (w, u, v) in enumerate(B):
        if root(u) != root(v):
            unite(u, v)
            ans += w
            used[i] = 1  # Marque cette arête B comme utilisée
            p = [2]
            E[u].append((v, w, p))
            E[v].append((u, w, p))
            rest -= 1
            cnt += 1

    if cnt != n - 1:  # Si l'arbre couvrant n'est pas complet
        print -1
        continue

    def dfs(v, s, prev):
        """
        Recherche en profondeur pour trouver la plus lourde arête A sur le chemin v-s.
        Ignore les arêtes A déjà "désactivées" (pointeur p = 0).
        
        Args:
            v (int): Sommet de départ.
            s (int): Sommet cible.
            prev (int): Sommet précédent (pour éviter de revenir en arrière).

        Returns:
            tuple: (poids le plus lourd d'une arête A, pointeur de l'arête A), ou (-1, None) si rien trouvé.
        """
        if v == s:
            return (-1, None)
        for i, (to, w, can) in enumerate(E[v]):
            if to == prev or can[0] == 0:
                continue
            res = dfs(to, s, v)
            if res is not None:
                if can[0] == 1:
                    return max(res, (w, can))
                else:
                    return res
        return None

    # 3. Amélioration par échange (remplacement d'une coûteuse arête A par une moins coûteuse B)
    for t in xrange(rest):
        res = (10 ** 18, None, None)  # (différence de coût, index B, pointeur A)
        for i, (w, u, v) in enumerate(B):
            if used[i]:
                continue
            rr = dfs(u, v, -1)
            if rr is None:
                continue
            cost, can = rr
            if cost != -1:
                res = min(res, (w - cost, i, can))
        co, i, can = res
        if i is None:  # Pas d'amélioration possible
            print -1
            break
        ans += co
        can[0] = 0  # Désactive l'arête A échangée

        w, u, v = B[i]
        used[i] = 1
        p = [2]
        E[u].append((v, w, p))
        E[v].append((u, w, p))
    else:
        print ans  # Affiche le coût minimum trouvé
        if ans == 272:
            print A, B  # Débogage : affiche les listes d'arêtes employées