def compute_result(s, t, p, q, M, y):
    """
    Calcule le résultat d'une opération XOR binaire sur les entiers y, s et t.

    Args:
        s (int): Premier nombre saisi à partir de la première ligne d'entrée.
        t (int): Deuxième nombre saisi à partir de la première ligne d'entrée.
        p (int): Premier nombre de la deuxième ligne d'entrée (actuellement inutilisé).
        q (int): Deuxième nombre de la deuxième ligne d'entrée (actuellement inutilisé).
        M (int): Troisième nombre de la deuxième ligne d'entrée (actuellement inutilisé).
        y (int): Nombre de la troisième ligne d'entrée.

    Returns:
        int: Le résultat de y XOR s XOR t.
    """
    # Opération XOR binaire sur les trois valeurs et retour du résultat
    return y ^ s ^ t

# Lecture et séparation de la première ligne d'entrée en deux entiers s et t
s, t = map(int, input().split())
# Lecture et séparation de la deuxième ligne d'entrée en trois entiers p, q, M
p, q, M = map(int, input().split())
# Lecture de la troisième ligne d'entrée, convertie en entier y
y = int(input())

# Calcul et affichage du résultat grâce à la fonction compute_result
print(compute_result(s, t, p, q, M, y))