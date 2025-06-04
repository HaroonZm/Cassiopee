import sys

# Cette solution utilise l'algorithme de reconstruction d'arbre phylogénétique UPGMA (Unweighted Pair Group Method with Arithmetic Mean),
# adapté ici pour reconstruire un arbre à partir d'une matrice de distances entre feuilles (ordinateurs).
# Le résultat final est la liste des degrés (nombre de connexions) des noeuds internes (switches) de l'arbre,
# triés en ordre croissant.

# Approche générale :
# 1) Chaque ordinateur est initialement un cluster séparé.
# 2) À chaque étape, on trouve la paire de clusters avec la distance moyenne la plus faible.
# 3) On les fusionne en un nouveau cluster (représentant un switch).
# 4) On met à jour la matrice de distances entre clusters avec la moyenne arithmétique des distances.
# 5) On répète jusqu'à obtenir un seul cluster (l'arbre complet).
# 6) On calcule les degrés des noeuds internes de l'arbre, correspondant aux switches.
#
# Remarque importante : 
# Les feuilles sont les ordinateurs et ne sont jamais internes.
# Les noeuds internes sont les switchs et ont donc un degré >= 2.
# Chaque cluster fusionné correspond à un switch.
# Le résultat est la liste (triée) des degrés de ces noeuds internes.

class Node:
    def __init__(self, idx, left=None, right=None):
        self.idx = idx           # identifiant unique du noeud
        self.left = left         # fils gauche (cluster fusionné)
        self.right = right       # fils droit (cluster fusionné)
        self.size = 1            # nombre de feuilles sous ce noeud
        self.degree = 0          # degré du noeud (nombre de connexions)
        # Le degré sera calculé ensuite à partir de la structure de l'arbre

def parse_input():
    # Lit les entrées jusqu'à '0' seul sur une ligne
    inputs = []
    lines = sys.stdin.read().strip().split('\n')
    i = 0
    while True:
        if i>=len(lines):
            break
        n = lines[i].strip()
        i += 1
        if n == '0':
            break
        n = int(n)
        matrix = []
        # les distances peuvent être sur plusieurs lignes
        while len(matrix) < n:
            row = []
            while len(row) < n:
                parts = lines[i].strip().split()
                i += 1
                row.extend(map(int, parts))
            matrix.append(row[:n])
        inputs.append((n, matrix))
    return inputs

def upgma(n, dist_matrix):
    # Initialisation : chaque feuille est un cluster initial
    clusters = [Node(i) for i in range(n)]
    active = [True]*n   # indique quels clusters sont encore actifs
    distances = {}
    # Stocker distances entre clusters dans un dict avec tuple (i,j) i<j
    for i in range(n):
        for j in range(i+1,n):
            distances[(i,j)] = dist_matrix[i][j]

    next_node_id = n    # identifiants pour noeuds internes

    # Fonction pour trouver la paire minimale
    def find_min_pair():
        min_dist = float('inf')
        min_pair = None
        for (x,y), d in distances.items():
            if active[x] and active[y]:
                if d < min_dist:
                    min_dist = d
                    min_pair = (x,y)
        return min_pair, min_dist

    # Stocker les noeuds internes pour calcul des degrés
    internal_nodes = []

    # Fusionner jusqu'à ce qu'il reste un cluster
    remaining = sum(active)
    while remaining > 1:
        (i,j), md = find_min_pair()
        # Créer noeud interne représentant la fusion
        new_node = Node(next_node_id, clusters[i], clusters[j])
        new_node.size = clusters[i].size + clusters[j].size
        internal_nodes.append(new_node)
        clusters.append(new_node)
        active.append(True)
        # Désactiver i et j
        active[i] = False
        active[j] = False
        active_count = sum(active)
        # Mise à jour des distances entre nouveau cluster et autres clusters actifs
        for k in range(len(clusters)-1):
            if active[k]:
                # calcul distance moyenne pondérée
                # distance(new,k) = (dist(i,k)*size(i) + dist(j,k)*size(j)) / (size(i) + size(j))
                # récupère distances dans distances dict (attention aux indices ordre)
                def get_dist(x,y):
                    a,b = min(x,y), max(x,y)
                    return distances[(a,b)] if (a,b) in distances else None

                di = get_dist(i,k)
                dj = get_dist(j,k)
                size_i = clusters[i].size
                size_j = clusters[j].size
                if di is None or dj is None:
                    # Peut arriver quand k = i ou j, mais on évite ces cas en testant active[k]
                    continue
                new_dist = (di*size_i + dj*size_j) / (size_i + size_j)
                # stocker nouvelle distance sous nouvel index next_node_id
                a,b = min(k,next_node_id), max(k,next_node_id)
                distances[(a,b)] = new_dist
        # enlever distances liées à i,j pour optimisation
        keys_to_remove = []
        for key in distances:
            if i in key or j in key:
                keys_to_remove.append(key)
        for key in keys_to_remove:
            del distances[key]

        next_node_id += 1
        remaining -= 1

    # Le dernier noeud actif est la racine
    root_idx = None
    for idx, act in enumerate(active):
        if act:
            root_idx = idx
            break
    root = clusters[root_idx]

    # Calculer degrés :
    # Feuilles (ordinateurs) ont degré 1.
    # Noeuds internes (switches) ont degré = nombre de voisins.
    # Dans notre arbre binaire, chaque noeud a des liens vers fils et vers son père.
    # On construit une adjacency list pour tous noeuds (feuilles + internes)
    # puis on calcule le degré des noeuds internes.

    # Construire adjacency list (dictionnaire de sets)
    adj = {}
    def add_edge(u,v):
        adj.setdefault(u,set()).add(v)
        adj.setdefault(v,set()).add(u)

    def build_adj(node):
        if node.left is not None and node.right is not None:
            add_edge(node.idx, node.left.idx)
            add_edge(node.idx, node.right.idx)
            build_adj(node.left)
            build_adj(node.right)

    build_adj(root)

    # Les feuilles sont 0..n-1, internes n.. next_node_id-1
    degrees_internal = []
    for nodeid in range(n, next_node_id):
        deg = len(adj[nodeid]) if nodeid in adj else 0
        degrees_internal.append(deg)

    degrees_internal.sort()
    return degrees_internal

def main():
    inputs = parse_input()
    for n, dist_matrix in inputs:
        degrees = upgma(n, dist_matrix)
        print(' '.join(map(str, degrees)))

if __name__ == "__main__":
    main()