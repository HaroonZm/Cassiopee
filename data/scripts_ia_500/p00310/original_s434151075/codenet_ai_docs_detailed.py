def somme_notes():
    """
    Lit trois entiers représentant des notes, calcule leur somme et affiche le résultat.
    
    L'utilisateur doit entrer trois entiers séparés par des espaces.
    La fonction calcule la somme de ces trois notes et affiche le total.
    """
    # Lecture des trois entiers saisis par l'utilisateur, séparés par des espaces,
    # et affectation aux variables p, m, et c.
    p, m, c = map(int, input("Entrez trois notes séparées par des espaces : ").split())
    
    # Calcul de la somme des trois notes.
    d = p + m + c
    
    # Affichage de la somme totale.
    print(d)

# Appel de la fonction
somme_notes()