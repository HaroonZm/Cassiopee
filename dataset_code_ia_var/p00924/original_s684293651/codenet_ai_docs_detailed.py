def read_input():
    """
    Lit les entrées utilisateur pour n, m, b et p.

    Returns:
        n (int): Taille du tableau b.
        m (int): Nombre d'éléments dans p.
        b (tuple): Tableau initial sous forme de tuple d'entiers.
        p (list): Séquence à rechercher, liste d'entiers.
    """
    n, m = map(int, input().split())
    b = tuple(map(int, input().split()))
    p = list(map(int, input().split()))
    return n, m, b, p

def enumerate_permutations(n, initial_b):
    """
    Génère toutes les permutations atteignables par transpositions successives de voisins,
    en calculant leur distance en nombre de transpositions à partir de initial_b.

    Args:
        n (int): Taille du tableau.
        initial_b (tuple): Tableau initial.

    Returns:
        ss (dict): Dictionnaire associant chaque permutation atteinte (tuple) à sa distance minimale (int).
        max_depth (int): Profondeur maximale atteinte (i.e. nombre minimal d'opérations nécessaires pour obtenir la permutation la plus lointaine).
    """
    current_depth = 0           # Niveau actuel (nombre de transpositions faites)
    permutation_depth = {}      # Associe à chaque permutation sa profondeur minimale
    current_frontier = []       # Utilisé pour lister les nouvelles permutations à ce niveau
    next_frontier = [initial_b] # Initialement, la seule permutation atteinte est initial_b

    while next_frontier:
        # Préparation du front pour l'étape suivante
        current_frontier, next_frontier = next_frontier, []
        while current_frontier:
            b = current_frontier.pop()
            if b not in permutation_depth:
                # On marque cette permutation comme atteinte pour la première fois à ce niveau
                permutation_depth[b] = current_depth
                b_list = list(b)
                for i in range(n - 1):
                    # Échange des éléments voisins i et i+1
                    b_list[i], b_list[i + 1] = b_list[i + 1], b_list[i]
                    # Ajout de la nouvelle permutation à explorer à l'étape suivante
                    next_frontier.append(tuple(b_list))
                    # Remise en place pour permettre l'autre échange
                    b_list[i + 1], b_list[i] = b_list[i], b_list[i + 1]
        current_depth += 1

    return permutation_depth, current_depth

def compute_block_sizes(permutation):
    """
    Calcule les tailles de blocs consécutifs de même élément dans une permutation.

    Args:
        permutation (tuple): La permutation sur laquelle calculer les blocs.

    Returns:
        res (list): Liste des tailles de blocs consécutifs.
    """
    res = []
    count = 1
    for i in range(1, len(permutation)):
        if permutation[i - 1] == permutation[i]:
            count += 1
        else:
            res.append(count)
            count = 1
    res.append(count)
    return res

def minimal_swaps_to_pattern(n, m, b, p):
    """
    Trouve le nombre minimal de transpositions voisin-voisin nécessaires pour
    que le tableau b puisse être transformé en une permutation dont les tailles
    de blocs de valeurs identiques correspondent exactement au motif p.

    Args:
        n (int): Taille du tableau b.
        m (int): Longueur du motif p.
        b (tuple): Tableau initial.
        p (list): Motif de bloc à atteindre.

    Returns:
        int: Nombre minimal de transpositions nécessaires, ou profondeur si motif jamais atteint.
    """
    # Génération de toutes les permutations atteignables et la profondeur (distance) minimale pour chacune
    perms_depth, max_depth = enumerate_permutations(n, b)
    min_swaps = max_depth
    # Pour chaque permutation atteinte, on vérifie si sa suite de blocs correspond
    for perm, depth in perms_depth.items():
        block_sizes = compute_block_sizes(perm)
        if block_sizes == p and depth < min_swaps:
            min_swaps = depth
    return min_swaps

def main():
    """
    Fonction principale exécutant le programme : lecture des entrées, calcul et affichage du résultat.
    """
    n, m, b, p = read_input()
    result = minimal_swaps_to_pattern(n, m, b, p)
    print(result)

# Lancement du programme
main()