def multiply_weight_by_32():
    """
    Demande à l'utilisateur de saisir un entier représentant un poids, 
    puis calcule et affiche le produit de ce poids par 32.

    Entrée :
        Aucun paramètre, la saisie se fait via input().
    Sortie :
        Affiche le résultat de la multiplication sur la sortie standard.
    """
    # Demander à l'utilisateur d'entrer une valeur entière
    # Cette valeur représente un poids (W)
    W = int(input("Veuillez entrer une valeur entière pour W : "))

    # Multiplier la valeur de W par 32
    result = W * 32

    # Afficher le résultat à l'utilisateur
    print(result)

# Appeler la fonction principale pour exécuter le programme
multiply_weight_by_32()