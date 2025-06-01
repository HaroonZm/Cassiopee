def calculer_somme_maximale():
    """
    Cette fonction lit six entiers depuis l'entrée standard,
    calcule la somme des quatre plus grands entiers parmi les quatre premiers,
    puis ajoute le plus grand des deux derniers entiers,
    et enfin affiche le résultat.

    Processus détaillé :
    - Lit six entiers a, b, c, d, e, f.
    - Calcule la somme des quatre premiers entiers (a, b, c, d) en excluant le minimum parmi eux.
    - Trouve le maximum entre les deux derniers entiers (e, f).
    - Additionne ces deux résultats pour obtenir la somme finale.
    - Affiche la somme finale.
    """

    # Lecture des quatre premiers entiers depuis l'entrée standard
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    # Lecture des deux derniers entiers depuis l'entrée standard
    e = int(input())
    f = int(input())

    # Calcul de la somme des quatre plus grands entiers parmi a, b, c, d
    # On fait la somme des quatre entiers et on soustrait le minimum pour exclure le plus petit
    somme_quatre_plus_grands = a + b + c + d - min(a, b, c, d)

    # Détermination du plus grand entier parmi e et f
    max_deux_dernier = max(e, f)

    # Calcul final : somme des quatre plus grands entiers plus le maximum des deux derniers
    somme_finale = somme_quatre_plus_grands + max_deux_dernier

    # Affichage du résultat
    print(somme_finale)

# Appel de la fonction pour exécuter le calcul
calculer_somme_maximale()