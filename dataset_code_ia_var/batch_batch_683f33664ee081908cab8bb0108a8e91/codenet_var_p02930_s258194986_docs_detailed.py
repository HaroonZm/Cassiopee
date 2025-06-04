"""
Ce script génère et affiche les niveaux des arêtes d'un graphe particulier basé sur une construction récursive.
Chaque fonction et chaque section sont accompagnées de commentaires détaillés et de docstrings.
Le script est compatible Python 2 (utilisation de raw_input).
"""

# Permet la compatibilité Python 2 où raw_input lit une ligne entrée par l'utilisateur
input = raw_input

# Lecture de la taille du graphe
N = int(input())

# Matrice pour niveaux (non-utilisée dans cette version, pourrait servir à d'autres calculs)
levels = [[0 for j in range(501)] for i in range(501)]

# Tableau contenant le nombre de niveaux minimum pour chaque taille de graphe
nums = [0 for i in range(501)]
nums[2] = 1  # Initialisation du nombre de niveaux pour 2 nœuds
nums[3] = 2  # Initialisation du nombre de niveaux pour 3 nœuds

# Liste de matrices d'adjacence (pour chaque taille de graphe jusqu'à 500)
graphs = [None for i in range(501)]

# Matrice d'adjacence pour un graphe de 2 nœuds spécifiques, avec le niveau des arêtes déjà fixé
graph2 = [[None, None, None],  # Ligne 0 non utilisée
          [None, None, 1],     # 1->2 a un niveau 1
          [None, 1, None]]     # 2->1 a un niveau 1
graphs[2] = graph2

# Matrice d'adjacence pour un graphe de 3 nœuds, initialisée avec les niveaux d'interconnexion
graph3 = [[None for i in range(3+1)] for j in range(3+1)]  # Initialisation 4x4 car indexations à partir de 1
graph3[1][2] = 2
graph3[1][3] = 1
graph3[2][1] = 2
graph3[2][3] = 1
graph3[3][1] = 1
graph3[3][2] = 1
graphs[3] = graph3

def get_graph(cur_graph, nodes):
    """
    Met à jour la matrice d'adjacence de sous-graphe donné, en recalculant les niveaux des arêtes basés sur un vieux modèle.

    Args:
        cur_graph (list): La matrice d'adjacence du graphe courant à modifier (tableau [N+1][N+1]).
        nodes (list): Liste des numéros des nœuds du sous-graphe à incorporer.
    
    Returns:
        list: La matrice d'adjacence mise à jour, avec la profondeur des arêtes augmentée d'un niveau.
    """
    n_nodes = len(nodes)

    old_graph = graphs[n_nodes]  # On récupère la matrice d'un graphe déjà généré de taille appropriée

    # Les nouveaux et anciens index de nœud pour mapping
    new_nodes = nodes
    old_nodes = list(range(1, n_nodes+1))

    # On parcourt toutes les paires de nœuds pour appliquer les niveaux d'arêtes du sous-graphe précédent
    for i, new_node1 in enumerate(new_nodes):
        old_node1 = i + 1
        for j2, new_node2 in enumerate(new_nodes[i+1:]):
            j = i + j2 + 1
            old_node2 = j + 1
            # On augmente le niveau de l'ancienne connexion d'une unité dans la matrice courante
            cur_graph[new_node1][new_node2] = old_graph[old_node1][old_node2] + 1

    return cur_graph

# Génération récursive des graphes de taille 4 à N
for n in range(4, N+1):
    n1 = n // 2       # Division du graphe en deux groupes à peu près égaux
    n2 = n1

    if n % 2 == 1:
        n1 += 1       # Si n est impair, le premier groupe prend un élément de plus

    # Création des groupes de nœuds (leurs indices)
    nodes1 = [i for i in range(1, n1+1)]                            # Groupe 1 : indices 1 à n1
    nodes2 = [i for i in range(n1+1, n+1)]                          # Groupe 2 : indices n1+1 à n

    # Initialisation de la matrice d'adjacence pour n nœuds
    cur_graph = [[None for i in range(n+1)] for j in range(n+1)]

    # Connexion des nœuds de chaque groupe au niveau 1 entre les deux groupes
    for node1 in nodes1:
        for node2 in nodes2:
            cur_graph[node1][node2] = 1
            cur_graph[node2][node1] = 1

    # Calcul du nombre de niveaux pour ce graphe, basé sur les sous-graphes
    nums[n] = 1 + max(nums[n1], nums[n2])

    # Application récursive du schéma sur chaque sous-groupe, en élevant le niveau des anciennes arêtes
    cur_graph = get_graph(cur_graph, nodes1)
    cur_graph = get_graph(cur_graph, nodes2)

    # Sauvegarde du graphe construit de taille n
    graphs[n] = cur_graph

# Affichage ligne par ligne, pour chaque nœud i, des arêtes (i, j) avec i < j
cur_graph = graphs[N]
for i in range(1, N+1):
    out_txt = " ".join([str(cur_graph[i][j]) for j in range(i+1, N+1)])
    print(out_txt)
# La variable nums[N] donne le nombre de niveaux du graphe final (non affichée ici)