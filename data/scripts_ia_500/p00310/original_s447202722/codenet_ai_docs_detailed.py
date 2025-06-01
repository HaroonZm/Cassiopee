def somme_de_trois_entiers():
    """
    Lit trois entiers depuis l'entrée standard, les additionne et affiche le résultat.

    L'utilisateur doit saisir trois entiers séparés par des espaces.
    La fonction lit ces valeurs, les convertit en entiers, calcule leur somme, puis affiche cette somme.
    """
    # Lecture de trois entiers séparés par des espaces depuis l'entrée standard
    p, m, c = map(int, input("Entrez trois entiers séparés par des espaces : ").split())
    
    # Calcul de la somme des trois entiers
    resultat = p + m + c
    
    # Affichage du résultat de la somme
    print("La somme des trois nombres est :", resultat)

# Appel de la fonction
somme_de_trois_entiers()