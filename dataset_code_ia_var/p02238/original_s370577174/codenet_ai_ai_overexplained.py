# Demander à l'utilisateur d'entrer un entier qui représente le nombre de sommets (nœuds) dans le graphe
n = int(input())

# Créer une liste vide appelée 'adj' pour stocker la liste d'adjacence de chaque sommet
adj = []

# Boucle pour lire les informations d'adjacence pour chaque sommet
for i in range(n):
    # Lire une ligne d'entrée, diviser les valeurs séparées par un espace, les convertir en entiers
    # et les ajouter comme une sous-liste à 'adj'
    adj.append(list(map(int, input().split())))

# Créer une matrice n x n remplie de zéros ; cette matrice représentera la présence (1) ou l'absence (0) d'arêtes
edge = [[0 for i2 in range(n)] for i1 in range(n)]

# --- Construction de la matrice d'adjacence à partir de la liste d'adjacence ---
for i in range(n):  # Parcourir chaque sommet
    # Pour chaque voisin de ce sommet (le nombre de voisins est spécifié à l'index 1 de la sous-liste)
    for j in range(adj[i][1]):
        # Dans la matrice d'adjacence, indiquer qu'il existe une arête du sommet 'i' vers le sommet indexé par 'adj[i][j+2]-1'
        # On soustrait 1 car les indices débutent à 0 en Python, alors que dans les entrées ils commencent à 1
        edge[i][adj[i][j + 2] - 1] = 1

# Initialiser une variable qui servira de compteur temporel pour l'ordre de découverte/fin
time = 1

# Créer une liste 'discover' pour enregistrer le temps de découverte de chaque sommet, avec une valeur initiale de 0
discover = [0 for i in range(n)]

# Créer une liste 'final' pour enregistrer le "temps de fin" de chaque sommet, également initialisée à 0
final = [0 for i in range(n)]

# Initialiser une liste vide appelée 'stack' ; elle servira de pile pour gérer les retours en arrière lors du parcours DFS
stack = []

# Définir une fonction de parcours en profondeur (DFS)
def dfs(id, time):
    # Pour chaque sommet possible (parcours ligne correspondant dans la matrice d'adjacence)
    for i in range(n):
        # Initialiser un compteur 'c' à 0 pour vérifier si le sommet a des voisins qui doivent être visités
        c = 0
        # Vérifier s'il existe une arête allant du sommet courant (id) à un autre sommet (i)
        # ET que ce sommet (i) n'a pas encore été découvert (discover[i] == 0)
        if edge[id][i] == 1 and discover[i] == 0:
            # Ajouter le sommet courant dans la pile avant de faire l'appel récursif
            stack.append(id)
            # Enregistrer le temps de découverte du sommet (i) avec la valeur actuelle de 'time'
            discover[i] = time
            # Incrémenter le compteur pour indiquer qu'on a trouvé un voisin à visiter
            c += 1
            # Appeler récursivement dfs sur le voisin trouvé, avec le temps incrémenté de 1
            dfs(i, time + 1)
        else:
            # Si pas d'arête vers ce voisin, ou déjà découvert, ne rien faire
            pass
    # Si le compteur 'c' est toujours 0 (pas de voisins non découverts), c'est la phase de "remontée/backtracking"
    if c == 0:
        # Vérifier si la pile n'est pas vide, c'est-à-dire qu'il y a des sommets où revenir
        if len(stack) > 0:
            # Assurer que le 'temps de fin' pour ce sommet n'a pas encore été marqué
            if final[id] == 0:
                # Enregistrer le temps de fin avec la valeur courante de 'time'
                final[id] = time
                # Retirer le sommet précédent de la pile pour revenir en arrière et continuer le DFS
                dfs(stack.pop(), time + 1)
            else:
                # Si le temps de fin de ce sommet a déjà été enregistré, simplement passer au sommet précédent sur la pile
                dfs(stack.pop(), time)

# Marquer le temps de découverte pour le sommet initial (ici sommet 0), en utilisant la première valeur possible
discover[0] = time
# Ajouter ce sommet dans la pile pour pouvoir revenir en arrière si besoin
stack.append(0)
# Lancer la recherche en profondeur à partir du sommet 0, avec un temps augmenté de 1
dfs(0, time + 1)

# Après le premier parcours, vérifier s'il reste des sommets non découverts (non reliés/ composante connexe différente)
for i in range(n):
    # Si le sommet i n'a pas encore été découvert (temps de découverte toujours à 0)
    if discover[i] == 0:
        # Affecter à sa découverte le temps de fin du premier sommet +1 (pour éviter les collisions de temps)
        discover[i] = final[0] + 1
        # Ajouter ce sommet à la pile
        stack.append(i)
        # Relancer DFS à partir de ce sommet, avec le temps mis à jour
        dfs(i, final[0] + 2)
        # On ne nettoie qu'un seul sommet non visité à la fois ici (hypothèse : au plus deux composantes non connexes)
        break

# Afficher les résultats : pour chaque sommet, imprimer son indice (en partant de 1),
# son temps de découverte et son temps de fin
for i in range(n):
    print(i + 1, discover[i], final[i])