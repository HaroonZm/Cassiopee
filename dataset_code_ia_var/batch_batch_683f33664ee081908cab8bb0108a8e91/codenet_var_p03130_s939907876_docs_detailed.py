def read_point():
    """
    Lit une ligne d'entrée standard, la divise en deux entiers et les retourne en tant que tuple.
    Renvoie :
        tuple : Un couple d'entiers représentant les coordonnées d'un point.
    """
    return map(int, input().split())

def main():
    """
    Lit les coordonnées de trois points, compte la fréquence des valeurs distinctes,
    puis détermine si la distribution des fréquences correspond à celles attendues (1,1,2,2),
    qui caractérisent un rectangle aligné sur les axes dont les côtés sont parallèles aux axes.
    Affiche 'YES' si la condition est remplie, sinon affiche 'NO'.
    """
    # Lecture des coordonnées des trois points
    a1, b1 = read_point()
    a2, b2 = read_point()
    a3, b3 = read_point()

    # Création d'une liste contenant toutes les coordonnées
    coords = [a1, a2, a3, b1, b2, b3]

    # Liste pour stocker les occurrences de chaque valeur possible entre 1 et 4 (exclus 5)
    frequency_list = []
    for i in range(1, 5):
        frequency_count = coords.count(i)
        frequency_list.append(frequency_count)

    # Tri des fréquences
    frequency_list.sort()

    # Vérifie si la distribution des fréquences correspond à celle attendue [1,1,2,2]
    if frequency_list == [1, 1, 2, 2]:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()