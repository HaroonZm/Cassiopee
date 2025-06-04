# Demander à l'utilisateur de saisir un entier, qui sera assigné à la variable N
# Ceci correspond typiquement au nombre de sommets/nœuds dans un graphe/arbre
N = int(input())

# Créer une liste de listes vide, appelée E, de taille (N+1)
# E[i] contiendra la liste des voisins du nœud i, c'est-à-dire sa liste d'adjacence
# On commence à l'indice 0, mais on n'utilisera que les indices 1 à N inclusivement
E = [[] for i in range(N + 1)]

# Créer un dictionnaire vide nommé ans
# Il servira à stocker les valeurs assignées à chaque nœud
ans = {}

# Initialiser la variable First à 0 ; elle désignera le nœud ayant le plus de voisins (le degré maximal)
First = 0

# Initialiser la variable edges à 0 ; elle retiendra le degré (nombre d'arêtes) maximal rencontré
edges = 0

# Créer une liste vide q, qui sera employée comme file (queue) pour le parcours (BFS)
q = []

# Créer une liste visited, initialement de longueur N+1, de valeurs False
# visited[i] indiquera si le nœud i a été visité ou non lors du parcours
visited = [False] * (N + 1)

# Boucle pour lire les N-1 arêtes (parce que dans un arbre à N nœuds, il y a toujours N-1 arêtes)
for i in range(N - 1):
    # Lire une ligne d'entrée, couper la chaîne par les espaces et convertir chaque élément en entier
    # On obtient ainsi les deux nœuds (A et B) reliés par une arête
    A, B = map(int, input().split())
    
    # Ajouter B dans la liste des voisins de A et vice-versa
    # Ceci car le graphe est non-orienté
    E[A].append(B)
    E[B].append(A)
    
    # Si le nombre de voisins de A dépasse la valeur maximale atteinte jusque-là, mettre à jour
    if len(E[A]) > edges:
        First = A      # Le nouveau nœud initial sera A
        edges = len(E[A])  # Mettre à jour le maximum de degré observé
    
    # Faire la même vérification pour B, pour être sûr de détecter le vrai max
    if len(E[B]) > edges:
        First = B
        edges = len(E[B])

# Lire une ligne, séparer les éléments et les convertir en entiers pour former la liste C
# Cette liste C contiendra les valeurs à assigner aux nœuds
C = list(map(int, input().split()))

# Trier la liste C en ordre croissant
# Cela sera utile pour l'affectation ultérieure des valeurs aux nœuds
C.sort()

# Calculer la somme maximale possible en additionnant toutes les valeurs de C sauf la plus grande
# Ceci est obtenu en faisant sum(C) - C[-1]
max = sum(C) - C[-1]

# Ajouter le nœud First à la file q pour débuter le parcours
q.append(First)

# Boucle pour parcourir l'ensemble des nœuds de 1 à N
for i in range(1, N + 1):
    # Retirer et obtenir le premier élément de la file q
    # C'est le nœud à traiter (BFS : on traite le plus ancien inséré)
    x = q.pop(0)
    
    # Marquer x comme visité dans la liste visited
    visited[x] = True
    
    # Assigner au nœud x la i-ème valeur la plus grande de la liste C
    # Comme on la veut en décroissant, on prend C[-i]
    ans[x] = C[-i]
    
    # Pour tous les voisins xx de x dans la liste d'adjacence
    for xx in E[x]:
        # Si ce voisin n'a pas encore été visité
        if not visited[xx]:
            # L'ajouter à la file q pour le traiter plus tard
            q.append(xx)

# Afficher la somme maximale calculée précédemment
print(max)

# Initialiser une chaîne vide s pour la construction du résultat final
s = ""

# Boucle sur chaque nœud de 1 à N pour construire et afficher les assignations
for i in range(1, N + 1):
    # Convertir la valeur assignée du nœud i en chaîne et l'ajouter à s
    s += str(ans[i])
    
    # Si ce n'est pas le dernier nœud, ajouter un espace pour la séparation
    if i != N:
        s += " "

# Afficher la chaîne s qui contient les valeurs attribuées à chaque nœud, séparées par des espaces
print(s)