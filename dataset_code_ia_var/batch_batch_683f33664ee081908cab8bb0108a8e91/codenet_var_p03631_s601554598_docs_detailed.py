def is_palindrome(N):
    """
    Vérifie si la chaîne fournie en entrée est un palindrome.

    Un palindrome est une séquence qui se lit de la même façon de gauche à droite et de droite à gauche.

    Paramètres :
    -----------
    N : str
        La chaîne de caractères à vérifier.

    Retourne :
    ---------
    bool
        True si la chaîne est un palindrome, False sinon.
    """
    # On compare la chaîne à son inverse générée par slicing [::-1]
    return N == N[::-1]

if __name__ == "__main__":
    # Lecture de l'entrée utilisateur. L'entrée est considérée comme une chaîne de caractères.
    N = input()
    # On imprime "Yes" si la chaîne est un palindrome, sinon "No"
    if is_palindrome(N):
        print("Yes")
    else:
        print("No")