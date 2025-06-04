def can_construct_bridge(n, l, a):
    """
    Détermine s'il est possible de construire le pont en respectant la contrainte de poids,
    puis génère la séquence d'étapes de construction si possible.

    Args:
        n (int): Nombre total de planches constituant le pont.
        l (int): Longueur minimale requise de chaque découpe de planche consécutive.
        a (list of int): Liste des longueurs des planches.

    Returns:
        tuple:
            - bool: True si la construction est possible, False sinon.
            - list of int: Séquence d'indices pour la construction ou liste vide si impossible.
    """
    failflag = True  # Indique si on a rencontré un problème (Impossible) au départ
    # Parcours de toutes les paires consécutives de planches
    for i in range(n - 1):
        # Vérifie si la somme de deux planches consécutives atteint la longueur minimale
        if a[i] + a[i + 1] >= l:
            failflag = False  # Il existe une paire adéquate, donc la construction est possible
            k = i  # L'indice où la découpe permet de satisfaire la condition
            break  # On a trouvé une option valide, on sort de la boucle

    if failflag:
        # Si aucune paire n'est valide, il est impossible de construire le pont
        return False, []
    else:
        # Il est possible de construire le pont.
        # Génère la séquence d'indices nécessaires pour la construction
        steps = []
        # On ajoute d'abord les indices de 1 à k (inclusions à gauche)
        for i in range(1, k + 1):
            steps.append(i)
        # Ensuite, on ajoute les indices à partir de la droite jusqu'à l'indice k+1 (inclusion à droite)
        for i in range(n - 1 - k):
            steps.append(n - 1 - i)
        return True, steps

def main():
    """
    Point d'entrée du programme. Lit l'entrée utilisateur, traite les données et imprime le résultat.
    """
    # Lecture de la première ligne : nombre de planches et longueur minimale
    n, l = map(int, input().split())
    # Lecture de la deuxième ligne : longueurs des planches
    a = list(map(int, input().split()))
    # Évaluation de la possibilité de construction et récupération de la séquence d'étapes
    possible, steps = can_construct_bridge(n, l, a)
    if not possible:
        print('Impossible')
    else:
        print('Possible')
        for step in steps:
            print(step)

# Lancement du programme principal lorsque le script est exécuté
if __name__ == "__main__":
    main()