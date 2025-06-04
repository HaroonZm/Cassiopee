def to_uppercase():
    """
    Demande à l'utilisateur une chaîne de caractères via l'entrée standard,
    convertit la chaîne saisie en lettres majuscules et affiche le résultat.
    """
    # Demander à l'utilisateur d'entrer une chaîne de caractères
    s = input()
    # Convertir la chaîne de caractères saisie en majuscules
    upper_s = s.upper()
    # Afficher la chaîne convertie
    print(upper_s)

# Appeler la fonction principale
to_uppercase()