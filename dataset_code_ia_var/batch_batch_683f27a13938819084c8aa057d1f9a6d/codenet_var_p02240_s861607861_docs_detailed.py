from collections import deque

def dfs(G, C, id, color):
    """
    Effectue une recherche en profondeur (DFS) sur un graphe pour colorier
    tous les sommets connectés au sommet 'id' avec la couleur spécifiée.

    Args:
        G (list of list of int): Le graphe représenté sous forme de liste d'adjacence.
        C (list of int): Liste des couleurs (-1 si non colorié).
        id (int): Index du sommet de départ pour le DFS.
        color (int): Couleur (étiquette de composante) à attribuer à la composante connectée.

    Side effect:
        Modifie la liste C pour attribuer à chaque sommet de la composante connectée la couleur 'color'.
    """
    stack = deque()         # Utilisation d'une pile pour l'itération DFS
    stack.append(id)
    C[id] = color           # Colorier le sommet de départ

    while stack:
        u = stack.pop()     # Prendre le sommet courant
        # Parcours des voisins du sommet courant
        for i in range(len(G[u])):
            v = G[u][i]
            # Si le voisin n'est pas colorié, on le colorie et on l'ajoute à la pile
            if C[v] == -1:
                C[v] = color
                stack.append(v)

if __name__ == '__main__':
    """
    Point d'entrée du programme. 
    Lit les entrées utilisateurs pour construire un graphe, trouve toutes les composantes connexes via DFS,
    puis répond à des requêtes pour savoir si deux sommets appartiennent à la même composante.
    """
    # Lecture du nombre d'utilisateurs (sommets) et du nombre de liens (arêtes)
    num_of_users, num_of_links = [int(x) for x in input().split(' ')]
    links = []
    # Lecture des paires d'utilisateurs à relier (arêtes du graphe)
    for _ in range(num_of_links):
        links.append(list(map(int, input().split(' '))))
    # Lecture du nombre de requêtes
    num_of_queries = int(input())
    queries = []
    # Lecture des requêtes sous la forme de paires d'utilisateurs
    for _ in range(num_of_queries):
        queries.append(list(map(int, input().split(' '))))

    # Construction de la liste d'adjacence du graphe
    # Suppose que les identifiants d'utilisateurs sont compris entre 0 et 99_999
    G = [[] for _ in range(100000)]     # Liste d'adjacence initialisée pour 100 000 sommets
    C = [-1] * 100000                   # Toutes les couleurs initialisées à -1 (non visité)
    # Ajout des arêtes non orientées au graphe
    for f, t in links:
        G[f].append(t)
        G[t].append(f)

    # Attribution d'une couleur (identifiant de composante connexe) à chaque groupe connecté
    color = 1
    for id in range(num_of_users):
        if C[id] == -1:
            dfs(G, C, id, color)       # Lancer un DFS si le sommet n'est pas encore colorié
            color += 1                 # Changer de couleur pour la prochaine composante

    # Réponses aux requêtes : les sommets sont-ils dans la même composante ?
    for x, y in queries:
        if C[x] == C[y]:
            print('yes')
        else:
            print('no')