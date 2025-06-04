def calculate_and_print_weight():
    """
    Demande à l'utilisateur d'entrer une valeur entière représentant un poids (W),
    puis calcule et affiche le résultat de W multiplié par 32.

    Aucune valeur n'est retournée. Le résultat est affiché dans la sortie standard.
    """
    # Demander à l'utilisateur de saisir une valeur entière et la convertir en int
    W = int(input("Veuillez entrer un poids (entier) : "))
    
    # Calculer le résultat en multipliant W par 32
    result = W * 32
    
    # Afficher le résultat dans la console
    print(result)

# Exécution de la fonction principale
calculate_and_print_weight()