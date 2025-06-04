def check_both_odd(a: int, b: int) -> str:
    """
    Vérifie si les deux entiers fournis sont impairs.

    Args:
        a (int): Le premier entier à vérifier.
        b (int): Le deuxième entier à vérifier.

    Returns:
        str: "Yes" si les deux nombres sont impairs, "No" sinon.
    """
    # Utilisation de l'opérateur modulo (%) pour déterminer l'impairité.
    # Un nombre est impair si la division par 2 donne un reste de 1.
    if a % 2 == 1 and b % 2 == 1:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    # Lecture de l'entrée utilisateur avec input(), séparée par des espaces.
    # map(int, ...) sert à convertir chaque élément en entier.
    a, b = map(int, input().split())

    # Appel de la fonction check_both_odd et affichage du résultat.
    print(check_both_odd(a, b))