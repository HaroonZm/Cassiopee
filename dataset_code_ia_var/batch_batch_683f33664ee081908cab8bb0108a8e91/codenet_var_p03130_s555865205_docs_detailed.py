def is_path_possible():
    """
    Détermine si, à partir de trois arêtes saisies entre 4 sommets (numérotés 1 à 4),
    il est possible de former un chemin linéaire reliant tous les sommets consécutivement.
    
    Saisie: Pour chaque arête, l'utilisateur entre deux entiers (a, b), représentant un lien non orienté entre les sommets a et b.
    Sortie: Affiche 'YES' si la configuration décrit un chemin de type ligne (chaque extrémité a un degré 1 et les autres un degré 2),
            sinon affiche 'NO'.
    """
    # Initialisation des degrés à 0 pour chaque sommet
    degrees = [0, 0, 0, 0]
    # Compteurs pour le nombre de sommets de degré 1 et de degré 2
    one = 0
    two = 0

    # Lecture de 3 paires d'entiers représentant les arêtes
    for _ in range(3):
        a, b = map(int, input().split())
        degrees[a - 1] += 1  # Incrémente le degré du sommet a
        degrees[b - 1] += 1  # Incrémente le degré du sommet b

    # Comptabilise le nombre de sommets ayant le degré 1 et 2
    for i in range(len(degrees)):
        if degrees[i] == 1:
            one += 1
        if degrees[i] == 2:
            two += 1

    # Condition: deux sommets de degré 1 (extrémités), deux de degré 2 (milieux)
    if one == 2 and two == 2:
        print('YES')
    else:
        print('NO')

# Exemple d'utilisation de la fonction :
if __name__ == "__main__":
    is_path_possible()