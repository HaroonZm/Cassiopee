def read_input():
    """
    Lit une ligne d'entrée standard, la divise en deux nombres entiers et les retourne.

    Returns:
        tuple: Un tuple contenant deux entiers (x, y) lus depuis l'entrée.
    """
    x_str, y_str = input().split()
    x = int(x_str)
    y = int(y_str)
    return x, y

def to_32bit_binary(value):
    """
    Convertit un entier en une chaîne binaire de 32 bits, complétée par des zéros à gauche si nécessaire.

    Args:
        value (int): L'entier à convertir.

    Returns:
        str: Représentation binaire de 32 bits de la valeur.
    """
    return format(value, '032b')

def bitwise_operations(x, y):
    """
    Effectue les opérations logiques 'et', 'ou' et 'xor' sur deux entiers.

    Args:
        x (int): Le premier entier.
        y (int): Le second entier.

    Returns:
        tuple: Un tuple de chaînes, chacune représentant le résultat binaire 32 bits des opérations 'et', 'ou', et 'xor' respectivement.
    """
    and_result = x & y         # Opération AND entre x et y
    or_result = x | y          # Opération OR entre x et y
    xor_result = x ^ y         # Opération XOR entre x et y
    # Conversion des résultats en binaire sur 32 bits
    return (to_32bit_binary(and_result), 
            to_32bit_binary(or_result), 
            to_32bit_binary(xor_result))

def main():
    """
    Fonction principale exécutant la lecture de l'entrée, les opérations logiques et l'affichage du résultat.
    """
    # Lire deux entiers depuis l'entrée standard
    x, y = read_input()
    # Effectuer les opérations logiques et obtenir les chaînes binaires 32 bits
    bin_and, bin_or, bin_xor = bitwise_operations(x, y)
    # Afficher les résultats
    print(bin_and)
    print(bin_or)
    print(bin_xor)

# Exécution du programme principal
if __name__ == "__main__":
    main()