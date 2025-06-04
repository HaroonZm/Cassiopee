def is_palindrome(n):
    """
    Vérifie si un nombre entier est un palindrome.

    Un palindrome est un nombre qui se lit de la même façon de gauche à droite et de droite à gauche.

    Args:
        n (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est un palindrome, False sinon.
    """
    s = str(n)  # Conversion du nombre en chaîne de caractères pour faciliter la comparaison
    return s == s[::-1]  # Compare la chaîne avec son inversion


def find_nearest_palindrome(n):
    """
    Trouve le palindrome le plus proche d'un nombre donné.
    
    Si deux palindromes sont à la même distance, le plus petit est préféré.

    Args:
        n (int): Le nombre de départ.

    Returns:
        int: Le palindrome le plus proche de n.
    """
    p = n  # Copie de n pour chercher le palindrome supérieur ou égal à n
    q = n  # Copie de n pour chercher le palindrome inférieur ou égal à n

    # Cherche le plus proche palindrome supérieur ou égal à n
    while not is_palindrome(p):
        p += 1

    # Cherche le plus proche palindrome inférieur ou égal à n
    while not is_palindrome(q):
        q -= 1

    # Si l'écart est le même, retourner le plus petit (q), sinon le plus proche
    if abs(n - q) <= abs(p - n):
        return q
    else:
        return p


if __name__ == "__main__":
    # Demande un nombre à l'utilisateur et affiche le palindrome le plus proche
    n = int(input("Entrez un nombre entier : "))
    result = find_nearest_palindrome(n)
    print(result)