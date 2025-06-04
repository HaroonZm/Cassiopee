def check_string_sequence(a: str, b: str, c: str) -> str:
    """
    Vérifie si la dernière lettre de la chaîne 'a' correspond à la première lettre de 'b',
    et si la dernière lettre de 'b' correspond à la première lettre de 'c'.
    Retourne 'YES' si les deux conditions sont vraies, sinon 'NO'.

    Args:
        a (str): Première chaîne de caractères.
        b (str): Deuxième chaîne de caractères.
        c (str): Troisième chaîne de caractères.

    Returns:
        str: 'YES' si les conditions sont remplies, 'NO' sinon.
    """
    # Vérifier si le dernier caractère de 'a' correspond au premier caractère de 'b'
    first_condition = a[-1] == b[0]

    # Vérifier si le dernier caractère de 'b' correspond au premier caractère de 'c'
    second_condition = b[-1] == c[0]

    # Retourner 'YES' uniquement si les deux conditions sont vraies, sinon 'NO'
    return 'YES' if first_condition and second_condition else 'NO'


if __name__ == "__main__":
    # Lire l'entrée utilisateur et séparer en trois chaînes de caractères
    a, b, c = input().split()

    # Vérifier la séquence et afficher le résultat
    print(check_string_sequence(a, b, c))