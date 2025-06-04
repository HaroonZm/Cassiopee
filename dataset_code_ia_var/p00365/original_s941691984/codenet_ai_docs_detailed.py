def get_input_values():
    """
    Lit deux lignes depuis l'entrée standard, chacune contenant trois entiers séparés par des espaces.
    Retourne les deux triplets d'entiers (a, b, c) et (d, e, f).

    Returns:
        tuple: ((a, b, c), (d, e, f)) où chaque élément est un tuple de trois entiers.
    """
    a, b, c = map(int, input().split())
    d, e, f = map(int, input().split())
    return (a, b, c), (d, e, f)

def compute_min_difference(triplet1, triplet2):
    """
    Calcule et affiche la différence minimale entre deux triplets basés sur leurs valeurs respectives
    selon les règles spécifiques du problème.

    Les règles sont les suivantes :
        - Si b == e et c == f, alors afficher la différence absolue entre a et d, puis arrêter.
        - Si a et d sont égaux, afficher 1, puis arrêter.
        - Sinon, selon la comparaison entre a et d, aiguille num et nu.
        - Si num > nu, afficher abs(a-d)+1, sinon afficher abs(a-d).

    Args:
        triplet1 (tuple): Le premier triplet d'entiers (a, b, c).
        triplet2 (tuple): Le second triplet d'entiers (d, e, f).
    """
    a, b, c = triplet1
    d, e, f = triplet2

    # Si les deux triplets ont des composantes b et c identiques
    if b == e and c == f:
        print(abs(a - d))
        return

    # Si les composantes a sont égales, on affiche 1
    if a == d:
        print(1)
        return

    # Construire des valeurs composées pour comparer les "positions"
    # La valeur num est la combinaison pondérée de b, c ou e, f selon la position de a et d.
    if a > d:
        num = 100 * b + c
        nu = 100 * e + f
    else:
        num = 100 * e + f
        nu = 100 * b + c

    # Si num > nu, on ajoute 1 à la différence absolue de a-d
    if num > nu:
        print(abs(a - d) + 1)
    else:
        print(abs(a - d))

def main():
    """
    Fonction principale qui traite l'entrée et lance le calcul.
    """
    triplet1, triplet2 = get_input_values()
    compute_min_difference(triplet1, triplet2)

if __name__ == "__main__":
    main()