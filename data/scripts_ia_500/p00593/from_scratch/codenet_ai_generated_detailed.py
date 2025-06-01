# Solution complète en Python pour générer le parcours en zigzag d'une matrice NxN
# Chaque élément de la matrice contient le numéro de visite dans la trajectoire zigzag
# Le parcours commence en haut à gauche (0,0) et termine en bas à droite (N-1,N-1)
# La numérotation commence à 1

def zigzag_order(N):
    """
    Calcule la matrice des temps de visite par parcours zigzag sur une matrice NxN.
    :param N: taille de la matrice (int)
    :return: matrice NxN où chaque élément indique l'ordre de visite (int)
    """
    result = [[0]*N for _ in range(N)]
    
    # Le parcours zigzag suit la diagonale somme des indices i+j = d
    # d varie de 0 à 2*(N-1)
    # Pour chaque diagonale d, on récupère les paires (i,j) telles que i+j=d
    # L'ordre de parcours alterne : pour d pair on va de bas en haut,
    # pour d impair on va de haut en bas
    
    count = 1  # numéro de visite
    
    for d in range(2*N - 1):
        if d % 2 == 0:
            # d pair: parcourir du bas vers haut : i décroissant, j croissant
            # i varie entre max(0, d-(N-1)) et min(d, N-1)
            i_start = max(0, d-(N-1))
            i_end = min(d, N-1)
            # On parcourt i de i_end à i_start (décroissant)
            for i in range(i_end, i_start - 1, -1):
                j = d - i
                result[i][j] = count
                count += 1
        else:
            # d impair: parcourir du haut vers bas : i croissant, j décroissant
            i_start = max(0, d-(N-1))
            i_end = min(d, N-1)
            for i in range(i_start, i_end + 1):
                j = d - i
                result[i][j] = count
                count += 1
    return result


def main():
    case_num = 1
    while True:
        N = int(input())
        if N == 0:
            break
        result = zigzag_order(N)
        print(f"Case {case_num}:")
        for row in result:
            # Chaque élément justifié à droite sur 3 espaces
            print("".join(f"{num:3d}" for num in row).lstrip())
        case_num += 1


if __name__ == "__main__":
    main()