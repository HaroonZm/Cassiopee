def compute_final_score(input_string):
    """
    Calcule un score basé sur la présence du caractère 'o' aux trois premières positions de la chaîne.
    
    Le score initial est de 700. Pour chaque 'o' à la position 0, 1 ou 2, on ajoute 100 au score.
    
    Args:
        input_string (str): Chaîne de caractères d'entrée contenant au moins 3 caractères.
        
    Returns:
        int: Le score final après application des règles.
    """
    # Initialisation du score de départ
    score = 700

    # Parcourir les trois premières positions de la chaîne
    for i in range(3):
        # Si le caractère à la position i est 'o', ajouter 100 au score
        if input_string[i] == 'o':
            score += 100
    
    # Retourner le score final
    return score

# Lecture de la chaîne d'entrée de l'utilisateur (mode compatible Python 2)
S = raw_input()

# Calcul du score final en utilisant la fonction définie
final_score = compute_final_score(S)

# Affichage du score final
print final_score