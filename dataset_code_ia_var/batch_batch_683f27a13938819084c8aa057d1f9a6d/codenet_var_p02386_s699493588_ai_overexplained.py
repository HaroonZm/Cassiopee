# Définition de la classe Dice représentant un dé à six faces
class Dice:
    # Le constructeur __init__ est appelé lors de la création d'une nouvelle instance de Dice
    # Il reçoit en paramètre p, qui est supposé être une liste de 6 éléments représentant les valeurs des faces du dé
    def __init__(self, p):
        # Initialisation de la liste y, représentant certaines faces dans l'ordre : haut(0), nord(1), bas(5), sud(4)
        self.y = [p[0], p[1], p[5], p[4]]
        # Initialisation de x, représentant les faces : haut(0), est(2), bas(5), ouest(3)
        self.x = [p[0], p[2], p[5], p[3]]
        # Initialisation de z, représentant les faces : nord(1), est(2), sud(4), ouest(3)
        self.z = [p[1], p[2], p[4], p[3]]

    # La fonction roll effectue une rotation du dé autour d'un axe donné, 'x', 'y' ou 'z'
    # c est une chaîne de caractères, doit valoir soit 'x', 'y', soit 'z'
    def roll(self, c):
        # Si la commande de roulement est autour de l'axe y
        if c == 'y':
            # La méthode pop(0) retire et retourne le premier élément de la liste y (face supérieure)
            # append ajoute cet élément à la fin de la liste (effectue ainsi une rotation dans y)
            self.y.append(self.y.pop(0))
            # Après la rotation autour de y, on ajuste les autres axes pour que les informations restent cohérentes.
            # L'élément 0 de x (face supérieure) devient le nouvel élément 0 de y
            self.x[0] = self.y[0]
            # L'élément 2 de x (face inférieure) devient le nouvel élément 2 de y
            self.x[2] = self.y[2]
            # L'élément 0 de z (nord) devient le nouvel élément 1 de y
            self.z[0] = self.y[1]
            # L'élément 2 de z (sud) devient le nouvel élément 3 de y
            self.z[2] = self.y[3]
        # Si la commande de roulement est autour de l'axe x
        elif c == 'x':
            # Rotation similaire mais sur la liste x (haut, est, bas, ouest)
            self.x.append(self.x.pop(0))
            # Après la rotation, réajuste les éléments correspondants dans y et z
            self.y[0] = self.x[0]    # Nouvelle face du haut (0)
            self.y[2] = self.x[2]    # Nouvelle face du bas (2)
            self.z[1] = self.x[1]    # Nouvelle face de l'est (1)
            self.z[3] = self.x[3]    # Nouvelle face de l'ouest (3)
        # Si la commande de roulement est autour de l'axe z
        elif c == 'z':
            # Rotation sur la liste z (nord, est, sud, ouest)
            self.z.append(self.z.pop(0))
            # Met à jour les autres axes apparentés
            self.x[1] = self.z[1]    # Nouvelle face est (1)
            self.x[3] = self.z[3]    # Nouvelle face ouest (3)
            self.y[1] = self.z[0]    # Nouvelle face nord (0)
            self.y[3] = self.z[2]    # Nouvelle face sud (2)

    # La méthode num retourne la valeur de la face numéro n (1 à 6, dans l'ordre habituel d'un dé)
    def num(self, n):
        # On convertit n en index 0-based (0 à 5) car les listes Python sont indexées depuis 0
        n = n - 1
        # Définition des positions correspondant à chaque face pour les axes y et x
        # pos_y et pos_x sont utilisés pour déterminer de quelle liste (y ou x) et quel index récupérer
        pos_y = [0, 1, 5, 4]  # faces haut, nord, bas, sud (indices dans p)
        pos_x = [0, 2, 5, 3]  # faces haut, est, bas, ouest (indices dans p)
        # Si l'index n correspond à une des positions de la liste y
        if n in pos_y:
            # Retourne la valeur de la list y à la position correspondante (cherche où dans pos_y il y a n)
            return self.y[pos_y.index(n)]
        else:
            # Sinon retourne depuis x (idem)
            return self.x[pos_x.index(n)]

    # La méthode same compare l'objet courant avec un autre dé pour voir si, par rotation,
    # ils peuvent correspondre (avoir la même configuration)
    def same(self, other):
        # Effectue une rotation quatre fois autour de l'axe x (possible positions du haut)
        for _ in range(4):
            # Si à ce stade les deux dés sont égaux (__eq__ renvoie True)
            if self == other:
                return True
            # Effectue une rotation de l'autre dé autour de x
            other.roll('x')
            # Pour chaque position du haut, fait également 4 tours autour de y (direction nord)
            for _ in range(4):
                if self == other:
                    return True
                # Tourne encore autour de y
                other.roll('y')
                # Pour chaque or, fait aussi 4 rotations autour de z (différentes orientations)
                for _ in range(4):
                    if self == other:
                        return True
                    # Tourne autour de z
                    other.roll('z')
        # Si aucune des 24 orientations n'a permis d'obtenir la même configuration, retourne False
        return False

    # Méthode spéciale d'égalité (compare deux objets Dice face par face)
    def __eq__(self, other):
        # Parcours les 6 faces (de 1 à 6)
        for i in range(1, 7):
            # Si une face est différente entre les deux dés, retourne False
            if self.num(i) != other.num(i):
                return False
        # Sinon, toutes les faces sont identiques, retourne True
        return True

# Lecture d'un entier depuis l'entrée standard, représentant le nombre de dés à tester
n = int(input())
# Création d'une liste vide pour stocker les dés
dices = []
# Boucle qui va de 0 à n-1 pour lire chaque dé
for _ in range(n):
    # Lecture d'une ligne, découpe la ligne en chaînes, conversion de chaque chaîne en entier, création d'une instance de Dice
    dices.append(Dice([int(i) for i in input().split()]))

# Vérifie si tous les dés (sauf le premier) sont différents du premier dé, peu importe leur orientation
# Utilisation de all : retourne True si tous les éléments de l'itérable sont vrais
# La liste de compréhensions 'not dices[0].same(other) for other in dices[1:]' retourne True pour chaque autre dé
yes = all([not dices[0].same(other) for other in dices[1:]])

# Affiche 'Yes' si yes est vrai (aucun autre dé n'est identique au premier), sinon 'No'
print('Yes' if yes else 'No')