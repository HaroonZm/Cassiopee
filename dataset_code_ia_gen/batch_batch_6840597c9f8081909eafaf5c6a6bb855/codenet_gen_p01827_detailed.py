import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# Le problème:
# Nous avons N employés avec leurs degrés de contribution c_i.
# Il existe M relations "de proximité" entre employés.
# Un salaire p_i est attribué à chaque employé, p_i > 0.
# Pour chaque relation entre i et j (proches), la relation d'ordre entre c_i et c_j
# doit être reflétée strictement dans p_i et p_j :
# c_i < c_j  <=>  p_i < p_j
# De plus, pour un employé i connecté à j et k, l'ordre entre c_j et c_k doit
# être respecté dans les salaires p_j et p_k.
# Il faut minimiser la somme totale des salaires p_i.

# Observation:
# La condition sur les salaires est une contrainte sur l'ordre d'intervalle des salaires
# selon les c_i, mais seulement pour les employés proches.
# On peut modéliser un graphe où chaque nœud est un employé,
# et chaque arête traduit des contraintes d'ordre entre p_i et p_j.

# Caractéristiques importantes:
# - Si c_i = c_j, alors il faut que p_i = p_j (car ni p_i < p_j ni p_j < p_i).
# - Si c_i < c_j, alors p_i < p_j strictement.
# - L'ensemble des relations (via les relations de proximité) imposent
#   ces contraintes locales qui doivent être cohérentes globalement.

# Approche:
# Pour chaque arête (a,b),
# on doit avoir c_a < c_b => p_a < p_b,
# c_a > c_b => p_a > p_b,
# c_a = c_b => p_a = p_b.

# Cela nous permet de déduire un graphe d'ordonnancement (orienté)
# et de grouper les sommets qui doivent avoir même salaire (c_i=c_j et liés).

# Étapes:
# 1) Fusionner dans les mêmes composantes fortement connexes (SCC)
#    tous les employés dont les salaires doivent être égaux (cas c_i=c_j et liés).
#    On crée donc une partition des employés en groupes où tous auront même p.

# 2) Construire un graphe quotient où chaque nœud est une composante SCC.
#    Les arcs vont dans le sens de la contrainte "plus petit salaire -> plus grand salaire".

# 3) Le graphe quotient est acyclique.
#    On affectera alors des salaires selon un DP sur ce graphe pour respecter les contraintes.
#    Chaque composante aura un salaire minimal au moins 1 + max de ses prédécesseurs.

# 4) La somme des salaires correspond à la somme des salaires de chaque employé
#    (chaque employé prend le salaire de sa composante).

# Implémentation:
# - Construire un graphe non orienté des employés en relation.
# - Pour chaque arête (u,v) :
#     - si c_u = c_v, fusionner u,v en même composante (via union-find).
# - Ensuite, construire un graphe orienté entre composants:
#     - pour chaque arête (u,v) où c_u != c_v,
#       ajouter un arc du composante de l'employé avec c plus petit vers celui avec c plus grand.
# - Faire un DP sur ce DAG pour calculer niveaux (salaires).
# - Calculer la somme des salaires.

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.sz = [1]*n

    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.sz[x] < self.sz[y]:
            x, y = y, x
        self.par[y] = x
        self.sz[x] += self.sz[y]
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

def main():
    N = int(input())
    c = list(map(int, input().split()))
    M = int(input())

    uf = UnionFind(N)

    edges = []
    for _ in range(M):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        edges.append((a,b))
        # Si contribution égale et liés, même salaire => fusion
        if c[a] == c[b]:
            uf.unite(a,b)

    # Construction graphe orienté entre composantes d'union-find
    # Chaque composante sera un noeud du graphe quotient
    comp_graph = dict()
    indeg = dict()
    for i in range(N):
        comp = uf.find(i)
        if comp not in comp_graph:
            comp_graph[comp] = []
            indeg[comp] = 0

    # Pour chaque arête d'origine, si contributions différentes,
    # ajouter un arc strict entre composantes
    for a,b in edges:
        ca = c[a]
        cb = c[b]
        comp_a = uf.find(a)
        comp_b = uf.find(b)
        if comp_a == comp_b:
            continue
        if ca < cb:
            comp_graph[comp_a].append(comp_b)
        elif ca > cb:
            comp_graph[comp_b].append(comp_a)

    # Recalculer les degrés entrants
    for u in comp_graph:
        for v in comp_graph[u]:
            indeg[v] += 1

    # DP topo: déterminer salaires minimaux par composante
    from collections import deque
    salary_comp = dict()
    q = deque()

    # Initialiser salaires à 1 pour tous les composantes
    for comp in comp_graph:
        salary_comp[comp] = 1
        if indeg[comp] == 0:
            q.append(comp)

    while q:
        u = q.popleft()
        # Propager la contrainte chez successeurs
        for v in comp_graph[u]:
            # salaire(v) > salaire(u)
            if salary_comp[v] < salary_comp[u] + 1:
                salary_comp[v] = salary_comp[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    # Calcul somme des salaires des employés
    total = 0
    for i in range(N):
        comp = uf.find(i)
        total += salary_comp[comp]

    print(total)

if __name__ == '__main__':
    main()