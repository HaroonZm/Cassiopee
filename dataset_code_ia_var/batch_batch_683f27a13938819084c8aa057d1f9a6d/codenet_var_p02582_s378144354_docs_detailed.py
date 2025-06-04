def max_consecutive_R(s):
    """
    Calcule le nombre maximal de 'R' consécutifs dans une chaîne de 3 caractères.

    Args:
        s (str): Une chaîne de caractères de longueur 3 composée de caractères quelconques.

    Returns:
        int: Le maximum d'occurrences consécutives du caractère 'R'.
    """
    ans = 0  # Stocke le maximum trouvé jusqu'à présent
    tmp = 0  # Compte la séquence courante de 'R' consécutifs
    
    # Parcourt chaque caractère des trois premiers (et seuls) caractères de la chaîne
    for i in range(3):
        if s[i] == "R":
            # Incrémente le compteur de R consécutifs si le caractère est 'R'
            tmp += 1
        else:
            # Si ce n'est pas un 'R', met à jour le maximum et réinitialise tmp
            ans = max(ans, tmp)
            tmp = 0
    else:
        # À la fin de la boucle, il faut vérifier si la dernière séquence de 'R'
        # était potentiellement la plus longue (si la chaîne se terminait par 'R')
        ans = max(ans, tmp)
    
    return ans

# Lecture de l'entrée utilisateur
s = input()

# Appel de la fonction et affichage du résultat
print(max_consecutive_R(s))