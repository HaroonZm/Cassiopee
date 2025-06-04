def PointSegmentDistance(point, begin, end):
    """
    Calcule la distance minimale entre un point et un segment dans le plan complexe.

    Paramètres
    ----------
    point : complex
        Le point pour lequel on veut la distance au segment.
    begin : complex
        Le point de début du segment.
    end : complex
        Le point de fin du segment.

    Retourne
    -------
    float
        La distance minimale entre le point et le segment [begin, end].
    """

    # Décale tous les points pour que 'begin' soit l'origine.
    # Ce changement de repère facilite les calculs vectoriels.
    vector_point = point - begin      # Point dans le repère local du segment
    vector_segment = end - begin      # Vecteur segment

    # Si le segment est réduit à un point, retourne la distance point-segment
    if abs(vector_segment) == 0:
        return abs(vector_point)

    # Projection du point sur la droite du segment, exprimée dans la base du segment
    # Le réel donne la coordonnée le long du segment, l'imaginaire la distance hors-segment (perpendiculaire)
    projection = (vector_point / vector_segment) * abs(vector_segment)
    segment_length = abs(vector_segment)

    # Si la projection tombe sur le segment en question
    if 0 <= projection.real <= segment_length:
        return abs(projection.imag)   # Distance perpendiculaire
    else:
        # Sinon, retourne la distance au plus proche des deux bouts du segment
        return min(abs(vector_point), abs(vector_point - vector_segment))


def main():
    """
    Point d'entrée principal. Lit l'entrée des deux polygones, 
    puis calcule la distance minimale entre leurs arêtes.
    """

    # Lecture du premier polygone (nombre de sommets, puis sommets)
    n1 = int(input())
    a = [0]  # Commence la liste avec le point 0 (origine)
    for _ in range(n1):
        x, y = map(int, input().split())
        a.append(complex(x, y))  # Ajoute chaque point comme un nombre complexe
    a.append(1000)  # Ajoute un point d'extrémité arbitraire (1000,0) pour fermer le contour ou éviter des erreurs d'indice

    # Lecture du second polygone (nombre de sommets, puis sommets)
    n2 = int(input())
    b = [1000j]  # Commence la liste avec le point (0,1000)
    for _ in range(n2):
        x, y = map(int, input().split())
        b.append(complex(x, y))  # Même principe que précédemment
    b.append(1000+1000j)  # Ajoute un point (1000,1000) pour le même usage qu'au-dessus

    # Variable pour mémoriser la distance minimale trouvée
    ans = 10**30

    # Pour chaque point du premier polygone et chaque segment du second
    for p in range(n1+2):
        for q in range(n2+1):
            dist = PointSegmentDistance(a[p], b[q], b[q+1])
            if dist < ans:
                ans = dist

    # Pour chaque point du second polygone et chaque segment du premier
    for q in range(n2+2):
        for p in range(n1+1):
            dist = PointSegmentDistance(b[q], a[p], a[p+1])
            if dist < ans:
                ans = dist

    # Affiche la plus petite distance obtenue
    print(ans)


if __name__ == "__main__":
    main()