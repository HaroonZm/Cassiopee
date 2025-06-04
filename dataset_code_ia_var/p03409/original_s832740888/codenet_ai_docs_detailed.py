def max_matching_pairs(input_data):
    """
    Calcule le nombre maximal de paires correspondantes entre deux listes de tuples,
    selon des critères d'appariement spécifiques :
      - Pour chaque paire (i, j) dans la seconde liste ('y'), on cherche une paire (a, b) dans la première ('x')
        telle que a < i et b < j. Chaque élément de 'x' ne peut être utilisé qu'une seule fois.

    Args:
        input_data (str): Une chaîne contenant tous les entiers de l'entrée séparés par des espaces :
                          - Le premier entier est n, le nombre d'éléments dans chaque liste.
                          - Les 2n entiers suivants sont les paires pour la liste 'x'.
                          - Les 2n entiers suivants sont les paires pour la liste 'y'.

    Returns:
        int: Le nombre maximal de paires correspondantes trouvées.
    """
    # Conversion de l'entrée en une liste d'entiers
    n, *t = map(int, input_data.split())

    # Création et tri de la première liste de n paires (b, a) à partir des 2n premiers éléments
    #   - t[:n*2:2] : valeurs 'a' (index pairs de 0 à 2n-2)
    #   - t[1:n*2:2] : valeurs 'b' (index impairs de 1 à 2n-1)
    x = sorted(zip(t[1:n*2:2], t[:n*2:2]))

    # Création et tri de la seconde liste de n paires (i, j) à partir des 2n éléments suivants
    #   - t[n*2::2] : valeurs 'i' (index pairs à partir de 2n jusqu'à la fin)
    #   - t[n*2+1::2] : valeurs 'j' (index impairs à partir de 2n+1 jusqu'à la fin)
    # La liste est triée par défaut dans l'ordre croissant des 'i', puis des 'j', puis inversée.
    y = sorted(zip(t[n*2::2], t[n*2+1::2]))[::-1]

    # Compteur du nombre de paires valides trouvées
    c = 0

    # Tant qu'il reste des éléments à traiter dans y
    while y:
        # On récupère la prochaine paire (i, j) à traiter (la moins prioritaire du tri)
        i, j = y.pop()
        # On parcourt la liste 'x' de la fin vers le début (valeurs les plus grandes d'abord)
        k = len(x) - 1
        while k >= 0:
            b, a = x[k]
            # On vérifie si la paire (b, a) peut être appariée avec (i, j)
            if a < i and b < j:
                # Si appariement possible, on incrémente le compteur et enlève la paire utilisée de 'x'
                c += 1
                del x[k]
                break  # On passe à la paire suivante dans 'y'
            k -= 1
    # On retourne le nombre maximal de paires trouvées
    return c

if __name__ == "__main__":
    import sys
    # Lecture de toute l'entrée depuis stdin
    input_data = sys.stdin.read()
    # Calcul et affichage du résultat
    print(max_matching_pairs(input_data))