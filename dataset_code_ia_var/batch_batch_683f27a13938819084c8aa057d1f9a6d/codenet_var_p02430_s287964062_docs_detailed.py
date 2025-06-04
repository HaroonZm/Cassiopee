from itertools import combinations

def get_input():
    """
    Lit deux entiers séparés par un espace depuis l'entrée standard.
    Le premier entier correspond à 'n', la taille de l'ensemble.
    Le second entier correspond à 'k', la taille des sous-ensembles à générer.

    Returns:
        tuple: Un tuple contenant deux entiers (n, k).
    """
    n, k = [int(x) for x in input().split()]
    return n, k

def generate_bitwise_combinations(n, k):
    """
    Génère tous les sous-ensembles de longueur k d'un ensemble de n éléments (allant de 0 à n-1),
    et associe à chaque sous-ensemble sa représentation binaire sous forme d'entier.

    Args:
        n (int): Taille de l'ensemble de base.
        k (int): Taille des sous-ensembles à générer.

    Returns:
        list: Une liste de tuples de la forme (bitnum, comb), où :
            - bitnum (int) : L'entier dont la représentation binaire a des bits à 1 aux positions des éléments du sous-ensemble.
            - comb (tuple): Un tuple contenant le sous-ensemble d'entiers (positions choisies).
    """
    # Génère la liste des indices de l'ensemble de base (de 0 à n-1)
    L = [x for x in range(n)]
    result = []

    # Génère toutes les combinaisons possibles d'indices de longueur k
    for subset in combinations(L, k):
        bitnum = 0  # Représentation binaire sous forme d'entier
        # Pour chaque indice dans le sous-ensemble, positionne le bit correspondant dans bitnum
        for i in subset:
            bitnum |= 1 << i
        # Ajoute le tuple (bitnum, subset) à la liste de résultats
        result.append((bitnum, subset))
    return result

def print_sorted_bitwise_combinations(bitwise_combinations):
    """
    Trie la liste des sous-ensembles selon leur représentation binaire, puis les affiche.

    Args:
        bitwise_combinations (list): Liste de tuples (bitnum, subset), où :
            - bitnum (int) : Représentation binaire du sous-ensemble.
            - subset (tuple): Sous-ensemble correspondant.
    """
    # Trie les tuples selon la valeur de bitnum
    bitwise_combinations.sort()
    # Parcourt et affiche chaque sous-ensemble avec sa valeur binaire
    for bitnum, subset in bitwise_combinations:
        print(f"{bitnum}: ", end="")
        print(*subset)

def main():
    """
    Fonction principale.
    Récupère les entrées utilisateur, génère toutes les combinaisons possibles,
    puis affiche le résultat trié selon leurs représentations binaires.
    """
    n, k = get_input()
    bitwise_combinations = generate_bitwise_combinations(n, k)
    print_sorted_bitwise_combinations(bitwise_combinations)

# Point d'entrée du programme
if __name__ == "__main__":
    main()