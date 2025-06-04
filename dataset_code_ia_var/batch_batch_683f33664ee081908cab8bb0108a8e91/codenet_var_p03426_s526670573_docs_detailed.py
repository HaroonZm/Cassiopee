def parse_input_dimensions():
    """
    Lit les dimensions h (hauteur), w (largeur), et d (pas de déplacement) depuis l'entrée standard.
    Retourne un tuple (h, w, d).
    """
    h, w, d = map(int, input().split())
    return h, w, d

def build_field_mapping(h, w):
    """
    Construit une liste qui associe chaque valeur de case (1 à h*w) à ses coordonnées (i, j) dans le champ.
    field[valeur-1] = [ligne, colonne] pour chaque valeur.
    Retourne la liste field.
    """
    # Initialisation de la liste de champs vides pour chaque case
    field = [None] * (h * w)
    # Parcours de chaque ligne de la grille
    for i in range(h):
        # Lecture et conversion des valeurs de la ligne courante en liste d'entiers
        x = list(map(int, input().split()))
        # Association de chaque valeur à ses coordonnées (i, j)
        for j in range(w):
            # Les valeurs dans la grille vont de 1 à h*w ; on utilise valeur - 1 comme index
            field[x[j] - 1] = [i, j]
    return field

def compute_distance_array(field, h, w, d):
    """
    Pour chaque indice de case (0 à h*w-1), pré-calcule la somme accumulée des 'coûts' de déplacement
    pour aller d'une case à la suivante selon l'incrément 'd'.
    Retourne la liste des coûts cumulés 'dis'.
    """
    # Initialisation de la liste de distance avec une grande valeur
    dis = [10 ** 20] * (h * w)
    # Les d premiers indices ont un coût de 0 (point de départ de chaque famille modulo d)
    for i in range(d):
        dis[i] = 0
    # Calcul pour chaque position en utilisant la récurrence basée sur un pas d
    for i in range(h * w):
        if i >= d:
            # Coût depuis la dernière case atteignable en sautant de d
            dis[i] = dis[i - d] + abs(field[i][0] - field[i - d][0]) + abs(field[i][1] - field[i - d][1])
    return dis

def answer_queries(dis):
    """
    Pour chaque requête, lit les indices l et r, puis affiche la différence de coûts cumulés entre la case r et l.
    """
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        # Affichage du coût pour aller de l à r (indices convertis en base 0)
        print(dis[r - 1] - dis[l - 1])

def main():
    """
    Programme principal qui gère toutes les étapes : lecture des dimensions, construction du champ,
    pré-calcul des distances, puis gestion des requêtes.
    """
    # Lecture des dimensions et du pas d
    h, w, d = parse_input_dimensions()
    # Construction de la correspondance valeur -> coordonnées du champ
    field = build_field_mapping(h, w)
    # Pré-calcul des coûts cumulés pour chaque case
    dis = compute_distance_array(field, h, w, d)
    # Réponse aux différentes requêtes
    answer_queries(dis)

if __name__ == '__main__':
    main()