def afficher_tables_multiplication():
    """
    Affiche les tables de multiplication de 1 à 9 au format 'AxB=C' pour chaque combinaison possible.
    Cette fonction parcourt tous les couples de nombres entiers compris entre 1 et 9 inclus et
    affiche leur produit, sous la forme 'AxB=C'.
    """
    # La boucle parcourt les entiers de 0 à 80 inclus, soit 81 combinaisons (9x9)
    for i in range(81):  # Utilise 'range' au lieu de 'xrange' pour la compatibilité Python 3
        a = i // 9 + 1   # Calcule la première valeur du couple (de 1 à 9)
        b = i % 9 + 1    # Calcule la seconde valeur du couple (de 1 à 9)
        produit = a * b  # Calcule le produit de a et b
        # Affiche le résultat de la multiplication sous la forme 'AxB=C'
        print("{}x{}={}".format(a, b, produit))


# Appel de la fonction pour afficher les tables de multiplication
afficher_tables_multiplication()