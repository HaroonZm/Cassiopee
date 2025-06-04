from collections import deque
import sys

# Read input quickly
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    """
    Résout une instance d'un problème de graphe soumis en entrée standard.
    Effectue une opération de type MST en distinguant les arêtes de type "A" et "B".
    Modifie si nécessaire le nombre d'arêtes de type "A" dans l'arbre pour atteindre un motif cible donné par K.
    Retourne True pour continuer, False pour arrêter la résolution de nouvelles instances (si N == 0).
    """
    # Lecture des paramètres du problème : nombre de sommets N, nombre d'arêtes M, nombre d'arêtes type "A" requises K
    N, M, K = map(int, readline().split())
    if N == 0:
        # Condition d'arrêt : si N vaut 0, il n'y a plus de cas à traiter
        return False

    # Structure pour Union-Find (disjoint-set) avec compression de chemin
    def root(x):
        """
        Retourne la racine de x dans l'ensemble disjoint.
        Applique la compression de chemin pour accélérer les recherches futures.
        """
        if prt[x] == x:
            return x
        # Compression de chemin
        prt[x] = y = root(prt[x])
        return y

    def unite(x, y):
        """
        Connecte deux ensembles contenant x et y. Retourne 1 si une fusion a eu lieu, 0 sinon (déjà connectés).
        """
        px = root(x)
        py = root(y)
        if px == py:
            return 0
        # Rattache le plus grand indice au plus petit (arbitraire mais garantit la terminaison)
        if px < py:
            prt[py] = px
        else:
            prt[px] = py
        return 1

    # Construction de la liste des arêtes : (poids, sommet u, sommet v, type)
    # type = 0 pour "A", 1 pour "B"
    E = []
    for i in range(M):
        u, v, w, l = readline().strip().split()
        u = int(u)
        v = int(v)
        w = int(w)
        if l == "A":
            E.append((w, u-1, v-1, 0))
        else:
            E.append((w, u-1, v-1, 1))

    # Trie de toutes les arêtes par poids croissant (Kruskal)
    E.sort()

    # U[i] indiquera si l'arête i est sélectionnée dans l'arbre actuel
    U = [0] * M
    cnt = 0       # Nombre d'arêtes "A" dans l'arbre courant
    ec = 0        # Nombre total d'arêtes dans l'arbre courant
    ans = 0       # Coût total de l'arbre

    # Initialisation de la structure Union-Find pour N sommets
    prt = list(range(N))

    # Construction initiale de l'arbre : algorithme de Kruskal
    for i, (w, u, v, d) in enumerate(E):
        if unite(u, v):
            U[i] = 1
            if d == 0:
                cnt += 1
            ec += 1
            ans += w

    # Vérifie si on a obtenu un arbre couvrant (N-1 arêtes)
    if ec != N-1:
        write("-1\n")
        return True

    # On détermine quel type d'arêtes on veut manipuler en fonction de la position par rapport à K
    if cnt < K:
        # Il manque des arêtes de type "A" : on va échanger des "B" contre des "A"
        m = 0
    else:
        # Il y a trop d'arêtes de type "A" : on va échanger des "A" contre des "B"
        m = 1

    # Préparation pour les échanges
    que = deque()
    used = [0]*N            # Marqueur des sommets visités dans BFS
    zeros = [0]*N           # Patron pour réinitialiser 'used'

    # Construction du graphe à partir de l'arbre sélectionné
    # Chaque arête garde en mémoire son indice si ce n'est pas du bon type pour échange
    G = [[] for _ in range(N)]
    for i in range(M):
        if not U[i]:
            continue
        w, u, v, d = E[i]
        if d == m:
            # Arête du type à renforcer
            G[u].append((v, 0, -1))
            G[v].append((u, 0, -1))
        else:
            # Arête du type opposé, potentiellement à retirer/remplacer
            G[u].append((v, w, i))
            G[v].append((u, w, i))

    # On procède à abs(K - cnt) échanges d'arêtes
    for t in range(abs(K - cnt)):
        s = 10**18    # Meilleur gain de coût trouvé
        p = q = -1    # p : indice d'arête à ajouter, q : indice d'arête à enlever

        # Parcours de toutes les arêtes non utilisées de type m pour échange
        for i in range(M):
            if U[i]:
                continue
            wi, ui, vi, di = E[i]
            if di != m:
                continue

            # BFS pour trouver la plus coûteuse arête du mauvais type sur un chemin ui->vi
            que.append((ui, 0, -1))
            used[:] = zeros
            used[ui] = 1
            while que:
                u, r, j = que.popleft()
                if u == vi:
                    # Terminaison BFS pour ce chemin
                    wj = r
                    break
                for v, w, k in G[u]:
                    if used[v]:
                        continue
                    if k != -1 and r < w:
                        # Candidat à l'échange potentiel (arête à fort coût)
                        que.append((v, w, k))
                    else:
                        # On propage la valeur max du chemin
                        que.append((v, r, j))
                    used[v] = 1
            que.clear()
            # Si nouveau minimum trouvé (amélioration de coût s)
            if wi - wj < s and j != -1:
                s = wi - wj
                p = i
                q = j

        # Si aucun échange possible, il est impossible d'atteindre le bon nombre d'arêtes "A"
        if p == -1:
            write("-1\n")
            return True

        # On effectue l'échange : supprime arête q, ajoute arête p
        wq, uq, vq, dq = E[q]
        # Suppression de l'arête q dans G
        g = G[uq]
        for i in range(len(g)):
            if g[i][0] == vq:
                g.pop(i)
                break
        g = G[vq]
        for i in range(len(g)):
            if g[i][0] == uq:
                g.pop(i)
                break

        # Ajout de l'arête p dans G
        wp, up, vp, dp = E[p]
        G[up].append((vp, 0, -1))
        G[vp].append((up, 0, -1))
        U[p] = 1
        U[q] = 0
        ans += s    # Mise à jour du coût global

    # Affichage du résultat pour ce cas
    write("%d\n" % ans)
    return True

# Boucle principale : résout les cas jusqu'à rencontre de N == 0
while solve():
    ...