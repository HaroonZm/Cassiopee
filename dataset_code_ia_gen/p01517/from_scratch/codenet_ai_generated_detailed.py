import sys

sys.setrecursionlimit(10**7)

# Fonction principale pour chaque dataset
def solve():
    input = sys.stdin.readline

    while True:
        N = int(input())
        if N == 0:
            break

        # Lecture des pays avec leurs caractéristiques
        # Pour accéder par index, on utilise un dictionnaire nom -> index
        countries = []
        name_to_idx = dict()
        for i in range(N):
            line = input().split()
            name = line[0]
            strength = int(line[1])
            ccount = int(line[2])
            neighbors = line[3:]
            countries.append((name, strength, neighbors))
            name_to_idx[name] = i

        # Construction du graphe avec indices
        # graphe[i] contient la liste des indices des voisins du pays i
        graph = [[] for _ in range(N)]
        for i, (name, strength, neighbors) in enumerate(countries):
            for nname in neighbors:
                graph[i].append(name_to_idx[nname])

        # Contraintes :
        # On ne peut pas choisir un pays voisin de soi-même
        # ni un pays voisin d'un pays allié
        # On cherche un ensemble de pays qui contient A1 (index 0)
        # et pour lequel ni un pays choisi ni ses voisins ne sont choisis

        # Cela correspond à choisir un ensemble indépendant dans "le carré du graphe",
        # autrement dit une solution similaire à Maximum Weight Independent Set avec contrainte supplémentaires.

        # Formule de la contrainte donnée:
        # Aucun deux alliés ne sont voisins
        # ni voisins des voisins
        # => Pour chaque pays choisi, aucun allié ne peut être son voisin ni le voisin d'un voisin (plus exactement: 
        # On ne peut PAS prendre deux pays qui sont à une distance <= 2 dans le graphe)

        # On peut modéliser cela en construisant un graphe "G2" où on relie deux pays s'ils sont voisins dans G ou 
        # à distance 2 dans G.
        # La condition d'alliance est donc qu'on choisisse un ensemble indépendant (pas d'arête entre eux) dans G2.
        # Et l'ensemble doit contenir le pays 0.

        # Construction de G2: on connecte i et j si dist(i,j) <= 2 dans G
        # Note: Tester distance 1 ou 2 entre tous les couples est possible avec N <= 40.

        # Construire une matrice d'adjacence pour G
        adj = [[False]*N for _ in range(N)]
        for i in range(N):
            for nei in graph[i]:
                adj[i][nei] = True

        # Construire G2
        # Dans G2, i et j sont reliés si:
        # - adj[i][j] == True (distance 1)
        # - ou il existe k tq adj[i][k] and adj[k][j] (distance 2)
        G2 = [[False]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if adj[i][j]:
                    G2[i][j] = True
                else:
                    # Vérifier s'il existe un k où i-k et k-j sont voisins
                    for k in range(N):
                        if adj[i][k] and adj[k][j]:
                            G2[i][j] = True
                            break

        # Maintenant on cherche un maximum-weight independent set dans G2 contenant le noeud 0.
        # N=40, on peut faire un backtracking avec bitsets pour accélérer

        weights = [countries[i][1] for i in range(N)]

        # Représentation avec bits pour accélérer:
        # On représente les voisins dans G2 sous forme de masque binaire
        neighbors_mask = [0]*N
        for i in range(N):
            mask = 0
            for j in range(N):
                if G2[i][j]:
                    mask |= 1 << j
            neighbors_mask[i] = mask

        # On doit prendre 0 (pays A1)
        # On initialise le choix avec 0 sélectionné et on ne peut pas sélectionner ses voisins.

        # Backtracking avec mémorisation:
        # On ne travaille que sur le sous-ensemble restant après avoir obligé le pays 0.

        full_set = (1 << N) - 1

        # Masques pour représenter l'état
        # chosen: pays déjà choisis (init: 0 with 0 chosen)
        # banned: pays interdits car voisins ou voisins de voisins des choisis
        # todo: ensemble des pays que l'on peut encore considérer

        # On part de:
        chosen = 1 << 0  # pays 0 choisi
        banned = neighbors_mask[0] | chosen  # voisins et le 0 lui-même bannis
        todo = full_set & (~banned)

        from functools import lru_cache

        # On garde la population (somme poids) courante
        base_strength = weights[0]

        # On réalise un maximum weight independent set dans G2 sur les noeuds dans todo
        # avec la contrainte que choisis précédemment sont dans chosen (déjà fait)

        # Le problème est que N=40, l'état est un bitmask de size 40,
        # on applique une approche de type "Maximum weighted independent set" classique
        # avec élagage.

        # Pour réduire la complexité, on va faire un maximum weight independent set dans un graphe induit par todo.
        # neighbors_mask restreint à todo.

        # Préparation du graphe pertinent restreint
        # Ici pour chaque noeud u in todo, on garde l'intersection neighbors_mask[u] & todo
        # afin de gérer le graphe induit

        # On stocke une liste des indices dans todo
        # On travaille avec la représentation bitmask todo

        # Transform todo en liste d'éléments (nodes):
        nodes = []
        for i in range(N):
            if (todo >> i) & 1:
                nodes.append(i)
        size = len(nodes)

        # Map from index in nodes to original node
        idx_to_node = nodes

        # On prépare un tableau des masques pour le graphe induit
        # neighbors_reduced[i] contient les voisins de idx_to_node[i] dans todo (indices dans 0..size-1)
        bm_index = dict()
        for i, node in enumerate(idx_to_node):
            bm_index[node] = i

        neighbors_reduced = [0]*size
        for i, node in enumerate(idx_to_node):
            mask = neighbors_mask[node] & todo  # voisins en todo
            # convertir mask en indices dans 0..size-1
            nb_mask = 0
            for j in range(size):
                if (mask >> idx_to_node[j]) & 1:
                    nb_mask |= 1 << j
            neighbors_reduced[i] = nb_mask

        w = [weights[node] for node in idx_to_node]

        # On fait un maximum weighted independent set dans ce graphe (neighbors_reduced)
        # avec taille <= 39 (car 0 est déjà pris)

        # Utilisation de recherche branch and bound et mémorisation cache

        best = 0

        # Trie les sommets par degré décroissante pour un meilleur élagage possible
        deg = [bin(neighbors_reduced[i]).count('1') for i in range(size)]
        order = sorted(range(size), key=lambda x: deg[x], reverse=True)

        # Fonction récursive avec branch and bound
        def mwis(r, current_sum):
            # r: bitmask des sommets restants
            # current_sum: somme des poids courants

            nonlocal best
            if r == 0:
                if current_sum > best:
                    best = current_sum
                return

            # Branch and bound: somme max possible = current_sum + somme des poids dans r
            # Calcul rapide de borne max:
            # On peut prendre tout les sommets non-adjacents, mais on prend la somme totale ici comme borne.
            bound = current_sum
            temp = r
            while temp:
                p = temp.bit_length() - 1
                bound += w[p]
                temp &= ~(1 << p)
            if bound <= best:
                return

            # Choisis un sommet u dans r (on prend le premier dans order qui est dans r)
            for u in order:
                if (r >> u) & 1:
                    break

            # Cas 1: on prend u
            # on enlève u + ses voisins de r
            mwis(r & ~( (1 << u) | neighbors_reduced[u]), current_sum + w[u])

            # Cas 2: on ne prend pas u
            mwis(r & ~(1 << u), current_sum)

        mwis((1 << size) - 1, 0)

        print(base_strength + best)


if __name__ == "__main__":
    solve()