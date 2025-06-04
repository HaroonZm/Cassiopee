"""
Bitset II - Enumeration of Combinations

Ce programme énumère toutes les combinaisons possibles de k éléments parmi n,
les encode sous forme de bitset (entier), puis affiche dans l'ordre croissant
la forme entière et les indices des éléments de chaque combinaison.

Entrée:
    Deux entiers n, k séparés par des espaces.
Sortie:
    Pour chaque combinaison, en ordre croissant de bitset :
    <bitset>: <indice1> <indice2> ... <indiceK>
"""

from itertools import combinations

def read_input():
    """
    Lit deux entiers depuis l'entrée standard.

    Returns:
        tuple: Un tuple (n, k) où n est le nombre total d'éléments,
               k le nombre d'éléments à choisir.
    """
    n, k = map(int, input().split())
    return n, k

def bitset_from_indices(indices):
    """
    Calcule la valeur entière du bitset correspondant à une liste d'indices.

    Args:
        indices (iterable): Un iterable d'indices entiers.

    Returns:
        int: L'entier dont les bits à la position des indices sont à 1.
    """
    return sum([1 << b for b in indices])

def enumerate_combinations_with_bitsets(n, k):
    """
    Génère toutes les combinaisons de k éléments parmi n, calcule leur bitset associé
    et prépare une sortie triée par valeur de bitset.

    Args:
        n (int): Nombre total d'éléments.
        k (int): Nombre d'éléments à choisir.

    Returns:
        list of tuple: Liste de tuples (bitset, indices_str), où bitset est l'entier
                       représentant la combinaison, indices_str une chaîne des indices.
    """
    results = []
    # Génération de toutes les combinaisons de k indices sur [0, n)
    for c in combinations(range(n), k):
        bitset = bitset_from_indices(c)
        indices_str = ' '.join(map(str, c))
        results.append((bitset, indices_str))
    # Trie les résultats selon la valeur entière du bitset
    results.sort()
    return results

def main():
    """
    Point d'entrée du programme :
      - Lit l'entrée standard.
      - Génère et affiche toutes les combinaisons au format demandé.
    """
    n, k = read_input()
    combi_with_bitsets = enumerate_combinations_with_bitsets(n, k)
    for bitset, indices in combi_with_bitsets:
        print(f'{bitset}: {indices}')

if __name__ == '__main__':
    main()