def calculate_sum_of_quotient_and_remainder(D, L):
    """
    Calcule la somme du reste et du quotient de la division entière de D par L.

    Args:
        D (int): Le dividende.
        L (int): Le diviseur.

    Returns:
        int: La somme du reste (modulo) et du quotient (division entière) de D par L.
    """
    remainder = D % L  # Calcule le reste de la division de D par L
    quotient = D // L  # Calcule le quotient entier de la division de D par L
    return remainder + quotient  # Retourne la somme du reste et du quotient

# Lecture des deux entiers séparés par un espace depuis l'entrée standard
D, L = map(int, input().split())

# Appel de la fonction avec les valeurs entrées et affichage du résultat
print(calculate_sum_of_quotient_and_remainder(D, L))