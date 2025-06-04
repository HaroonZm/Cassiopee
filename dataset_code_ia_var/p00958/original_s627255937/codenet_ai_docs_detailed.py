from math import gcd

def read_input_points(m):
    """
    Lit m points depuis l'entrée standard et retourne une liste de points.
    
    Args:
        m (int): Le nombre de points à lire.

    Returns:
        list: Une liste de points, chaque point étant une liste [x, y].
    """
    points = [list(map(int, input().split())) for _ in range(m)]
    return points

def reduce_direction(x, y):
    """
    Réduit le vecteur (x, y) à sa direction canonique (avec coefficients premiers entre eux).
    Garde la cohérence du signe.

    Args:
        x (int): Différence sur l'axe x.
        y (int): Différence sur l'axe y.

    Returns:
        tuple: Un tuple représentant la direction réduite.
    """
    if x == 0 and y == 0:
        return (0, 0)
    d = gcd(x, y)
    rx, ry = x // d, y // d
    # Assure que la représentation (-a, -b) et (a, b) soit la même
    if rx < 0 or (rx == 0 and ry < 0):
        rx, ry = -rx, -ry
    return (rx, ry)

def find_direction_pairs(points):
    """
    Génère un dictionnaire où chaque clé est une direction canonique
    et la valeur est la liste des paires de points correspondant à cette direction.

    Args:
        points (list): Liste de points [x, y].

    Returns:
        dict: Dictionnaire des directions et des paires de points correspondantes.
    """
    tmp = {}
    m = len(points)
    for i, pi in enumerate(points):
        for j, pj in enumerate(points):
            if i == j:
                break  # Uniquement les couples (i, j) où i > j (évite doublons & i==j)
            x = pi[0] - pj[0]
            y = pi[1] - pj[1]
            k = reduce_direction(x, y)
            if k in tmp:
                tmp[k].append([pi, pj])
            else:
                tmp[k] = [[pi, pj]]
    return tmp

def filter_multiple_direction_lines(tmp):
    """
    Filtre le dictionnaire pour ne garder que les directions associées à plusieurs paires.

    Args:
        tmp (dict): Dictionnaire direction -> listes de paires de points.

    Returns:
        dict: Sous-dictionnaire où il y a plus d'une paire par direction.
    """
    dic = {}
    for direction in tmp:
        if len(tmp[direction]) == 1:
            continue
        dic[direction] = tmp[direction]
    return dic

def compute_max_group(dic):
    """
    Calcule la valeur maximale anstmp trouvée par la recherche de combinaisons de 4 directions.

    Args:
        dic (dict): Dictionnaire filtré des directions avec plusieurs paires.

    Returns:
        int: La valeur maximale anstmp trouvée.
    """
    ans = 0
    directions = list(dic.keys())

    for d1 in directions:
        # Première famille de segments colinéaires (même direction)
        line1 = dic[d1]
        used1 = [pt for pair in line1 for pt in pair]  # Points déjà utilisés

        for d2 in directions:
            tmp2 = []
            for pair in dic[d2]:
                # On ne prends que les paires disjointes
                if pair[0] in used1 or pair[1] in used1:
                    continue
                tmp2.append(pair)
            if len(tmp2) <= 1:
                continue
            line2 = tmp2
            used2 = used1 + [pt for pair in tmp2 for pt in pair]

            for d3 in directions:
                tmp3 = []
                for pair in dic[d3]:
                    if pair[0] in used2 or pair[1] in used2:
                        continue
                    tmp3.append(pair)
                if len(tmp3) <= 1:
                    continue
                line3 = tmp3
                used3 = used2 + [pt for pair in tmp3 for pt in pair]

                for d4 in directions:
                    tmp4 = []
                    for pair in dic[d4]:
                        if pair[0] in used3 or pair[1] in used3:
                            continue
                        tmp4.append(pair)
                    if len(tmp4) <= 1:
                        continue
                    # Calcul du score temporaire pour cette combinaison
                    anstmp = 0
                    for group in [line1, line2, line3, tmp4]:
                        n = len(group)
                        # On compte le nombre de façons de choisir 2 paires dans chaque groupe
                        anstmp += n * (n - 1) / 2
                    ans = max(ans, anstmp)
    return int(ans)

def main():
    """
    Fonction principale gérant la lecture, le traitement et l'affichage du résultat final.
    """
    m = int(input())
    points = read_input_points(m)
    tmp = find_direction_pairs(points)
    dic = filter_multiple_direction_lines(tmp)
    ans = compute_max_group(dic)
    print(ans)

if __name__ == "__main__":
    main()