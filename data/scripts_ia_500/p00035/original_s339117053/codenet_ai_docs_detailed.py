import collections

# Définition d'un Point avec des coordonnées x et y
Point = collections.namedtuple("Point", "x y")

# Définition d'une Ligne avec deux points : first et second
Line = collections.namedtuple("Line", "first second")

def cross(line1, line2):
    """
    Détermine si deux segments de droite se croisent ou s'intersectent.
    
    Args:
        line1 (Line): Premier segment défini par deux points.
        line2 (Line): Deuxième segment défini par deux points.
    
    Returns:
        bool: True si les segments se croisent, False sinon.
    
    Fonctionnement:
    - La fonction interne get_s calcule l'aire orientée formée par trois points,
      utilisée pour déterminer de quel côté d'une droite se trouve un point.
    - On teste ensuite si les points d'un segment sont sur des côtés opposés
      de l'autre segment, ce qui est nécessaire pour que deux segments s'intersectent.
    """
    def get_s(a, b, c):
        """
        Calcule l'aire orientée entre trois points.
        
        Args:
            a (Point): Premier point.
            b (Point): Deuxième point.
            c (Point): Troisième point de référence.
        
        Returns:
            float: Aire orientée entre les points.
        """
        x1 = a.x - c.x
        x2 = b.x - c.x
        y1 = a.y - c.y
        y2 = b.y - c.y
        return (x1 * y2) - (x2 * y1)

    # Calcul des orientations relatives des points du deuxième segment par rapport au premier segment
    s1 = get_s(line1.first, line1.second, line2.first)
    s2 = get_s(line1.first, line1.second, line2.second)

    # Si les deux points du deuxième segment sont du même côté du premier segment, pas d'intersection
    if not (s1 > 0) ^ (s2 > 0):
        return False

    # Calcul des orientations relatives des points du premier segment par rapport au deuxième segment
    s3 = get_s(line2.first, line2.second, line1.first)
    s4 = get_s(line2.first, line2.second, line1.second)

    # Si les deux points du premier segment sont du même côté du deuxième segment, pas d'intersection
    if not (s3 > 0) ^ (s4 > 0):
        return False

    # Les segments se croisent
    return True


if __name__ == '__main__':
    # Boucle infinie de lecture d'entrée au format : xa,ya,xb,yb,xc,yc,xd,yd
    while True:
        try:
            # Lecture et conversion des huit coordonnées en float
            xa, ya, xb, yb, xc, yc, xd, yd = map(float, raw_input().split(','))
            
            # Création des points A, B, C, D à partir des coordonnées
            A = Point(xa, ya)
            B = Point(xb, yb)
            C = Point(xc, yc)
            D = Point(xd, yd)
            
            points = [A, B, C, D]

            # Flag indiquant si la configuration est invalide ou non
            f = False

            # Vérification des croisements entre les diagonales des points dans différents ordres
            for i in xrange(4):
                line1 = Line(points[(i + 0) % 4], points[(i + 2) % 4])
                line2 = Line(points[(i + 1) % 4], points[(i + 3) % 4])
                if not cross(line1, line2):
                    # Si des diagonales ne se croisent pas, marquer comme invalide
                    f = True

            # Vérification de la présence de croisements entre côtés opposés du quadrilatère
            for i in xrange(4):
                line1 = Line(points[i], points[(i + 1) % 4])
                line2 = Line(points[(i + 2) % 4], points[(i + 3) % 4])
                if cross(line1, line2):
                    # Si deux côtés opposés se croisent, marquer comme invalide
                    f = True

            # Affichage du résultat selon la validité détectée
            if f:
                print "NO"
            else:
                print "YES"
        except EOFError:
            # Fin de lecture des entrées, sortir de la boucle
            break