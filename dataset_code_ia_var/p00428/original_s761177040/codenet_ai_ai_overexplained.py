# Commencer une boucle infinie qui ne s’arrêtera qu’avec un break
while True:
    # Lire une ligne de l'entrée utilisateur, la diviser en éléments séparés par un espace,
    # puis convertir chacun de ces éléments en entier à l'aide de map et int
    # raw_input() lit une ligne sous forme de chaîne (string)
    n, m = map(int, raw_input().split())
    
    # Vérifier si la paire d'entiers (n, m) est égale à (0, 0)
    # Si oui, cela signifie qu’on doit arrêter la boucle
    if (n, m) == (0, 0):
        break  # Quitter immédiatement la boucle while
    
    # Créer une liste appelée r contenant m éléments, initialisés à zéro,
    # pour stocker temporairement les résultats
    r = [0] * m  # [0, 0, ..., 0] m fois
    
    # Démarrer une boucle qui va s’exécuter n fois, pour traiter n lignes d’entrées
    for i in range(n):
        # Lire la prochaine ligne d’entrée, diviser par espace, convertir chaque élément en int
        q = map(int, raw_input().split())
        # Boucler sur chacun des m éléments de la ligne q
        for j in range(m):
            # Soustraire q[j] de r[j] et réaffecter la nouvelle valeur à r[j]
            # L’opérateur -= effectue la soustraction puis la réaffectation
            r[j] -= q[j]
    
    # Créer une nouvelle liste de tuples (r[i], i+1) pour chaque colonne (index i)
    # i+1 est utilisé car l’énoncé semble vouloir une numérotation des colonnes à partir de 1
    temp = [(r[i], i + 1) for i in range(m)]
    
    # Trier la liste temp par ordre croissant du premier élément du tuple (la valeur r[i])
    r = sorted(temp)
    
    # On extrait la deuxième valeur de chaque tuple trié (qui correspond au numéro de colonne)
    # Cela produit une liste ordonnée des numéros des colonnes, selon la valeur triée de r
    resultats = [rr[1] for rr in r]
    
    # Convertir chaque entier de cette liste en chaîne de caractères
    # Utiliser ' '.join pour afficher tous les numéros séparés par des espaces sur une même ligne
    print ' '.join(map(str, resultats))