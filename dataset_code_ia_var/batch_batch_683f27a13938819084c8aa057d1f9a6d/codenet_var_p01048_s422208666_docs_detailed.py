def choisir_element():
    """
    Affiche un élément d'une liste prédéfinie en fonction d'un indice donné par l'utilisateur.

    L'utilisateur saisit un nombre entier correspondant à la position (à partir de 1) dans la liste :
    [1, 2, 4, 6, 16, 12, 64, 24, 36, 48, 1024, 60]
    Le programme affiche alors la valeur à cette position.

    Entrée :
        - Un nombre entier n fourni par l'utilisateur (1 <= n <= 12).

    Sortie :
        - L'élément n-1 de la liste.
    """
    # Liste prédéfinie des éléments parmi lesquels l'utilisateur peut choisir.
    liste_elements = [1, 2, 4, 6, 16, 12, 64, 24, 36, 48, 1024, 60]
    
    # Demande à l'utilisateur de saisir un nombre correspondant à une position dans la liste.
    indice = int(input("Veuillez saisir un numéro entre 1 et 12 : "))
    
    # Calcule l'indice effectif dans la liste (Python utilise des indices de 0 à n-1),
    # donc on soustrait 1 au nombre entré par l'utilisateur.
    indice_liste = indice - 1
    
    # Affiche l'élément sélectionné de la liste.
    print(liste_elements[indice_liste])

# Appelle la fonction principale pour exécuter le programme.
choisir_element()