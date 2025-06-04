def display_multiplication_table():
    """
    Affiche la table de multiplication de 1 à 9.
    
    Pour chaque entier i de 1 à 9, et pour chaque entier j de 1 à 9,
    cette fonction affiche une ligne de la forme "ixj=produit".
    Exemple : "2x3=6"
    """
    # Boucle extérieure : parcourt les entiers de 1 à 9 (inclus)
    for i in range(1, 10):
        # Boucle intérieure : parcourt aussi les entiers de 1 à 9 (inclus)
        for j in range(1, 10):
            # Concatène i, 'x', j et le résultat de leur multiplication dans une chaîne
            # et l'affiche à l'écran.
            print(str(i) + "x" + str(j) + "=" + str(i * j))

# Appel de la fonction pour afficher la table de multiplication
display_multiplication_table()