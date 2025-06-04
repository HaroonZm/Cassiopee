def distance_between_A_and_Z(s):
    """
    Calcule la distance (en nombre de caractères, extrémités incluses) entre la première occurrence de 'A'
    et la dernière occurrence de 'Z' dans une chaîne donnée.

    Args:
        s (str): La chaîne de caractères à analyser.

    Returns:
        int: La distance entre 'A' et 'Z', c'est-à-dire la position de la dernière 'Z'
             moins la position de la première 'A', plus un (pour inclure les deux caractères).
    """
    # Trouver l'indice de la première occurrence du caractère 'A'
    first_A = s.find('A')
    # Trouver l'indice de la dernière occurrence du caractère 'Z'
    last_Z = s.rfind('Z')
    # Calculer la distance entre ces deux indices, en incluant les deux caractères
    distance = last_Z - first_A + 1
    return distance

# Lire une chaîne de caractères depuis l'entrée utilisateur
input_string = input()
# Appeler la fonction et afficher le résultat
print(distance_between_A_and_Z(input_string))