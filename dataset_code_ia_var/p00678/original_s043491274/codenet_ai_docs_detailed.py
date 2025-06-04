from math import sqrt

def dist(x1, y1, x2, y2):
    """
    Calcule la distance euclidienne entre deux points (x1, y1) et (x2, y2).
    
    Args:
        x1 (float): Abscisse du premier point.
        y1 (float): Ordonnée du premier point.
        x2 (float): Abscisse du second point.
        y2 (float): Ordonnée du second point.
        
    Returns:
        float: Distance euclidienne entre les deux points.
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def find_min_time(x, y, v):
    """
    Trouve le point du plan (px, py) qui minimise le temps maximum nécessaire 
    pour rejoindre (px, py) depuis chacun des n points (x[i], y[i]) 
    selon leurs vitesses respectives v[i], par une méthode d'optimisation.
    
    Args:
        x (list of int): Liste des abscisses des points de départ.
        y (list of int): Liste des ordonnées des points de départ.
        v (list of int): Liste des vitesses associées à chaque point.
    
    Returns:
        float: Le temps minimal maximal pour rejoindre le point optimal (px, py).
    """
    n = len(x)
    # Initialisation du point de recherche au centre (0, 0)
    px = 0.0
    py = 0.0
    # Largeur initiale de la recherche : grand pas
    d  = 1000.0

    ans = float('inf')
    # On réduit progressivement la largeur d'exploration jusqu'à la précision souhaitée
    while d > 0.1 ** 8:
        # Pour stocker le (temps maximal actuel constaté, index du point responsable)
        mx = (0, 0)
        for i in range(n):
            # Calcule le temps pour atteindre (px, py) depuis chaque point à sa vitesse
            time_i = dist(px, py, x[i], y[i]) / v[i]
            # On garde le maximum de ces temps, et l'index associé
            mx = max(mx, (time_i, i))
        # Le temps maximal actuel (pour le px,py courant)
        ans = mx[0]
        far_i = mx[1]
        # On déplace (px, py) dans la direction du point responsable du temps max
        px += d / ans * (x[far_i] - px)
        py += d / ans * (y[far_i] - py)
        # On réduit le pas d'exploration
        d /= 1.01
    return ans

def main():
    """
    Programme principal lisant les entrées et affichant le temps minimal maximal calculé.
    Procède en boucle jusqu'à ce que l'utilisateur saisisse 0.
    """
    while True:
        # Lit le nombre de points
        n = int(raw_input())
        # Si n vaut 0, on termine le programme
        if n == 0:
            break
        # Préparation des listes pour stocker les coordonnées et vitesses
        x = [0 for i in range(n)]
        y = [0 for i in range(n)]
        v = [0 for i in range(n)]
        # Lecture des coordonnées et vitesses de chaque point
        for i in range(n):
            xi, yi, vi = map(int, raw_input().split())
            x[i] = xi
            y[i] = yi
            v[i] = vi
        # Calcul du temps minimal maximal
        ans = find_min_time(x, y, v)
        # Affichage du résultat avec 8 chiffres après la virgule
        print "%.8f" % ans

# Lancement du programme principal
main()