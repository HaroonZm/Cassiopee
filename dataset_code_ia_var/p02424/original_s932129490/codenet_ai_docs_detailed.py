def bitwise_operations(a: int, b: int) -> str:
    """
    Effectue les opérations binaires ET, OU et OU exclusif entre deux entiers donnés,
    puis retourne une chaîne avec leurs représentations binaires respectives sur 32 bits.

    Args:
        a (int): Premier entier.
        b (int): Second entier.

    Returns:
        str: Représentation sur 32 bits de (a & b), (a | b) et (a ^ b), séparées par des sauts de ligne.
    """
    # Opération ET bit à bit entre a et b, avec formatage en binaire sur 32 bits
    and_result = f"{a & b:032b}"

    # Opération OU bit à bit entre a et b, formatée sur 32 bits
    or_result = f"{a | b:032b}"

    # Opération OU exclusif (XOR) bit à bit entre a et b, formatée sur 32 bits
    xor_result = f"{a ^ b:032b}"

    # Retourne les trois résultats, chacun sur une ligne
    return f"{and_result}\n{or_result}\n{xor_result}"

def main():
    """
    Demande à l'utilisateur d'entrer deux entiers séparés par un espace,
    puis affiche le résultat des opérations binaires ET, OU et OU exclusif
    en format binaire, sur 32 bits pour chaque résultat.
    """
    # Demande à l'utilisateur de saisir deux entiers séparés par un espace
    a, b = map(int, input().split())

    # Appelle la fonction de calcul et affiche les résultats
    print(bitwise_operations(a, b))

if __name__ == "__main__":
    main()