# Définition de la classe Wall qui représente un mur de forme circulaire
class Wall():

    # Méthode spéciale d'initialisation appelée lors de la création d'une instance de Wall
    # x : abscisse du centre du mur
    # y : ordonnée du centre du mur
    # r : rayon du mur
    def __init__(self, x, y, r):
        # Enregistre l'abscisse du centre du mur dans l'attribut d'instance self.x
        self.x = x
        # Enregistre l'ordonnée du centre du mur
        self.y = y
        # Enregistre le rayon du mur
        self.r = r

    # Méthode pour déterminer si le point (x, y) est à l'intérieur ou à l'extérieur du cercle
    # Prend en compte le centre du cercle (self.x, self.y) et son rayon self.r
    def sign(self, x, y):
        # Calcule la distance au carré entre le point (x, y) et le centre du cercle (self.x, self.y)
        # (x - self.x)^2 + (y - self.y)^2 produit la distance au carré
        # self.r*self.r est le rayon au carré
        # Si la distance au carré est strictement supérieure au rayon au carré, le point est à l'extérieur du cercle
        if (x-self.x)*(x-self.x) + (y-self.y)*(y-self.y) - self.r*self.r > 0:
            # Retourne 1 si le point est à l'extérieur du mur/cercle
            return 1
        else:
            # Retourne -1 si le point est à l'intérieur ou sur le cercle
            return -1

# Fonction pour déterminer si le segment (x1, y1)-(x2, y2) est "visible", c'est-à-dire non bloqué par un mur "wall"
def isVisible(x1, y1, x2, y2, wall):

    # Vérifie si les deux points sont tous les deux à l'extérieur du mur
    if wall.sign(x1, y1) == 1 and wall.sign(x2, y2) == 1:

        # Récupère les coordonnées du centre et le rayon du mur/cercle
        x0 = wall.x
        y0 = wall.y
        r0 = wall.r

        # Calcul des coefficients la, lb, lc de l'équation de la droite passant par (x1, y1) et (x2, y2)
        # Equation générale d'une droite : la*x + lb*y + lc = 0
        # la est la différence des ordonnées (y2 - y1)
        la = y2 - y1
        # lb est l'opposé de la différence des abscisses (-(x2 - x1))
        lb = -(x2 - x1)
        # lc est défini de sorte que la droite passe par (x1, y1) : -x1*(y2-y1) + y1*(x2-x1)
        lc = -x1 * (y2 - y1) + y1 * (x2 - x1)

        # Calcul des coefficients ma, mb, mc pour la droite passant aussi par (x1, y1)-(x2, y2), 
        # mais utilisée pour calculer le produit scalaire afin de vérifier l'intersection
        ma = x2 - x1
        mb = y2 - y1
        # mc associé au centre du cercle
        mc = -(x2 - x1) * x0 - (y2 - y1) * y0

        # Condition géométrique pour savoir si la droite coupe le cercle au moins en un point
        # (la*x0 + lb*y0 + lc)^2 <= r0^2 * (la^2 + lb^2)
        # Cette inégalité vérifie si la distance du centre du cercle à la droite est inférieure ou égale au rayon,
        # donc s'il y a potentiellement intersection
        if (la*x0 + lb*y0 + lc)*(la*x0 + lb*y0 + lc) <= r0*r0*(la*la + lb*lb):
            # Vérifie si les points (x1, y1) et (x2, y2) sont de part et d'autre de la droite passant par le centre
            # Si le produit (ma*x1 + mb*y1 + mc) * (ma*x2 + mb*y2 + mc) < 0, alors ils sont de part et d'autre de la droite,
            # donc le segment traverse le cercle
            if (ma*x1 + mb*y1 + mc) * (ma*x2 + mb*y2 + mc) < 0:
                # Il y a un croisement : visibilité bloquée
                return False
            else:
                # Sinon, ils sont du même côté ou sur la droite : pas d'intersection du segment avec le mur
                return True
        else:
            # La droite ne coupe pas le cercle : le segment n'est pas bloqué par le mur
            return True

    # Si les deux points sont tous les deux à l'intérieur du cercle, la visibilité n'est pas bloquée par le mur
    elif wall.sign(x1, y1) == -1 and wall.sign(x2, y2) == -1:
        return True
    else:
        # Sinon, le segment est bloqué par le mur
        return False

# Boucle principale du programme : s'exécute jusqu'à ce que l'utilisateur décide d'arrêter (saisie de 0)
while True:
    # Read the number of walls for current test (n)
    n = int(input())
    # Si l'utilisateur saisit 0, on quitte la boucle et donc le programme
    if n == 0:
        break

    # Initialise une liste vide pour stocker tous les murs de ce test
    walls = []
    # Pour chaque mur spécifié par l'utilisateur (n fois)
    for l in range(n):
        # Lit trois entiers séparés par des espaces représentant x, y, r pour chaque mur
        x, y, r = [int(i) for i in input().split()]
        # Crée une instance de Wall (le mur circulaire) et l'ajoute à la liste "walls"
        walls.append(Wall(x, y, r))

    # Lit le nombre de cas à traiter pour ce set de murs (nombre d'essais/test de visibilité)
    m = int(input())
    # Pour chaque essai
    for l in range(m):
        # Lit les coordonnées de la cible (tx, ty) et du tireur/source (sx, sy)
        tx, ty, sx, sy = [int(i) for i in input().split()]
        # Initialise la réponse par défaut à "Danger", ce qui signifie que par défaut il n'y a pas de mur bloquant
        ans = "Danger"
        # Pour chaque mur, on vérifie la visibilité
        for k in range(len(walls)):
            # Si la visibilité est bloquée par ce mur (isVisible retourne False)
            if isVisible(tx, ty, sx, sy, walls[k]) == False:
                # On considère que la visibilité est "Safe" (sûre/protégée)
                ans = "Safe"
                # On peut arrêter la recherche dès qu'au moins un mur bloque la visibilité
                break
        # Affiche la réponse pour cet essai
        print(ans)