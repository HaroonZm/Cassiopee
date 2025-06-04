def read_two_integers():
    """
    Lit deux entiers de l'entrée standard séparés par un espace.

    Returns:
        tuple: Un tuple contenant deux entiers (a, b)
    """
    a_str, b_str = input().split()
    a = int(a_str)
    b = int(b_str)
    return a, b

def format_32bit_binary(value):
    """
    Convertit un entier en une chaîne binaire de 32 bits avec des zéros précédents.

    Args:
        value (int): L'entier à convertir.

    Returns:
        str: La représentation binaire sur 32 bits de value.
    """
    return "{:032b}".format(value)

def main():
    """
    Fonction principale qui lit deux entiers,
    effectue des opérations logiques binaires (AND, OR, XOR),
    et affiche leurs résultats au format binaire sur 32 bits.
    """
    # Lire deux entiers de l'utilisateur
    a, b = read_two_integers()

    # Constante pour 'masquer' sur 32 bits (tous les bits à 1 sur 32 bits)
    MASK = (1 << 32) - 1

    # Calcul et affichage du résultat AND (a & b) sur 32 bits
    print(format_32bit_binary(a & b))

    # Calcul et affichage du résultat OR (a | b) sur 32 bits
    print(format_32bit_binary(a | b))

    # Calcul et affichage du résultat XOR (a ^ b) sur 32 bits
    print(format_32bit_binary(a ^ b))

if __name__ == "__main__":
    main()