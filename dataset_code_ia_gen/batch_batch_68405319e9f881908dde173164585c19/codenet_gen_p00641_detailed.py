import sys
sys.setrecursionlimit(10**7)

MOD = 10007

# Fonction pour calculer x^y % mod en log(y)
def mod_pow(x, y, mod):
    result = 1
    base = x % mod
    while y > 0:
        if y & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        y >>= 1
    return result

# Classe pour trouver et union des composantes connexes (Union-Find)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.size = [1]*n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

def solve():
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break

        # Lecture des données d'entrée pour chaque famille (les partenaires et couts)
        # On construit la liste des arêtes avec (cout, u, v)
        edges = []
        # Pour vérifier la cohérence des arêtes, on ajoute l'arête entre i et b repeated from i's input
        # Attention indices dans l'entrée semblent 0-based, à vérifier sur exemples

        for i in range(n):
            b0, f0, b1, f1 = map(int, sys.stdin.readline().split())
            edges.append((f0, i, b0))
            edges.append((f1, i, b1))

        # Le graphe est construit via edges
        # On doit trouver les composantes connexes induites par toutes les arêtes
        uf = UnionFind(n)
        for cost, u, v in edges:
            uf.unite(u, v)

        # Découpage du graphe en composantes connexes
        comp_map = {}
        comp_count = 0
        for i in range(n):
            root = uf.find(i)
            if root not in comp_map:
                comp_map[root] = comp_count
                comp_count += 1

        # Collectionner les sommets par composante
        comps = [[] for _ in range(comp_count)]
        for i in range(n):
            comps[comp_map[uf.find(i)]].append(i)

        # Regrouper les arêtes par composante
        # On ne garde que les arêtes internes à une composante
        adj_comp = [[] for _ in range(comp_count)]
        # On construit aussi une structure par composante listant edges : (cost, u', v')
        # où u', v' indices locaux dans la composante
        comp_edges = [[] for _ in range(comp_count)]
        pos_in_comp = [0]*n
        for cid in range(comp_count):
            for idx, v in enumerate(comps[cid]):
                pos_in_comp[v] = idx

        for cost, u, v in edges:
            cu = comp_map[uf.find(u)]
            cv = comp_map[uf.find(v)]
            if cu == cv:
                u_local = pos_in_comp[u]
                v_local = pos_in_comp[v]
                comp_edges[cu].append((cost, u_local, v_local))

        # On veut calculer pour chaque composante le nombre de MST de poids minimal
        # puis faire le produit modulo 10007
        res = 1

        # Fonction pour calculer le nombre de MST dans une composante via MST count algorithm
        # Approche:
        # On utilise l'algorithme de Kruskal modifié pour compter les MST minimal de toute la composante
        # https://en.wikipedia.org/wiki/Spanning_tree#Counting_spanning_trees
        # En fait on utilise une méthode basée sur "Kruskal avec comptage"
        # On trie les arêtes par coût croissant
        # On procède en blocs par coût égal, 
        # on calcule le nombre de manières d'intégrer ces arêtes dans l'union-find
        # puis on multiplie le résultat par la taille du nombre de choix dans la phase
        
        from collections import defaultdict

        def count_mst(nc, edges):
            """
            nc : nombre de sommets locale dans la composante
            edges: liste de tuples (cost, u, v)
            """
            edges.sort(key=lambda x:x[0])
            uf_local = UnionFind(nc)
            ans = 1
            i = 0
            m = len(edges)
            while i < m:
                cost = edges[i][0]
                # Sous-liste des arêtes avec même coût
                j = i
                while j < m and edges[j][0] == cost:
                    j += 1
                same_cost_edges = edges[i:j]
                # Graphe induit par ces arêtes
                # On doit compter les MST sur ces arêtes restreints aux composantes courantes dans uf_local
                
                # Regrouper les sommets de ces arêtes qui sont dans composantes différentes dans uf_local
                temp_nodes = set()
                for _, u, v in same_cost_edges:
                    temp_nodes.add(uf_local.find(u))
                    temp_nodes.add(uf_local.find(v))
                # On ne travaille que sur le graphe induit par ces racines dans uf_local
                
                # Map des anciens sommets à 0..k-1
                roots_list = sorted(temp_nodes)
                root_idx = {r: idx for idx, r in enumerate(roots_list)}
                k = len(roots_list)
                if k == 1:
                    # Toutes les arêtes entre même racine, aucune influence sur MST
                    # Juste on unit celles permettant
                    for _, u, v in same_cost_edges:
                        uf_local.unite(u,v)
                    i = j
                    continue

                # Graphe construit sur ces racines
                # Construire la liste d'arêtes entre roots
                graph = [[] for _ in range(k)]
                edge_list = []
                for _, u, v in same_cost_edges:
                    ru = uf_local.find(u)
                    rv = uf_local.find(v)
                    u0 = root_idx[ru]
                    v0 = root_idx[rv]
                    if u0 != v0:
                        graph[u0].append(v0)
                        graph[v0].append(u0)
                        edge_list.append((u0, v0))
                # Enlever les multi-arêtes sur le même couple (u,v)
                # Ici on doit utiliser un set pour edges
                unique_edges = set()
                for u0, v0 in edge_list:
                    if u0 > v0:
                        u0, v0 = v0, u0
                    unique_edges.add((u0, v0))
                unique_edges = list(unique_edges)

                # Le graphe sur racines est non orienté avec k sommets et unique_edges arêtes
                # On cherche le nombre d'arbres couvrants dans ce graphe complet formé par ces arêtes
                # Cela correspond au nombre d'arbres couvrants d'un graphe donné
                # On l'obtient en construisant la matrice de Laplace et calculant son déterminant principal

                # Construire la matrice de Laplace (k x k)
                # L[i][i] = degré de i
                # L[i][j] = -nombre d'arêtes entre i et j (ici 0 ou 1)
                import numpy as np

                L = np.zeros((k,k), dtype=int)
                deg = [0]*k
                for u0,v0 in unique_edges:
                    deg[u0] += 1
                    deg[v0] += 1
                for i_ in range(k):
                    L[i_, i_] = deg[i_]
                for u0,v0 in unique_edges:
                    L[u0,v0] = L[v0,u0] = -1

                # Calcul du déterminant principal (on enlève une ligne et colonne)
                # Ici on ne va garder que la matrice (k-1 x k-1)
                mat = L[1:,1:]

                # Calcul du déterminant modulo MOD
                # NumPy by default does float, on doit faire nous meme le déterminant modulo avec méthode LU

                def determinant_mod(mat, mod):
                    n = mat.shape[0]
                    mat = mat.copy()
                    res = 1
                    for i_ in range(n):
                        pivot = -1
                        for r_ in range(i_, n):
                            if mat[r_, i_] % mod != 0:
                                pivot = r_
                                break
                        if pivot == -1:
                            return 0
                        if pivot != i_:
                            mat[[pivot, i_]] = mat[[i_, pivot]]
                            res = (-res) % mod
                        res = (res * mat[i_, i_]) % mod
                        inv = pow(int(mat[i_, i_]), mod-2, mod)  # inverse modulaire
                        for r_ in range(i_+1, n):
                            if mat[r_, i_] != 0:
                                fac = (mat[r_, i_] * inv) % mod
                                mat[r_, i_] = 0
                                for c_ in range(i_+1, n):
                                    mat[r_, c_] = (mat[r_, c_] - fac * mat[i_, c_]) % mod
                    return res % mod

                count = determinant_mod(mat, MOD)

                # Multiplier le résultat courant
                ans = (ans * count) % MOD

                # Union toutes les arêtes dans uf_local
                for _, u, v in same_cost_edges:
                    uf_local.unite(u, v)

                i = j

            return ans

        for cid in range(comp_count):
            nc = len(comps[cid])
            if nc == 1:
                # Composante singleton, 1 façon de construire clan
                continue
            ways = count_mst(nc, comp_edges[cid])
            res = (res * ways) % MOD

        print(res)


if __name__ == "__main__":
    solve()