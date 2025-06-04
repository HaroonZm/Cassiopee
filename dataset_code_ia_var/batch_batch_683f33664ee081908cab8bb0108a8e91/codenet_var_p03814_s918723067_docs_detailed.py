def distance_between_A_and_Z(s):
    """
    Calcule la distance (incluant les lettres de début et de fin) entre la première occurrence de 'A'
    et la dernière occurrence de 'Z' dans une chaîne de caractères.

    Paramètres:
        s (str): La chaîne dans laquelle chercher les lettres.

    Retourne:
        int: La distance entre l'index de la première 'A' et celui de la dernière 'Z', plus un.
             Si 'A' ou 'Z' n'est pas présent, retourne une valeur basée sur la différence obtenue.
    """
    # Recherche de l'index de la première occurrence de 'A'
    first_A = s.find('A')
    # Recherche de l'index de la dernière occurrence de 'Z'
    last_Z = s.rfind('Z')
    # Calcul et retour de la distance (inclus les deux bornes)
    return last_Z - first_A + 1

# Lecture de la chaîne d'entrée de l'utilisateur
input_string = input()
# Appel de la fonction et affichage du résultat
print(distance_between_A_and_Z(input_string))