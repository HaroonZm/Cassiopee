def read_input():
    """
    Lit deux entiers depuis l'entrée standard.

    Returns:
        tuple: Un tuple contenant deux entiers lus à partir de l'entrée utilisateur.
    """
    A = int(input())
    B = int(input())
    return A, B

def find_missing_number(A, B):
    """
    Trouve et retourne le nombre manquant parmi les entiers 1, 2 et 3, sachant que A et B sont deux d'entre eux.

    Args:
        A (int): Premier nombre donné (doit être soit 1, 2 ou 3).
        B (int): Deuxième nombre donné (doit être soit 1, 2 ou 3).

    Returns:
        int: Le nombre manquant parmi 1, 2 et 3.
    """
    # La somme des nombres 1, 2 et 3 est toujours égale à 6.
    # Donc, le nombre manquant peut être trouvé par 6 - (A + B).
    return 6 - (A + B)

def main():
    """
    Fonction principale du programme. Lit deux entiers de l'utilisateur
    et affiche le nombre manquant parmi 1, 2 et 3.
    """
    # Lire les deux entrées utilisateur
    A, B = read_input()
    # Calculer le nombre manquant
    missing = find_missing_number(A, B)
    # Afficher le résultat
    print(missing)

# Appeler la fonction principale si ce script est exécuté
if __name__ == '__main__':
    main()