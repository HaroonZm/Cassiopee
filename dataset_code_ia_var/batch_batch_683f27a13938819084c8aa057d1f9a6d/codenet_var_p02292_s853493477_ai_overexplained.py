import math  # Importe le module math pour les fonctions mathématiques, par exemple sqrt pour la racine carrée

eps = 10 ** -8  # Définit une très petite valeur epsilon pour comparer les nombres à virgule flottante

# Lit une ligne depuis l'entrée utilisateur (souvent du texte tapé par l'utilisateur ou passé en entrée standard)
line = input()  # Par exemple "0 0 2 2"

# Divise la ligne en morceaux quand il y a des espaces et convertit chaque morceau en entier
x1, y1, x2, y2 = list(map(int, line.split()))
# Après cette ligne, x1, y1 sont les coordonnées du premier point du segment
# x2, y2 sont les coordonnées du second point du segment

# Lit une autre ligne de l'entrée utilisateur, en général pour stocker d'autres informations
line = input()
q = int(line)  # Convertit la ligne en entier, pour savoir combien de points suivent

pts = []  # Initialise une liste vide qui contiendra tous les points à traiter

# Boucle qui va de 0 à q-1
for _ in range(0, q):
    line = input()  # Lit la position du prochain point
    x, y = list(map(int, line.split()))  # Découpe la ligne et convertit chaque morceau en entier
    pts += [[x, y]]  # Ajoute le point (x, y) comme une liste à la liste des points

# Déclaration d’une fonction nommée solve, sans arguments
def solve():
    # Calcule la longueur du segment entre (x1, y1) et (x2, y2) en utilisant la formule de distance euclidienne
    l1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    # Parcours chaque point dans la liste pts pour effectuer les calculs nécessaires
    for x, y in pts:

        # Calcule la distance entre le premier point du segment (x1, y1) et le point (x, y)
        l2 = math.sqrt((x - x1)**2 + (y - y1)**2)

        # Calcule la différence normalisée des coordonnées en x et en y pour le segment (direction)
        dx = (x2 - x1) / l1  # Valeur entre -1 et 1 représentant le déplacement horizontal unitaire
        dy = (y2 - y1) / l1  # Valeur entre -1 et 1 représentant le déplacement vertical unitaire

        # Calcule le produit scalaire entre les vecteurs (x2-x1, y2-y1) et (x-x1, y-y1)
        # Ce produit donne une information sur l’alignement et la direction relative des deux vecteurs
        ip = (x - x1) * (x2 - x1) + (y - y1) * (y2 - y1)

        # Calcule le produit vectoriel (en 2D), ici le déterminant des deux vecteurs
        # Permet de savoir si le point (x, y) est à gauche ou à droite du segment
        sine = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)

        # Si le produit vectoriel est négatif, le point est du côté gauche du segment (en fonction de l’orientation)
        if sine < 0.0:
            print("COUNTER_CLOCKWISE")  # Affiche que le point est dans le sens trigonométrique par rapport au segment

        # Si le produit vectoriel est positif, le point est du côté droit
        elif sine > 0.0:
            print("CLOCKWISE")  # Affiche que le point est dans le sens horaire

        # Si le produit vectoriel est nul (ou presque, selon epsilon), le point est sur la même droite que le segment (colinéaire)
        elif abs(ip - l1 * l2) < eps:
            # Si la distance l2 est supérieure à la longueur du segment, le point est "devant" (dans le prolongement du segment)
            if l1 < l2:
                print("ONLINE_FRONT")  # Le point est sur la droite du segment, en avant de x2, y2
            else:
                print("ON_SEGMENT")  # Le point est strictement sur le segment entre x1,y1 et x2,y2

        # Sinon, si le produit scalaire plus l1*l2 est petit (le point est aligné mais dans l’autre direction)
        elif ip + l1 * l2 < eps:
            print("ONLINE_BACK")  # Le point est sur la droite, mais derrière x1, y1 (prolongement "arrière" du segment)

# Appelle la fonction solve pour lancer le traitement et afficher les résultats
solve()