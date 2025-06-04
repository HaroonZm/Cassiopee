import sys

def read_input_values():
    """
    Lit deux entiers s et t depuis l'entrée standard, séparés par un espace.

    Returns:
        tuple: Un tuple contenant les deux entiers (s, t).
    """
    s, t = map(int, input().split())
    return s, t

def skip_next_input_line():
    """
    Ignore la prochaine ligne de l'entrée standard.
    Cela permet de lire et de ne pas utiliser une ligne superflue, typiquement un séparateur ou une donnée inutile.
    """
    input()

def read_integer():
    """
    Lit un entier depuis l'entrée standard.

    Returns:
        int: L'entier lu depuis l'entrée.
    """
    y = int(input())
    return y

def compute_xor(s, t, y):
    """
    Calcule le résultat du XOR entre trois entiers s, t et y.

    Args:
        s (int): Le premier entier.
        t (int): Le deuxième entier.
        y (int): Le troisième entier.

    Returns:
        int: Le résultat de l'opération s ^ t ^ y (XOR bit à bit).
    """
    return s ^ t ^ y

def main():
    """
    Programme principal :
    1. Lit deux entiers s et t depuis l'entrée.
    2. Ignore la ligne suivante de l'entrée.
    3. Lit un entier y depuis l'entrée.
    4. Affiche le résultat du XOR entre s, t et y.
    """
    s, t = read_input_values()        # Étape 1 : lire s, t
    skip_next_input_line()            # Étape 2 : ignorer la prochaine ligne
    y = read_integer()                # Étape 3 : lire y
    result = compute_xor(s, t, y)     # Étape 4 : calculer le XOR
    print(result)                     # Afficher le résultat

if __name__ == "__main__":
    main()