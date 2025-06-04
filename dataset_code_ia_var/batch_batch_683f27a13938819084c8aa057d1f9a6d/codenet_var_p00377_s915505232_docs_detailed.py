def calculate_average_rounded_up():
    """
    Lit deux lignes d'entrée :
        - La première ligne contient deux entiers n et c (c n'est pas utilisé ici).
        - La deuxième ligne contient n entiers représentant des valeurs données.
    Calcule la somme de ces valeurs, puis calcule la moyenne de la somme divisée par (n+1),
    arrondie à l'entier supérieur si nécessaire.
    Affiche le résultat final.
    """
    # Lire et extraire les valeurs de la première ligne.
    # n : nombre d'éléments, c : valeur ignorée selon l'énoncé du code.
    n, c = map(int, input().split(" "))

    # Lire la deuxième ligne, contenant n entiers, et calculer leur somme.
    p = sum(list(map(int, input().split(" "))))

    # Incrémenter n de 1, conformément à l'algorithme d'origine.
    n += 1

    # Calculer la partie entière de la division de la somme par le nouveau n.
    result = int(p / n)

    # Si la division est entière, afficher le résultat tel quel.
    # Sinon, ajouter 1 pour arrondir à l'entier supérieur, puis afficher.
    if p % n == 0:
        print(result)
    else:
        print(result + 1)

# Appel de la fonction principale
calculate_average_rounded_up()