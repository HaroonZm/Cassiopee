import itertools

def compute_subset_sums(n, k):
    """
    Génère toutes les combinaisons d'indices de taille k parmi n éléments,
    calcule la somme des puissances de 2 correspondant à chaque indice de chaque combinaison,
    puis retourne les sommes et les combinaisons triées selon la valeur de la somme.
    
    Args:
        n (int): Nombre d'éléments (généralement la taille de l'ensemble de départ)
        k (int): Taille des combinaisons à générer
    
    Returns:
        tuple:
            - sumlist (list): Liste des sommes triées (chaque somme est la somme des 2^indice)
            - combs (list): Liste des combinaisons d'indices triées selon la somme
    """
    # Crée un objet range représentant les indices de l'ensemble de départ
    l = range(n)
    # Génère toutes les combinaisons possibles de k indices parmi n
    combs = list(itertools.combinations(l, k))
    
    # Liste destinée à stocker la somme 2^indice pour chaque combinaison
    sumlist = []
    # Pour chaque combinaison d'indices...
    for comb in combs:
        sum_comb = 0
        # ... additionne 2 à la puissance de chaque indice de la combinaison
        for c in comb:
            sum_comb += pow(2, c)
        # Ajoute la somme calculée à la liste
        sumlist.append(sum_comb)
    
    # Lie chaque somme à sa combinaison correspondante sous forme de tuples
    zipped = zip(sumlist, combs)
    # Trie les tuples selon la valeur de la somme (en ordre croissant)
    sorted_zipped = sorted(zipped)
    
    # Défait les tuples triés en deux listes distinctes (sommes et combinaisons)
    sumlist_sorted, combs_sorted = zip(*sorted_zipped)
    
    return sumlist_sorted, combs_sorted

def main():
    """
    Point d'entrée principal du script.
    Lit deux entiers depuis l'entrée standard, calcule les sommes des sous-ensembles,
    puis affiche chaque somme suivie de la combinaison correspondante d'indices.
    """
    # Récupère les deux entiers n et k depuis l'entrée standard de l'utilisateur
    n, k = map(int, input().split())
    
    # Calcule toutes les sommes possibles des puissances de 2 et les combinaisons associées
    sumlist, combs = compute_subset_sums(n, k)
    
    # Parcours des tuples (somme, combinaison) pour un affichage formaté
    for sum_value, comb in zip(sumlist, combs):
        # Convertit la combinaison d'indices en une chaîne de caractères séparée par des espaces
        c_str = ' '.join(str(c) for c in comb)
        # Affiche la somme et la combinaison formatée
        print(str(sum_value) + ": " + c_str)

# Exécution du programme principal si ce fichier est exécuté directement
if __name__ == "__main__":
    main()