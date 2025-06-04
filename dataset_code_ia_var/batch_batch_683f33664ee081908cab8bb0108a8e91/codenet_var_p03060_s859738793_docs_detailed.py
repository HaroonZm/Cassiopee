def calculate_total_gain(n, v, c):
    """
    Calcule le gain total en additionnant la différence 'v[i] - c[i]' pour chaque 'i' où v[i] > c[i].

    Args:
        n (int): Le nombre d'éléments dans les listes v et c.
        v (list of int): Liste des valeurs v.
        c (list of int): Liste des valeurs c.

    Returns:
        int: Le gain total cumulé pour tous les indices où v[i] > c[i].
    """
    # Initialiser la variable qui stockera la somme totale
    ans = 0
    # Parcourir toutes les positions de 0 à n-1
    for i in range(n):
        # Vérifier si la valeur v[i] est supérieure à la valeur c[i]
        if v[i] > c[i]:
            # Ajouter la différence à la somme totale
            ans += v[i] - c[i]
    # Retourner le gain total calculé
    return ans


if __name__ == "__main__":
    # Lire le nombre d'éléments de la séquence
    n = int(input())
    # Lire la liste des valeurs v, séparées par des espaces et converties en entiers
    v = list(map(int, input().split()))
    # Lire la liste des valeurs c, séparées par des espaces et converties en entiers
    c = list(map(int, input().split()))
    # Calculer le gain total à l'aide de la fonction dédiée
    result = calculate_total_gain(n, v, c)
    # Afficher le résultat final
    print(result)