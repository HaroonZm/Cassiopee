import sys

def can_form_set(a, b, c):
    """
    Détermine si, pour les entiers a, b, c donnés, le nombre d'entiers différents
    entre 1 et (20 - a - b) exclusif qui sont distincts de a, b, c est inférieur à 3.5.

    Args:
        a (int): Premier entier à exclure.
        b (int): Deuxième entier à exclure.
        c (int): Troisième entier à exclure.

    Returns:
        bool: True si le nombre d'éléments dans l'ensemble de référence privés de {a, b, c}
        est inférieur à 3.5, False sinon.
    """
    # Crée un ensemble des nombres de 1 à (20 - a - b) (exclu)
    base_set = set(range(1, 21 - a - b))
    # Retire les éléments a, b et c de ce set
    remaining = base_set - {a, b, c}
    # Renvoie True si la condition sur le nombre d'éléments est remplie
    return len(remaining) < 3.5

def main():
    """
    Fonction principale qui lit les entrées standard ligne par ligne,
    extrait trois entiers par ligne, puis affiche 'YES' ou 'NO' selon la logique de can_form_set.
    """
    # Parcourt chaque ligne d'entrée standard
    for line in sys.stdin:
        # Découpe la ligne en entiers a, b, c
        a, b, c = map(int, line.split())
        # Affiche 'YES' si la condition est remplie, 'NO' sinon
        print('YES' if can_form_set(a, b, c) else 'NO')

# Exécute la fonction principale si ce script est exécuté directement
if __name__ == "__main__":
    main()