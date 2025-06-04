def calculate_cube():
    """
    Lit un entier depuis l'entrée standard et affiche son cube.
    
    Fonctionnement :
    1. Demande à l'utilisateur d'entrer un nombre entier.
    2. Calcule le cube (puissance 3) de ce nombre.
    3. Affiche le résultat.
    """
    # Demander un entier à l'utilisateur via l'entrée standard et convertir la saisie en int
    N = int(input())
    
    # Calculer le cube de l'entier renseigné
    result = N ** 3
    
    # Afficher le résultat obtenu
    print(result)

# Appel de la fonction principale pour exécuter la logique du programme
calculate_cube()