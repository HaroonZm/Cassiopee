def check_value(x: int, a: int) -> int:
    """
    Compare deux entiers et retourne 0 si le premier est strictement inférieur au second, sinon retourne 10.

    Args:
        x (int): La première valeur entière à comparer.
        a (int): La seconde valeur entière à comparer.

    Returns:
        int: 0 si x < a, sinon 10.
    """
    # On compare les deux valeurs et retourne le résultat approprié.
    if x < a:
        return 0
    else:
        return 10

def main():
    """
    Fonction principale.
    Lit deux entiers depuis l'entrée standard, puis affiche le résultat de la comparaison
    selon les spécifications de la fonction check_value.
    """
    # Lecture de deux entiers séparés par un espace à partir de l'entrée standard.
    x, a = map(int, input().split())

    # Appel de la fonction de comparaison, puis impression du résultat.
    print(check_value(x, a))

# Exécute la fonction principale si ce script est appelé directement.
if __name__ == "__main__":
    main()