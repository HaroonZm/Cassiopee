from math import pi, cos, sin

def compute_segment_areas(radius, x_coord, y_coord, sector_masses):
    """
    Calcule une valeur pour chaque secteur sur un cercle divisé en arcs proportionnels à sector_masses.
    
    Chaque valeur dépend de la géométrie du secteur et de la position (x, y) par rapport au centre du cercle.
    
    Args:
        radius (int): Rayon du cercle.
        x_coord (int): Coordonnée x (abscisse) du point à analyser (par rapport au centre du cercle).
        y_coord (int): Coordonnée y (ordonnée) du point à analyser (par rapport au centre du cercle).
        sector_masses (List[int]): Liste des masses (ou poids) associées à chaque secteur (déterminant leur angle).
        
    Returns:
        List[int]: Liste de valeurs calculées pour chaque secteur (arrondies à l'entier, selon la formule donnée).
    """
    n = len(sector_masses)           # Nombre de secteurs
    x = x_coord / radius             # Normalisation de la coordonnée x (par le rayon)
    y = y_coord / radius             # Normalisation de la coordonnée y (par le rayon)
    total_mass = sum(sector_masses)  # Masse/poids total

    # Préparation des angles de début/fin (en radians) pour chaque secteur
    angles = [0.0] * (n + 1)  # angles[i] = angle du bord gauche du secteur i, angles[i+1] = bord droit
    current_angle = 0         # Angle accumulé jusqu'au secteur courant
    
    # Calcul des angles cumulés, pour chaque secteur
    for i in range(n):
        current_angle += sector_masses[i] / total_mass * 2 * pi
        angles[i + 1] = current_angle
    
    # Calcul des valeurs par secteur selon une intégrale spécifiée (formule du code source d'origine)
    results = []
    for i in range(n):
        # Calcul du numérateur de la formule d'intégrale sectorielle
        numerator = (
            (sin(angles[i]) * y - cos(angles[i]) * x) +
            (x * cos(angles[i + 1]) - y * sin(angles[i + 1]))
        )
        # Calcul du "coefficient moyen" sur le secteur (de t_i à t_{i+1})
        value = (1 + numerator / (angles[i + 1] - angles[i])) * 100
        results.append(int(value))  # Conversion en entier, résultat arrondi par troncature
    return results

def main():
    """
    Lit l'entrée de l'utilisateur, calcule et affiche les résultats pour chaque secteur.
    Entrée:
        Ligne 1: r x y n (entiers), séparés par des espaces
        Ligne 2: n entiers correspondant aux masses des secteurs
    Sortie:
        n entiers (séparés par des espaces), résultats pour chaque secteur
    """
    # Lecture de la première ligne: rayon, x, y, n
    r, _x, _y, n = map(int, input().split())
    
    # Lecture de la deuxième ligne: masses des secteurs
    sector_masses = list(map(int, input().split()))

    # Calcul des secteurs et affichage
    results = compute_segment_areas(r, _x, _y, sector_masses)
    print(*results)

if __name__ == "__main__":
    main()