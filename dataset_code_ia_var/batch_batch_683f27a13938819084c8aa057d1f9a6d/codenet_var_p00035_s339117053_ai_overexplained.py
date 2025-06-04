import collections  # Importe le module collections pour utiliser namedtuple, une fonction permettant de créer des tuples nommés

# Définition d'un type nommé "Point" qui représente un point dans un espace à deux dimensions (plan)
# Il possède deux attributs : x et y
Point = collections.namedtuple("Point", "x y")  

# Définition d'un type nommé "Line" qui représente une ligne définie par deux points
# Il possède deux attributs : first et second, qui stockent chacun un Point
Line = collections.namedtuple("Line", "first second")  

def cross(line1, line2):
    """
    Fonction qui teste si deux lignes (segments) se croisent.
    Prend en entrée deux objets de type 'Line' et retourne True s'ils se croisent, sinon False.
    """

    def get_s(a, b, c):
        # Fonction interne qui calcule le déterminant (ou produit vectoriel) de deux vecteurs :
        # Calculé à partir des points a, b et c.
        # Cela sert à déterminer la position relative du point c par rapport à la ligne (a,b).
        # L'expression (x1 * y2) - (x2 * y1) donne le signe de l'aire du parallélogramme formé par les vecteurs.
        x1 = a.x - c.x  # Calcule la projection x du vecteur ac (du point c vers a)
        x2 = b.x - c.x  # Calcule la projection x du vecteur bc (du point c vers b)
        y1 = a.y - c.y  # Calcule la projection y du vecteur ac
        y2 = b.y - c.y  # Calcule la projection y du vecteur bc
        return (x1 * y2) - (x2 * y1)  # Calcule le déterminant (produit vectoriel) des deux vecteurs

    # On calcule get_s pour line1 et les deux points de line2
    s1 = get_s(line1.first, line1.second, line2.first)  # Signe du point line2.first par rapport à line1
    s2 = get_s(line1.first, line1.second, line2.second)  # Signe du point line2.second par rapport à line1

    # Vérifie si les deux points de line2 sont du même côté de line1
    # Le XOR (^) renvoie True si les signes sont opposés, donc s'ils ne sont pas du même côté
    if not (s1 > 0) ^ (s2 > 0):
        return False  # S'ils sont du même côté, les segments ne se croisent pas

    # On procède de même en inversant les rôles des lignes pour l'autre orientation
    s3 = get_s(line2.first, line2.second, line1.first)
    s4 = get_s(line2.first, line2.second, line1.second)

    # Vérifie que line1 n'a pas ses deux extrémités du même côté de line2
    if not (s3 > 0) ^ (s4 > 0):
        return False  # S'ils sont du même côté, les segments ne se croisent pas

    return True  # Si les conditions sont remplies, les segments se croisent


if __name__ == '__main__':  # Point d'entrée principal du programme, ce code ne s'exécutera que si le fichier est exécuté directement
    while 1:  # Boucle infinie, on continuera tant que l'utilisateur fournit des entrées valides
        try:
            # Demande à l'utilisateur d'entrer 8 valeurs représentant les coordonnées de 4 points
            # Utilise raw_input() pour saisir la chaîne de caractères et split(',') pour séparer selon la virgule
            xa, ya, xb, yb, xc, yc, xd, yd = map(float, raw_input().split(','))
            
            # Crée quatre points à partir des coordonnées saisies
            A = Point(xa, ya)  # Premier point
            B = Point(xb, yb)  # Deuxième point
            C = Point(xc, yc)  # Troisième point
            D = Point(xd, yd)  # Quatrième point
            
            points = [A, B, C, D]  # Place tous les points dans une liste pour un accès plus facile
            
            f = False  # Initialise un indicateur à False, il servira à signaler si la condition d'échec est atteinte

            # Première boucle pour vérification de configuration croisée des diagonales
            for i in xrange(4):  # On itère 4 fois, i variant de 0 à 3 inclut
                # Selectionne deux lignes qui sont des diagonales du quadrilatère
                # (i+0)%4 et (i+2)%4 forment la première diagonale
                # (i+1)%4 et (i+3)%4 forment la seconde diagonale
                line1 = Line(points[(i + 0) % 4], points[(i + 2) % 4])
                line2 = Line(points[(i + 1) % 4], points[(i + 3) % 4])
                
                # Vérifie si ces deux lignes ne se croisent pas
                if not cross(line1, line2):
                    f = True  # Met à jour l'indicateur pour signaler l'échec

            # Seconde boucle pour vérification des arêtes successives
            for i in xrange(4):  # Encore, 4 itérations pour chaque côté
                # Prend une arête du quadrilatère et l'arête opposée
                line1 = Line(points[i], points[(i + 1) % 4])
                line2 = Line(points[(i + 2) % 4], points[(i + 3) % 4])

                # Vérifie si ces arêtes se croisent (ce qui ne doit pas arriver dans un quadrilatère simple)
                if cross(line1, line2):
                    f = True  # Met l'indicateur à True

            # Affiche le résultat : si une des conditions d'échec a été rencontrée, affiche "NO", sinon "YES"
            if f:
                print "NO"
            else:
                print "YES"
        except EOFError:
            break  # Quitte la boucle et termine le programme si aucune donnée n'est plus disponible en entrée