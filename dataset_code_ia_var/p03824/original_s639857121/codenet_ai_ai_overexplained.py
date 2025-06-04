import sys  # Importe le module sys pour accéder à sys.stdin (entrée standard)
range = xrange  # Redéfinit 'range' pour utiliser 'xrange' (utilisé en Python 2 pour efficacité mémoire)

def decomp(coupl, root=0):
    # Cette fonction calcule un étiquetage spécial des noeuds du graphe en arbre.
    # coupl : une liste d'adjacence du graphe (les voisins de chaque noeud)
    # root  : noeud racine pour le parcours (par défaut le premier noeud, indexé 0)
    n = len(coupl)  # On calcule le nombre total de noeuds dans l'arbre
    visible_labels = [0] * n  # Liste contenant un label binaire pour chaque noeud. Initialisée à zéro.

    bfs = [root]  # Liste pour effectuer un parcours en largeur partant de la racine.
    
    # On effectue un parcours en largeur (BFS).
    for node in bfs:  # Pour chaque noeud déjà découvert ...
        for nei in coupl[node]:  # Pour chaque voisin (adjacent) de ce noeud
            coupl[nei].remove(node)  # On retire le parent du voisin pour éviter les doublons/allers-retours
        bfs += coupl[node]  # On ajoute les voisins du noeud courant à la liste de parcours

    # On traite les noeuds dans l'ordre inverse du BFS pour traiter d'abord les feuilles puis remonter
    for node in reversed(bfs):  
        seen = 0  # Variable accumulant les labels visibles par ce noeud (binaire)
        seen_twice = 0  # Variable accumulant les labels vus plus d'une fois

        for nei in coupl[node]:  # Pour chaque voisin du noeud courant
            seen_twice |= seen & visible_labels[nei]  # Marque les labels déjà vus (collision)
            seen |= visible_labels[nei]  # Ajoute le label du voisin à la variable seen (union binaire)

        # Calcule un nouvel identifiant binaire pour ce noeud (choisit le plus petit label inutilisé).    
        tmp = ~seen & -(1 << seen_twice.bit_length())  # Bitmask binaire pour identifier les bits libres
        label = tmp & -tmp  # Garde le bit de plus faible poids non utilisé

        visible_labels[node] = (label | seen) & -label  # Assigne un label unique parmi ceux non encore utilisés
    
    # Retourne la "taille" du label (sous forme d'indice, via bit_length-1) pour chaque noeud 
    return [(seen & -seen).bit_length() - 1 for seen in visible_labels]

# Lecture de l'entrée standard (sys.stdin), le tout est lu comme une unique chaîne puis séparé en entiers
inp = [int(x) for x in sys.stdin.read().split()]
ii = 0  # Initialise un pointeur d'indice pour la lecture séquentielle

n = inp[ii]  # Récupère le nombre de noeuds dans l'arbre
ii += 1  # Incrémente l'indice de lecture

coupl = [[] for _ in range(n)]  # Crée une liste d'adjacence vide pour chaque noeud

# On lit les n-1 arêtes décrivant les connexions entre les noeuds (car l'arbre avec n noeuds a n-1 arêtes)
for _ in range(n - 1):
    u = inp[ii] - 1  # Lecture du premier sommet de l'arête (converti en indice commençant à 0)
    ii += 1  # Avance l'indice de lecture
    v = inp[ii] - 1  # Lecture du deuxième sommet de l'arête (converti en indice commençant à 0)
    ii += 1  # Avance l'indice encore

    coupl[u].append(v)  # Ajoute la connexion v à la liste d'adjacence de u
    coupl[v].append(u)  # Ajoute la connexion u à la liste d'adjacence de v (car non orienté)

# Appel de la fonction decomp, et affiche le maximum calculé parmi tous les labels visibles des noeuds
print max(decomp(coupl))  # 'max' récupère la valeur la plus grande de la liste retournée