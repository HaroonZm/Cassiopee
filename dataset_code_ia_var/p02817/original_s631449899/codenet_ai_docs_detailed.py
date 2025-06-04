def swap_and_concatenate():
    """
    Demande à l'utilisateur d'entrer deux mots séparés par un espace,
    puis inverse l'ordre des mots et les concatène sans espace supplémentaire.
    Affiche le résultat à l'écran.

    Exemple :
        Entrée : chat chien
        Sortie : chienchat
    """
    # Demander à l'utilisateur d'entrer deux éléments séparés par un espace
    first, second = input().split()
    # Concaténer le second mot avant le premier et afficher le résultat
    print(second + first)

# Appeler la fonction principale pour exécuter le programme
swap_and_concatenate()