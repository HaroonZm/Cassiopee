class Vector:
    """
    Représente un vecteur en 2 dimensions, utilisé pour manipuler des positions dans la grille.
    """

    def __init__(self, x, y):
        """
        Initialise un vecteur avec des coordonnées (x, y).
        
        Args:
            x (int): La coordonnée horizontale.
            y (int): La coordonnée verticale.
        """
        self.x = x
        self.y = y

    def move(self, offset):
        """
        Déplace le vecteur selon le décalage spécifié.

        Args:
            offset (list ou tuple): Un décalage de la forme [dx, dy] à appliquer à ce vecteur.
        """
        self.x += offset[0]
        self.y += offset[1]

    def move_offset(self, offset, multiple=1):
        """
        Calcule un nouveau vecteur selon un décalage et un facteur multiplicateur sans modifier l'original.

        Args:
            offset (list ou tuple): Déplacement [dx, dy].
            multiple (int, optionnel): Facteur multiplicateur appliqué au décalage (par défaut 1).

        Returns:
            Vector: Un nouveau vecteur résultant du déplacement.
        """
        x = self.x + offset[0] * multiple
        y = self.y + offset[1] * multiple
        return Vector(x, y)


# Constantes définissant les caractères pour l'affichage de la grille
NOTHING = " "
EXIST = "#"
SENTINEL = "?"

# Définitions des directions pour le mouvement en spirale (sens horaire)
# Chaque direction possède : à gauche, en face, à droite
MOVE = [
    [[-1, -1], [-1, +0], [-1, +1]],   # Vers le haut
    [[-1, +1], [-0, +1], [+1, +1]],   # Vers la droite
    [[+1, +1], [+1, +0], [+1, -1]],   # Vers le bas
    [[+1, -1], [+0, -1], [-1, -1]],   # Vers la gauche
]


def create_area(size):
    """
    Crée une grille (aire) de taille spécifiée, avec des bordures sentinelles.

    Args:
        size (int): Taille interne de la grille (hors sentinelles).

    Returns:
        list: Grille 2D, chaque case étant un caractère SENTINEL, NOTHING, etc.
    """
    # Création des lignes internes avec deux sentinelles de chaque côté
    area = [[SENTINEL] * 2 + [NOTHING] * size + [SENTINEL] * 2 for _ in range(size)]
    # Création de lignes sentinelles complètes
    tmp = [[SENTINEL] * (size + 4)]
    # Encadrement de l'aire avec deux lignes sentinelles en haut et en bas
    area = tmp * 2 + area + tmp * 2
    return area


def even_spiral_pattern(area, point):
    """
    Remplit la grille en dessinant une spirale pour une taille paire.

    Args:
        area (list): La grille à remplir.
        point (Vector): Point de départ (doit être une instance de Vector).

    Returns:
        list: La grille après le passage de la spirale.
    """
    move_index = 0  # Commence par la direction "haut"
    area[point.x][point.y] = EXIST  # Marque le point initial comme rempli

    while True:
        # On prend les vecteurs de déplacement pour la direction actuelle
        left, center, right = MOVE[move_index]
        # On calcule les positions d'extrémité à gauche et à droite
        end1, end2 = point.move_offset(left), point.move_offset(right)
        # On calcule la position devant et deux cases devant
        offset, offset2 = point.move_offset(center), point.move_offset(center, 2)

        # Si une des extrémités est déjà occupée, on termine la génération
        if area[end1.x][end1.y] == EXIST or area[end2.x][end2.y] == EXIST:
            return area
        # Si devant c'est vide et que deux devant n'est pas occupé, on avance
        elif area[offset.x][offset.y] == NOTHING and area[offset2.x][offset2.y] != EXIST:
            point.move(center)
            area[point.x][point.y] = EXIST
        # Sinon, on change de direction (sens horaire)
        else:
            move_index += 1
            move_index %= 4


def odd_spiral_pattern(area, point):
    """
    Remplit la grille en dessinant une spirale pour une taille impaire.

    Args:
        area (list): La grille à remplir.
        point (Vector): Point de départ (doit être une instance de Vector).

    Returns:
        list: La grille après le passage de la spirale.
    """
    move_index = 0  # Direction initiale "haut"
    is_end = False  # Pour savoir si on a fait un tour complet sans avancer
    area[point.x][point.y] = EXIST  # Marque le point initial

    while True:
        # Prend les directions pour la rotation courante
        left, center, right = MOVE[move_index]
        # On ne regarde ici que le pas devant et deux pas devant
        offset, offset2 = point.move_offset(center), point.move_offset(center, 2)

        # Si on peut avancer
        if area[offset.x][offset.y] == NOTHING and area[offset2.x][offset2.y] != EXIST:
            point.move(center)
            area[point.x][point.y] = EXIST
            is_end = False  # On a avancé, on remet à False
        # Sinon, si déjà impossible d'avancer, on termine
        else:
            if is_end:
                return area
            else:
                is_end = True  # Premier blocage, il faut encore tourner

            # On tourne d'un quart de tour (sens horaire)
            move_index += 1
            move_index %= 4


def formater(area):
    """
    Formate la grille pour l'affichage : enlève les sentinelles et assemble chaque ligne.

    Args:
        area (list): Grille 2D à formatter.

    Returns:
        str: Chaîne de caractères prêtes à être affichée pour la grille.
    """
    # Ne prend que les lignes internes (hors bordures sentinelles)
    output = ["".join(item).replace(SENTINEL, "") for item in area[2:-2]]
    output = "\n".join(output)
    return output


# Liste pour stocker tous les résultats produisant une sortie finale groupée
output = []

# Boucle principale : traite chaque cas de test
for _ in range(int(input())):
    size = int(input())  # Lecture de la taille de la grille demandée

    area = create_area(size)                        # Initialise la grille avec sentinelles
    point = Vector(size - 1 + 2, 2)                # Point de départ en bas à gauche (hors sentinelles)

    # Choisit la méthode selon la parité de la taille
    if size % 2 == 0:
        result = even_spiral_pattern(area, point)
    else:
        result = odd_spiral_pattern(area, point)

    # Formate et ajoute le résultat dans la liste de sorties
    output.append(formater(result))

# Affiche tous les résultats, séparés par deux sauts de ligne
print("\n\n".join(output))