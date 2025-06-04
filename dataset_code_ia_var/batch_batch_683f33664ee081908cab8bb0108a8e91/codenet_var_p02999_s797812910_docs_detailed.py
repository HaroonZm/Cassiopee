def compare_values():
    """
    Demande deux entiers en entrée standard, les compare selon un critère défini :
        - Affiche 0 si le premier entier est strictement inférieur au second.
        - Affiche 10 sinon.
    Cette fonction ne prend pas d'argument et ne retourne rien ; elle affiche directement le résultat.
    """
    # Lecture et transformation de l'entrée utilisateur : on attend deux entiers séparés par un espace.
    x, a = map(int, input("Entrez deux entiers séparés par un espace (x a) : ").split())

    # Comparaison : si x est strictement inférieur à a, afficher 0.
    if x < a:
        print(0)
    # Sinon (x >= a), afficher 10.
    else:
        print(10)

# Appeler la fonction principale lorsque le script s'exécute.
compare_values()