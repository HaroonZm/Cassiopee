def max_manhattan_distance():
    """
    Lit des points à partir de l'entrée standard et calcule la plus grande distance de Manhattan entre deux points.
    
    Lecture attendue :
        La première ligne est un entier n, le nombre de points.
        Les lignes suivantes contiennent pour chaque point deux entiers (coordonnées x puis y).
    
    Retour :
        Affiche dans la sortie standard la plus grande distance de Manhattan entre deux points.
    """

    # Lire tous les entiers de l'entrée standard.
    # Le premier entier 'n' est le nombre de points, les autres sont les coordonnées.
    n, *z = map(int, open(0).read().split())

    # Initialiser les listes pour stocker x + y et x - y pour chaque point.
    a, b = [], []

    # Parcourir la liste 'z' deux par deux (x, y pour chaque point).
    # Utilisation de zip(*[iter(z)]*2) pour grouper les éléments par paires.
    for x, y in zip(*[iter(z)]*2):
        # Ajouter la somme (x + y) à la liste 'a'.
        a.append(x + y)
        # Ajouter la différence (x - y) à la liste 'b'.
        b.append(x - y)

    # Calculer la différence maximale pour chaque liste :
    #   - max(a) - min(a) donne la plus grande distance sur la diagonale x+y.
    #   - max(b) - min(b) donne la plus grande distance sur la diagonale x-y.
    # La plus grande distance de Manhattan est le max des deux.
    max_dist = max(abs(max(a) - min(a)), abs(max(b) - min(b)))

    # Afficher la distance maximale trouvée.
    print(max_dist)

# Appel de la fonction principale.
max_manhattan_distance()