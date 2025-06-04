import sys

# Redéfinition de la fonction d'entrée pour lire plus efficacement depuis stdin
input = sys.stdin.readline

# Augmentation de la limite de récursion, bien que le DFS soit ici itératif
sys.setrecursionlimit(10**6)

def read_graph(N):
    """
    Construit le graphe non orienté sous forme de liste d'adjacence à partir des entrées.
    
    Args:
        N (int): Nombre de noeuds dans le graphe.

    Returns:
        list: Liste d'adjacence représentant le graphe (indices de 1 à N inclus).
    """
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph

def find_special_node(graph, N):
    """
    Recherche un noeud du graphe ayant un degré strictement supérieur à 2.

    Args:
        graph (list): Liste d'adjacence du graphe.
        N (int): Nombre total de noeuds.

    Returns:
        int: L'indice du noeud spécial, ou -1 si aucun noeud ne correspond.
    """
    for n in range(1, N + 1):
        if len(graph[n]) > 2:
            return n
    return -1

def dfs2(s, graph, N):
    """
    Effectue un parcours DFS itératif à partir du noeud s pour résoudre le problème spécifique.
    Cette fonction utilise un style imitant la récursion avec gestion manuelle de la pile,
    et met à jour plusieurs tableaux auxiliaires afin de répondre à la question posée par l'énoncé.
    
    Args:
        s (int): Noeud source pour le parcours DFS.
        graph (list): Liste d'adjacence représentant le graphe.
        N (int): Nombre de noeuds.

    Returns:
        int: Résultat calculé suite au parcours DFS (ici probablement le nombre de "triplets" internes).
    """
    ans = 0             # Compteur pour stocker le résultat cherché
    S = [0] * (N + 1)   # Tableau pour stocker des informations intermédiaires pour chaque noeud
    T = [0] * (N + 1)   # Tableau pour compter les enfants visités pour chaque noeud
    Ind = [0] * (N + 1) # Indices de parcours pour chaque noeud (prochain voisin à explorer)
    stack = [s]         # Pile simulant la récursion DFS

    while stack:
        p = stack[-1]   # Noeud courant (au sommet de la pile)

        # Si tous les voisins du noeud courant ont été explorés
        if Ind[p] == len(graph[p]):
            # Met à jour l'accumulateur de résultat avec une formule dépendant de S et T
            ans += max(T[p] - S[p] - 1, 0)
            stack.pop() # Retire le noeud courant de la pile (retour arrière dans le DFS)
            if stack:
                par = stack[-1]   # Récupère le parent dans l'arbre DFS
                T[par] += 1       # Incrémente le nombre d'enfants terminés du parent
                # Met à jour S du parent en fonction des résultats des enfants
                if S[p] > 0 or T[p] > 1:
                    S[par] += 1
        # Si le prochain voisin à explorer est le parent, on le saute
        elif len(stack) > 1 and stack[-2] == graph[p][Ind[p]]:
            Ind[p] += 1
        # Sinon, avance vers le prochain voisin
        else:
            stack.append(graph[p][Ind[p]])
            Ind[p] += 1
    return ans

def main():
    """
    Point d'entrée principal du programme. Lit l'entrée, construit le graphe,
    recherche un noeud "spécial", effectue le traitement, puis affiche le résultat.
    """
    N = int(input())
    graph = read_graph(N)
    s = find_special_node(graph, N)
    # Si aucun noeud n'a un degré strictement supérieur à 2 (c'est une chaîne)
    if s == -1:
        ans = 1
    else:
        ans = dfs2(s, graph, N)
    print(ans)

if __name__ == '__main__':
    main()