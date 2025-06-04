inf = 0x10101010  # Une grande constante utilisée pour initialiser les coûts infiniment élevés

def solve(A, strt):
    """
    Calcule les distances minimales à partir d'un sommet de départ donné dans un graphe pondéré.
    
    Cette fonction utilise un algorithme similaire à Dijkstra pour trouver les coûts minimaux 
    depuis le sommet 'strt' vers tous les autres sommets dans la matrice de poids A.
    
    Arguments:
    A -- matrice carrée (liste de listes) des poids entre noeuds, où A[i][j] représente le poids 
         entre les noeuds i et j (0 si pas de lien).
    strt -- indice du sommet de départ (entier)
    
    Retourne:
    cost -- liste des coûts minimaux (entiers) du sommet de départ vers chaque autre sommet.
    """
    cost = [inf] * m              # Initialise la liste des coûts avec une valeur infinie
    visited = [False] * m         # Liste pour indiquer si un sommet a déjà été visité ou non
    cost[strt] = 0                # Le coût du sommet de départ vers lui-même est 0

    while True:
        min_cost = inf            # Pour trouver le sommet non visité avec le coût minimal
        next_node = -1            # Index du prochain sommet à visiter
        visited[strt] = True      # Marquer le sommet actuel comme visité
        
        # Met à jour les coûts des sommets adjacents en fonction du sommet actuel
        for i in range(m):
            if visited[i]:
                continue          # Ignore les sommets déjà visités
            
            if A[strt][i]:        # S'il y a une arête entre strt et i
                d = cost[strt] + A[strt][i]  # Calcul du coût total supposé pour atteindre i via strt
                if d < cost[i]:
                    cost[i] = d   # Mise à jour du coût minimal pour atteindre le sommet i
            
            # Trouver le sommet non visité avec le coût minimal pour la prochaine itération
            if cost[i] < min_cost:
                min_cost = cost[i]
                next_node = i
        
        # Le prochain sommet à visiter est celui avec le plus petit coût non visité
        strt = next_node
        if next_node == -1:
            break                # Si aucun prochain sommet n'a été trouvé, fin de la boucle

    return cost

# Boucle principale de lecture des données et résolution du problème
while True:
    n, m = map(int, raw_input().split())  # Lire le nombre d'arêtes n et le nombre de sommets m
    if n == 0:
        break                             # Si n=0, fin des données
    
    # Initialiser les matrices des temps (T) et des coûts (C) à zéro
    T = [[0] * m for _ in range(m)]
    C = [[0] * m for _ in range(m)]
    
    # Remplir les matrices T et C avec les valeurs fournies
    for _ in range(n):
        a, b, c, t = map(int, raw_input().split())
        # Indices ajustés (base 0) pour les listes Python
        T[a-1][b-1] = T[b-1][a-1] = t  # Temps de trajet entre a et b (non orienté)
        C[a-1][b-1] = C[b-1][a-1] = c  # Coût associé à cet itinéraire entre a et b
    
    # Calculer les distances minimales pour tous les sommets en utilisant le temps
    TS = [solve(T, i) for i in range(m)]
    # Calculer les distances minimales pour tous les sommets en utilisant le coût
    CS = [solve(C, i) for i in range(m)]
    
    # Traiter les requêtes de l'utilisateur
    for _ in range(input()):
        a, b, q = map(int, raw_input().split())
        if q == 0:
            # Affiche le coût minimal pour aller de a à b
            print CS[a-1][b-1]
        else:
            # Affiche le temps minimal pour aller de a à b
            print TS[a-1][b-1]