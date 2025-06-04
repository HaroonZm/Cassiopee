# Début d'une boucle infinie qui continuera jusqu'à ce qu'on rencontre une condition d'arrêt explicite (break)
while True :
    # Ici, on lit une ligne depuis l'entrée utilisateur avec 'input()', puis on la découpe en plusieurs éléments grâce à la méthode 'split()'.
    # Chaque élément est alors converti en entier via 'map(int, ...)'.
    # Enfin, l'ensemble est converti en une liste de deux éléments, correspondant à 'n' et 'm', puis déballé (unpacking) dans les deux variables.
    n, m = map(int, input().split())
    
    # Condition d'arrêt : si les deux entiers n et m valent tous les deux zéro (0),
    # alors la boucle s'interrompt grâce à l'instruction 'break'.
    if n == 0  and m == 0 :
        break

    # Initialisation d'une liste vide appelée 'car_list' qui va contenir les éléments à traiter.
    car_list = []
    
    # Si la première valeur d'entrée (n) n'est pas égale à zéro,
    # alors on va lire encore une ligne pour obtenir les 'n' entiers, les transformer en list et les stocker dans A.
    if n != 0 :
        # Lecture d'une ligne d'entrée, transformation en liste d'entiers
        A = list(map(int, input().split()))
        # On parcourt chacun des 'n' indices (de 0 à n-1) avec une boucle for classique.
        for i in range(n) :
            # On ajoute l'élément A[i] à la fin de la liste 'car_list' à l'aide de 'append'.
            car_list.append(A[i])
    
    # On répète le même processus si la seconde valeur d'entrée (m) n'est pas égale à zéro.
    if m != 0 :
        # Idem : on lit m entiers et on les convertit en liste appelée A.
        A = list(map(int, input().split()))
        # Boucle sur m indices et ajout de chaque élément A[i] à la liste finale.
        for i in range(m) :
            car_list.append(A[i])
    
    # À ce stade, 'car_list' contient tous les éléments saisis à partir des entrées pour n et m.
    # On trie cette liste dans l'ordre croissant à l'aide de la méthode 'sort()',
    # ce qui permet de comparer facilement leurs différences successives.
    car_list.sort()
    
    # On ajoute la valeur entière 0 au début de la liste.
    # 'insert(0, 0)' signifie insérer à l'indice 0 la valeur 0, ce qui décale tous les autres éléments d'un cran vers la droite.
    car_list.insert(0, 0)
    
    # On initialise une variable qui va contenir la plus grande différence trouvée entre deux éléments successifs de 'car_list'.
    max_car = 0
    
    # On parcourt la liste 'car_list' du début jusqu'à l'avant-dernier élément en utilisant une boucle 'for'.
    # La boucle s'exécute (n + m) fois car il y a n+m éléments d'entrée (des deux listes saisies), plus le zéro ajouté au début,
    # donc les index de 0 à n+m-1 pour accéder à car_list[i+1] à chaque itération.
    for i in range(n+m) :
        # Pour chaque élément, on calcule la différence entre l'élément actuel et le suivant,
        # soit car_list[i+1] - car_list[i].
        # Si cette différence est supérieure à la valeur actuelle de 'max_car', on la met à jour avec cette nouvelle différence.
        if car_list[i+1] - car_list[i] > max_car :
            max_car = car_list[i+1] - car_list[i]
    
    # Enfin, on affiche la valeur de 'max_car' trouvée, ce qui correspond à la plus grande distance consécutive entre deux éléments de la liste.
    print(max_car)