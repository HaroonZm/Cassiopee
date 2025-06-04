import cmath

EPS = 1e-6  # Petite valeur pour la tolérance des comparaisons de nombres flottants

def read_circle():
    """
    Lit une ligne d'entrée standard composée de trois entiers séparés par des espaces,
    représentant les coordonnées x, y du centre du cercle et son rayon r.
    
    Retourne :
        tuple: (centre_complexe, rayon) où centre_complexe est un nombre complexe (x + yj) et rayon est un entier.
    """
    x, y, r = map(int, input().split())
    centre = complex(x, y)
    return (centre, r)

def classify_circles(c1, c2):
    """
    Détermine la relation géométrique entre deux cercles dans le plan complexe.
    
    Arguments :
        c1 (tuple): Premier cercle au format (centre_complexe, rayon)
        c2 (tuple): Second cercle au format (centre_complexe, rayon)
        
    Retourne :
        int: Un code indiquant la relation selon les règles suivantes :
            0 - Un cercle est entièrement à l'intérieur de l'autre sans tangence
            1 - Cercles tangents intérieurement
            2 - Cercles se coupent en deux points
            3 - Cercles tangents extérieurement
            4 - Cercles totalement disjoints
    """
    centre1, rayon1 = c1
    centre2, rayon2 = c2
    
    # Calcul de la distance entre centres
    dist_centres = abs(centre1 - centre2)
    
    # Somme et valeur absolue de la différence des rayons
    somme_rayons = rayon1 + rayon2
    diff_rayons = abs(rayon1 - rayon2)
    
    # Cas tangent extérieur
    if abs(dist_centres - somme_rayons) <= EPS:
        return 3
    # Cas tangent intérieur
    elif abs(diff_rayons - dist_centres) <= EPS:
        return 1
    # Cercles disjoints (non sécants)
    elif dist_centres > somme_rayons:
        return 4
    # Un cercle entièrement dans l'autre, pas tangents
    elif diff_rayons > dist_centres:
        return 0
    # Cercles sécants en deux points
    else:
        return 2

def main():
    """
    Point d'entrée principal du script.
    Lit deux cercles et affiche le code de leur relation géométrique.
    """
    # Lecture des deux cercles
    c1 = read_circle()
    c2 = read_circle()
    
    # Classification de leur relation
    result = classify_circles(c1, c2)
    
    print(result)

if __name__ == "__main__":
    main()