def calculate_score(input_string):
    """
    Calcule le score en fonction du nombre de caractères 'o' dans la chaîne d'entrée.
    Le score de base est 700, auquel s'ajoutent 100 points pour chaque 'o' présent.

    Args:
        input_string (str): La chaîne de caractères à analyser.

    Returns:
        int: Le score calculé.
    """
    # Compter le nombre d'occurrences du caractère 'o' dans la chaîne d'entrée
    count_o = input_string.count('o')
    # Calculer le score total : score de base (700) + 100 pour chaque 'o'
    score = 700 + 100 * count_o
    # Retourner le score calculé
    return score

if __name__ == "__main__":
    # Lecture de la chaîne d'entrée de l'utilisateur
    user_input = input()
    # Calcul et affichage du score correspondant
    print(calculate_score(user_input))