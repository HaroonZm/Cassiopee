from bisect import bisect_left as bl

def max_subarray_sum_modulo(n, m, klst):
    """
    Calcule la somme maximale d'un sous-tableau modulo m.

    Cette fonction reçoit la taille du tableau n, un entier modulo m,
    ainsi qu'une liste klst contenant n éléments. Elle calcule la somme
    maximale possible de n'importe quel sous-tableau de klst, prise modulo m.

    Args:
        n (int): La taille de la liste klst.
        m (int): L'entier modulo.
        klst (list of int): La liste des entiers.

    Returns:
        int: La somme maximale modulo m obtenue parmi tous les sous-tableaux.
    """
    # Calcul des sommes préfixes modulo m
    cum = []
    acc = 0
    for k in klst:
        acc += k
        acc %= m
        cum.append(acc)

    # Liste triée des sommes préfixes utilisées pour la recherche binaire
    use = [0]
    use_len = 1
    ans = 0

    for k in cum:
        # Recherche de la position d'insertion du prochain élément strictement supérieur à k
        ind = bl(use, k + 1)
        # Si un élément strictement supérieur est trouvé, on calcule une sous-somme candidate
        if ind < use_len:
            ans = max(ans, (k - use[ind]) % m)
        # On évalue aussi la valeur elle-même k comme candidate
        ans = max(ans, k)
        # Insertion de la somme préfixe k dans la liste triée use pour les prochaines itérations
        use.insert(bl(use, k), k)
        use_len += 1

    return ans


# Boucle principale pour la lecture des entrées
while True:
    # Lecture de deux entiers n (taille du tableau) et m (modulo)
    n, m = map(int, input().split())
    # Condition d'arrêt si n = 0
    if n == 0:
        break
    # Lecture de la liste des entiers
    klst = list(map(int, input().split()))
    # Calcul et affichage du résultat correspondant
    print(max_subarray_sum_modulo(n, m, klst))