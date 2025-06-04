def is_even_number_of_odds(numbers):
    """
    Détermine si le nombre d'éléments impairs dans la liste donnée est pair.

    Args:
        numbers (list of int): La liste des entiers à analyser.

    Returns:
        bool: True si le nombre de nombres impairs est pair, False sinon.
    """
    # Appliquer le modulo 2 à chaque élément pour déterminer la parité (0 si pair, 1 si impair)
    parities = list(map(lambda x: x % 2, numbers))
    # Compter le nombre d'éléments impairs (nombre de 1 dans la liste des parités)
    odd_count = parities.count(1)
    # Retourne True si ce nombre est pair, sinon False
    return odd_count % 2 == 0

def main():
    """
    Fonction principale : lit les entrées utilisateurs, détermine la parité du nombre d'impairs,
    puis affiche 'YES' si ce nombre est pair, sinon 'NO'.
    """
    # Lire un entier depuis l'entrée standard (correspond au nombre d'éléments)
    n = int(input())
    # Lire une ligne d'entiers séparés par des espaces et les convertir en liste d'entiers
    a = list(map(int, input().split()))
    # Vérifier si le nombre d'éléments impairs est pair
    if is_even_number_of_odds(a):
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()