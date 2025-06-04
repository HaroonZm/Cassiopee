def is_unique_even_positions():
    """
    Demande une chaîne à l'utilisateur, extrait les caractères à des indices pairs,
    puis vérifie si ces caractères sont tous identiques.
    
    Affiche 'Yes' si tous les caractères extraits sont identiques, sinon 'No'.
    """
    # Lecture de l'entrée utilisateur en tant que chaîne de caractères
    s = input()
    
    # On prend les caractères aux indices pairs (0, 2, 4, ...) grâce au slicing
    even_chars = s[::2]
    
    # On crée un ensemble à partir de ces caractères pour identifier les caractères uniques
    unique_chars = set(even_chars)
    
    # Si l'ensemble contient exactement un caractère, alors ils sont tous identiques
    # Afficher 'Yes' si c'est le cas, sinon 'No'
    print(("Yes", "No")[len(unique_chars) - 1])

# Appel de la fonction principale
is_unique_even_positions()