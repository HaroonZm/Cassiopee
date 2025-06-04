# Définition de la fonction dfs (Depth-First Search) utilisée pour trouver des chemins augmentants dans le graphe
def dfs(v, t, f, used, graph):
    # Si le sommet courant v est le même que le sommet cible t, cela signifie qu'on a atteint le puits,
    # donc on retourne la capacité f (le flot possible sur ce chemin)
    if v == t:
        return f
    # Marque le sommet courant v comme ayant été visité dans la recherche actuelle
    used[v] = True
    # On parcourt tous les sommets accessibles directement depuis v (i.e., tous les voisins de v dans le graphe)
    for to in graph[v]:
        # c représente la capacité (i.e., le flot restant) de l'arête de v vers to
        c = graph[v][to]
        # Si le sommet to a déjà été visité, ou si la capacité de l'arête est nulle, on ignore ce chemin
        if used[to] or c == 0:
            continue  # Passe au prochain voisin
        # On tente une exploration récursive à partir de to, avec la capacité minimale possible sur le chemin
        # (c'est-à-dire le minimum entre le flot disponible jusque-là f et la capacité c de l'arête actuelle)
        d = dfs(to, t, min(f, c), used, graph)
        # Si un flot positif a effectivement pu passer par ce chemin (c'est-à-dire d > 0)
        if d > 0:
            # On réduit la capacité de l'arête de v vers to du flot d trouvé
            graph[v][to] -= d
            # On augmente la capacité de l'arête opposée (to vers v), ce qui permet un retour éventuel (flot résiduel)
            graph[to][v] += d
            # On retourne la valeur de ce flot (d) au niveau supérieur de l'exploration
            return d
    # Si aucun chemin valable n'a été trouvé depuis ce sommet, retourne 0 pour signaler l'échec de cette voie
    return 0
 
# Fonction pour calculer le flot maximal à partir de la source s vers le puits t dans le graphe
def max_flow(s, t, graph):
    # Initialise la valeur totale du flot trouvé à 0
    flow = 0
    # Boucle infinie: on continue tant qu'on trouve des chemins augmentants dans le graphe résiduel
    while True:
        # Construit une liste pour mémoriser quels sommets ont déjà été visités pendant cette recherche
        used = [False] * len(graph)
        # Lance une DFS en cherchant à envoyer le flot maximal possible (float('inf') représente l'infini)
        f = dfs(s, t, float('inf'), used, graph)
        # On ajoute le flot obtenu par ce chemin (peut être 0 si aucun chemin n'a été trouvé)
        flow += f
        # Si on n'a pas pu envoyer de flot supplémentaire, ou on passe de flot infini, alors l'algorithme s'arrête
        if f == 0 or f == float('inf'):
            return flow  # Retourne la valeur finale du flot total
 
# Lecture du nombre de lignes H (hauteur) et du nombre de colonnes W (largeur) depuis l'entrée standard
H, W = map(int, input().split())

# Lecture de la grille : chaque ligne lue est une chaîne de caractères représentant une ligne de la grille
a = [input() for _ in range(H)]
# Pour travailler plus facilement, conversion de chaque ligne en liste de caractères (donc a devient une liste de listes)
a = [[s for s in a[i]] for i in range(H)]

# Construction du graphe sous la forme d'une liste de dictionnaires :
# chaque sommet du graphe correspond à un index, chaque dictionnaire donne les voisins accessibles depuis ce sommet et la capacité des arêtes
# Il y a H sommets pour les lignes, W sommets pour les colonnes, 1 sommet source (H+W), et 1 sommet puits (H+W+1)
graph = [{} for _ in range(H + W + 2)]

# Parcours de toutes les cases de la grille pour établir la structure du graphe et les capacités des arêtes
for h in range(H):
    for w in range(W):
        # Si la case contient un 'o', cela signifie qu'il y a une connexion entre la ligne h et la colonne w (capacité 1 dans les deux sens)
        if a[h][w] == 'o':
            # Arête de la ligne h vers la colonne w (décalée de H pour la différencier des lignes)
            graph[h][H + w] = 1  # Capacité 1
            # Arête de la colonne w vers la ligne h (retour), aussi capacité 1
            graph[H + w][h] = 1
        # Si on découvre la source ('S'), on connecte la source à la ligne et la colonne correspondantes avec capacité infinie (c'est float('inf'))
        if a[h][w] == 'S':
            # Source est au sommet H+W
            # Connexion de la source aux sommets ligne h et colonne w
            graph[H + W][h] = float('inf')
            graph[H + W][H + w] = float('inf')
            # Les arêtes opposées (retour) sont initialisées à 0
            graph[h][H + W] = 0
            graph[H + w][H + W] = 0
        # Si la case est le puits ('T'), on connecte les lignes et colonnes concernées au puits avec capacité infinie (flot illimité dans ces directions)
        if a[h][w] == 'T':
            # Puits est au sommet H+W+1
            # Connexions opposées du puits vers la ligne et la colonne (capacité nulle, utilisé pour les flots résiduels)
            graph[H + W + 1][h] = 0
            graph[H + W + 1][H + w] = 0
            # Connexions de la ligne et de la colonne vers le puits avec capacité infinie
            graph[h][H + W + 1] = float('inf')
            graph[H + w][H + W + 1] = float('inf')

# Calcul du flot maximal entre la source (sommet H+W) et le puits (sommet H+W+1)
ans = max_flow(H + W, H + W + 1, graph)

# Si la valeur maximale du flot est 'infinie', on retourne -1 (cela signifie probablement que S et T sont sur la même ligne ou même colonne, soit un cas impossible)
if ans == float('inf'):
    ans = -1

# Affiche la réponse finale : le flot maximal trouvé, ou -1 si impossible
print(ans)