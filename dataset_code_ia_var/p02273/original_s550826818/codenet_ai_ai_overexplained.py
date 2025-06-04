import math  # Importe le module mathématique standard de Python pour accéder à des fonctions comme cosinus et sinus

# Calcule la valeur en radians correspondant à 60 degrés, car les fonctions trigonométriques de Python utilisent les radians
rad = math.radians(60)  # math.radians convertit des degrés en radians

# Définition d'une classe nommée 'coordinates' pour représenter les points avec des coordonnées x, y dans un plan
class coordinates:
    # Méthode spéciale d'initialisation de la classe, appelée automatiquement lors de la création d'une instance (objet)
    def __init__(self, x, y):
        # Attribue la valeur du paramètre x à l'attribut x de l'instance créée
        self.x = x
        # Attribue la valeur du paramètre y à l'attribut y de l'instance créée
        self.y = y

# Définition d'une fonction nommée koch qui dessine récursivement une courbe de Koch
# n: niveau de récursion ou profondeur
# a: point de départ (instance de coordinates)
# b: point d'arrivée (instance de coordinates)
def koch(n, a, b):
    # Condition d'arrêt de la récursion
    if n == 0:
        # Quand le niveau de récursion atteint zéro, on sort sans rien faire
        return
    # Calcul du point s : situé à 1/3 de la distance entre a et b en utilisant l'interpolation linéaire
    s = coordinates((2.0 * a.x + b.x) / 3.0, (2.0 * a.y + b.y) / 3.0)
    # Calcul du point t : situé à 2/3 de la distance entre a et b
    t = coordinates((a.x + 2.0 * b.x) / 3.0, (a.y + 2.0 * b.y) / 3.0)
    # Calcul de vecteur t-s (dx,dy)
    dx = t.x - s.x  # Différence en x entre t et s
    dy = t.y - s.y  # Différence en y entre t et s
    # Effectue une rotation de 60 degrés sur le segment [s, t] pour calculer le sommet 'u' du "triangle équilatéral"
    ux = dx * math.cos(rad) - dy * math.sin(rad) + s.x  # Formule de rotation 2D pour x
    uy = dx * math.sin(rad) + dy * math.cos(rad) + s.y  # Formule de rotation 2D pour y
    # Crée le point u avec les nouvelles coordonnées calculées
    u = coordinates(ux, uy)
    
    # Appelle récursivement la fonction pour dessiner le segment entre a et s
    koch(n - 1, a, s)
    # Affiche les coordonnées du point s (séparées par une espace)
    print s.x, s.y
    # Appelle récursivement la fonction pour dessiner le segment entre s et u
    koch(n - 1, s, u)
    # Affiche les coordonnées du point u
    print u.x, u.y
    # Appelle récursivement la fonction pour dessiner le segment entre u et t
    koch(n - 1, u, t)
    # Affiche les coordonnées du point t
    print t.x, t.y
    # Appelle récursivement la fonction pour dessiner le segment entre t et b
    koch(n - 1, t, b)

# Demande à l'utilisateur d'entrer un entier, lequel détermine le niveau de récursion du flocon de Koch
# input() lit une entrée depuis le clavier (dans Python 2, il faut utiliser raw_input pour un string)
n = input()

# Crée un point de départ p1 à l'origine (0, 0) en utilisant la classe coordinates
p1 = coordinates(0.0, 0.0)
# Crée un point d'arrivée p2 à la coordonnée (100, 0), c'est-à-dire 100 unités à droite de l'origine
p2 = coordinates(100.0, 0.0)

# Affiche les coordonnées x et y du point de départ, séparées par un espace
print p1.x, p1.y
# Appelle la fonction koch pour dessiner la courbe de Koch à partir de p1 jusqu'à p2 au niveau de récursion n
koch(n, p1, p2)
# Affiche les coordonnées x et y du point d'arrivée, cela termine la courbe à la position finale
print p2.x, p2.y