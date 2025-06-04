def calculate_r_sequence_score(s):
    """
    Calcule le score basé sur la séquence consécutive de la lettre 'R' dans une chaîne donnée.
    Le score est déterminé comme suit :
        - 1 si 'R' apparaît au moins une fois
        - 2 si 'RR' apparaît (au moins deux 'R' consécutifs)
        - 3 si 'RRR' apparaît (trois 'R' consécutifs ou plus)
    Si aucun 'R' n'est présent, le score est 0.

    Args:
        s (str): La chaîne de caractères à analyser.

    Returns:
        int: Le score basé sur la présence de séquences de 'R'.
    """
    ans = 0  # Initialiser le score à 0

    # Vérifier la présence de séquences spécifiques de 'R' dans l'ordre croissant de longueur

    if "R" in s:
        # Au moins un 'R' trouvé, score minimum 1
        ans = 1
    if "RR" in s:
        # Deux 'R' consécutifs trouvés, score augmenté à 2
        ans = 2
    if "RRR" in s:
        # Trois 'R' consécutifs trouvés, score maximal 3
        ans = 3

    return ans

# Demander à l'utilisateur de saisir une chaîne de caractères
s = input()

# Appeler la fonction pour obtenir le score correspondant
result = calculate_r_sequence_score(s)

# Afficher le score calculé
print(result)