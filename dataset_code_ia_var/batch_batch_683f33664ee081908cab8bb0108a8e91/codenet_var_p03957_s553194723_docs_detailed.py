def contains_c_followed_by_f(s):
    """
    Vérifie si la chaîne de caractères 's' contient un 'C' suivi d'un 'F' quelque part après.

    Args:
        s (str): La chaîne à analyser.

    Returns:
        bool: True si un 'C' est suivi d'un 'F', False sinon.
    """
    # Vérifie si 'C' est présent dans la chaîne
    if "C" in s:
        # Trouve l'index du premier 'C'
        index_c = s.index("C")
        # Cherche un 'F' dans la sous-chaîne débutant à partir de ce 'C'
        if "F" in s[index_c:]:
            return True
    # Retourne False si 'C' ou un 'F' après 'C' ne sont pas présents
    return False

if __name__ == "__main__":
    # Demande à l'utilisateur de saisir une chaîne de caractères
    s = input()
    # Vérifie si la condition est remplie et affiche "Yes" ou "No" en conséquence
    if contains_c_followed_by_f(s):
        print("Yes")
    else:
        print("No")