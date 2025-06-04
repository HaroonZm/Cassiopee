def compute_prefix_sums(arr):
    """
    Calcule la somme cumulative (préfixée) d'une liste de nombres.

    Args:
        arr (list of int): Liste des entiers pour lesquels calculer les sommes préfixées.

    Returns:
        list of int: Liste des sommes préfixées.
    """
    n = len(arr)
    prefix_sums = [0] * n
    prefix_sums[0] = arr[0]
    for i in range(1, n):
        prefix_sums[i] = arr[i] + prefix_sums[i - 1]
    return prefix_sums

def min_operations_to_alternate_sign(prefix_sums):
    """
    Calcule le nombre minimal d'opérations nécessaires pour que les
    sommes partielles alternent de signe, en modifiant les valeurs par addition.

    Deux alternatives sont considérées :
    - La première grosseur est positive (commence par '+')
    - La première grosseur est négative (commence par '-')

    Args:
        prefix_sums (list of int): Liste des sommes préfixées du tableau d'origine.

    Returns:
        int: Le nombre minimal d'opérations nécessaires.
    """
    n = len(prefix_sums)

    # Option 1 : La première somme doit être positive, les suivantes alternent
    ans1 = 0  # Nombre total d'opérations
    offset1 = 0  # Décalage cumulé appliqué pour maintenir l'alternance de signe
    for i in range(n):
        current = prefix_sums[i] + offset1
        if i % 2 == 0:
            # Doit être strictement positif
            if current <= 0:
                delta = 1 - current  # Quantité à ajouter pour qu'il soit 1
                ans1 += delta
                offset1 += delta
        else:
            # Doit être strictement négatif
            if current >= 0:
                delta = current + 1  # Quantité à soustraire pour qu'il soit -1
                ans1 += delta
                offset1 -= delta

    # Option 2 : La première somme doit être négative, les suivantes alternent
    ans2 = 0  # Nombre total d'opérations
    offset2 = 0  # Même principe, mais démarre de signe opposé
    for i in range(n):
        current = prefix_sums[i] + offset2
        if i % 2 != 0:
            # Doit être strictement positif
            if current <= 0:
                delta = 1 - current
                ans2 += delta
                offset2 += delta
        else:
            # Doit être strictement négatif
            if current >= 0:
                delta = current + 1
                ans2 += delta
                offset2 -= delta

    # On retourne le minimum des deux stratégies
    return min(ans1, ans2)

def main():
    """
    Fonction principale pour lire les entrées,
    calculer les sommes préfixées, et afficher la
    solution selon le problème défini.
    """
    n = int(input())
    ar = list(map(int, input().split()))
    prefix_sums = compute_prefix_sums(ar)
    result = min_operations_to_alternate_sign(prefix_sums)
    print(result)

if __name__ == "__main__":
    main()