def concat_strings():
    """
    Lit deux chaînes de caractères séparées par un espace depuis l'entrée standard,
    puis les concatène dans l'ordre inverse (T suivi de S) et affiche le résultat.
    """
    # Lecture de l'entrée utilisateur : attend deux mots séparés par un espace
    S, T = input().split()
    # Concaténation des deux chaînes dans l'ordre T suivi de S
    result = T + S
    # Affichage du résultat à l'écran
    print(result)

# Appel de la fonction principale pour exécuter la logique
concat_strings()