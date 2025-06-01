# Démarrage d'une boucle infinie pour exécuter continuellement un bloc de code
while True:
    # Lecture d'une entrée utilisateur, conversion de la chaîne reçue en entier, et stockage dans la variable 'n'
    n = int(input())
    # Lecture d'une deuxième entrée utilisateur, conversion en entier, et stockage dans 'm'
    m = int(input())
    
    # Condition pour vérifier si 'm' est égal à zéro
    # Si c'est le cas, on interrompt la boucle infinie avec 'break' (fin du programme)
    if m == 0:
        break
    
    # Création d'une liste appelée 'dataset' contenant 'm' éléments
    # Chaque élément est une liste de chaînes obtenues en divisant la saisie utilisateur au niveau des espaces
    # [input().split() for _ in range(m)] utilise une compréhension de liste pour répéter 'm' fois cette opération
    dataset = [input().split() for _ in range(m)]
    
    # Création d'un dictionnaire 'list_' où les clés sont des entiers de 1 à 'n' (inclus)
    # Chaque clé est associée à une liste vide, utilisée pour stocker des connexions ou voisins
    # {i+1: [] for i in range(n)} utilise une compréhension de dictionnaire pour générer ces paires
    list_ = {i+1: [] for i in range(n)}
    
    # Iteration sur chaque élément de 'dataset'; 'data' est une liste de deux chaînes représentant des indices
    for data in dataset:
        # Conversion des deux éléments de 'data' en entiers avec 'map' et dépaquetage dans idx_x et idx_y
        idx_x, idx_y = map(int, data)
        
        # Ajout de idx_y à la liste des voisins de idx_x dans le dictionnaire 'list_'
        list_[idx_x].append(idx_y)
        # Ajout de idx_x à la liste des voisins de idx_y également, provoquant une connexion bidirectionnelle
        list_[idx_y].append(idx_x)

    # Initialisation d'une liste 'ans' avec une copie des voisins directs du premier élément (clé 1) dans 'list_'
    ans = list_[1].copy()
    
    # Pour chaque voisin de la clé 1 dans 'list_', on ajoute à 'ans' ses propres voisins
    for i in list_[1]:
        ans += list_[i]
    
    # Conversion de 'ans' en set pour garder uniquement les éléments uniques et suppression d'un élément avec '-1'
    # Le '-1' enlève la clé 1 elle-même si elle apparaissait, car on cherche les connexions indirectes et directes sauf soi-même
    # On affiche finalement la taille (nombre d'éléments uniques) de ce set
    print(len(set(ans))-1)