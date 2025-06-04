def to_32bit_binary_str(n):
    """
    Convertit un entier en chaîne binaire sur 32 bits.

    Args:
        n (int): L'entier à convertir.

    Returns:
        str: Représentation binaire sur 32 bits de l'entier.
    """
    return "{:032b}".format(n)

def main():
    """
    Lit deux entiers depuis l'entrée standard, effectue les opérations
    ET, OU et OU exclusif au niveau bit à bit, puis affiche le résultat
    de chaque opération sous forme binaire sur 32 bits.
    """
    # Lecture de deux entiers séparés par un espace depuis l'entrée standard
    a, b = map(int, input().split())

    # Application de l'opération ET bit à bit (&) entre a et b
    result_and = a & b
    # Application de l'opération OU bit à bit (|) entre a et b
    result_or = a | b
    # Application de l'opération OU exclusif bit à bit (^) entre a et b
    result_xor = a ^ b

    # Affichage des résultats pour chaque opération, formatés en binaire sur 32 bits
    print(to_32bit_binary_str(result_and))  # Résultat de l'ET bit à bit
    print(to_32bit_binary_str(result_or))   # Résultat du OU bit à bit
    print(to_32bit_binary_str(result_xor))  # Résultat du OU exclusif bit à bit

if __name__ == "__main__":
    main()