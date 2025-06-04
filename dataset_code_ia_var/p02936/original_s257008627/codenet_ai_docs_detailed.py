from collections import deque

def build_tree(n, edge_list):
    """
    Construit la représentation par listes d'adjacence d'un arbre non orienté.

    Args:
        n (int): Nombre de sommets dans l'arbre.
        edge_list (list of tuple): Liste des arêtes, chaque arête étant une paire (a, b).

    Returns:
        list: Liste d'adjacence où chaque index i contient une liste des sommets adjacents à i.
    """
    tree = [[] for _ in range(n + 1)]  # Initialisation d'une liste vide pour chaque sommet (1-indicé)
    for a, b in edge_list:
        tree[a].append(b)  # Ajoute b à la liste des voisins de a
        tree[b].append(a)  # Ajoute a à la liste des voisins de b (car non orienté)
    return tree

def propagate_counts(n, tree, cnt):
    """
    Propagation des valeurs cumulées le long de l'arbre à partir du sommet racine (1).

    Args:
        n (int): Nombre de sommets dans l'arbre.
        tree (list): Liste d'adjacence représentant l'arbre.
        cnt (list): Liste contenant la valeur initiale de chaque sommet (1-indicé).

    Returns:
        list: Liste mise à jour où chaque sommet i contient la somme des valeurs cumulées jusqu'à lui.
    """
    stack = deque()       # Utilisé pour un parcours type DFS itératif
    stack.append(1)       # On commence depuis la racine (supposée être 1)
    checked = set()       # Garde trace des sommets déjà parcourus

    while stack:
        node = stack.pop()       # On traite le sommet en haut de la pile
        checked.add(node)        # Marque le sommet comme visité
        for neighbor in tree[node]:
            if neighbor not in checked:    # Si le voisin n'a pas encore été traité
                stack.append(neighbor)     # Ajoute le voisin à la pile pour prochain traitement
                cnt[neighbor] += cnt[node] # Propage la somme cumulative au voisin

    return cnt

def main():
    """
    Fonction principale pour gérer la lecture d'entrée, les appels aux fonctions de construction d'arbre,
    la propagation des valeurs, et l'affichage du résultat.
    """
    # Lecture du nombre de sommets (n) et du nombre de requêtes (q)
    n, q = map(int, input().split())

    # Lecture des arêtes (n-1 au total pour un arbre)
    edge_list = []
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edge_list.append((a, b))

    # Construction de la représentation de l'arbre
    tree = build_tree(n, edge_list)

    # Initialisation du tableau de comptage pour chaque sommet (1-indicé)
    cnt = [0 for _ in range(n + 1)]

    # Lecture et application des requêtes de mise à jour
    for _ in range(q):
        p, x = map(int, input().split())
        cnt[p] += x

    # Propagation des valeurs depuis la racine vers tous les sommets de l'arbre
    cnt = propagate_counts(n, tree, cnt)

    # Affichage de la valeur finale pour chaque sommet (en ignorant l'indice 0)
    print(*cnt[1:])

if __name__ == "__main__":
    main()