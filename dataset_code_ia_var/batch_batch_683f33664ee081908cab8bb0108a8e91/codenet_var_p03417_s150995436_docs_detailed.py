def calculate_difference(n: int, m: int) -> int:
    """
    Calcule la différence absolue entre le produit de n et m et deux fois leur somme diminuée de 4.

    Plus formellement, calcule :
        abs((n * m) - (2 * (n + m) - 4))

    Args:
        n (int): La première dimension (par exemple, longueur).
        m (int): La seconde dimension (par exemple, largeur).

    Returns:
        int: La valeur absolue de la différence calculée.
    """
    # Calcule le produit des deux dimensions
    area = n * m
    # Calcule deux fois la somme des dimensions et enlève 4
    perimeter_correction = 2 * (n + m) - 4
    # Calcule la différence puis prend la valeur absolue
    result = abs(area - perimeter_correction)
    return result

def main():
    """
    Lit deux entiers depuis l'entrée standard, les passe à la fonction de calcul,
    puis affiche le résultat.
    """
    # Lit une ligne de l'entrée, la découpe et convertit chaque partie en int
    n, m = list(map(int, input().split()))
    # Calcule la différence et l'affiche
    print(calculate_difference(n, m))

# Appelle la fonction principale si ce script est exécuté
if __name__ == "__main__":
    main()