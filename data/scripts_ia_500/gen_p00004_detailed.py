import sys

# Cette fonction résout un système de deux équations linéaires à deux inconnues:
# ax + by = c
# dx + ey = f
# Elle utilise la méthode de Cramer pour trouver x et y.
def solve_simultaneous_equation(a, b, c, d, e, f):
    # Calcul du déterminant principal
    determinant = a * e - b * d
    
    # Comme l'énoncé garantit une solution unique, determinant ne sera jamais nul
    # Calcul des déterminants pour x et y en appliquant la règle de Cramer
    determinant_x = c * e - b * f
    determinant_y = a * f - c * d
    
    # Calcul des valeurs de x et y
    x = determinant_x / determinant
    y = determinant_y / determinant
    
    return x, y

# Lecture de l'entrée ligne par ligne jusqu'à EOF
for line in sys.stdin:
    # Supprimer les espaces superflus et séparer les valeurs
    parts = line.strip().split()
    if len(parts) != 6:
        # Si la ligne ne contient pas 6 éléments, on ignore (sécurité)
        continue
    
    # Conversion des chaînes en entiers
    a, b, c, d, e, f = map(int, parts)
    
    # Résolution du système
    x, y = solve_simultaneous_equation(a, b, c, d, e, f)
    
    # Affichage des résultats arrondis à 3 décimales
    print(f"{x:.3f} {y:.3f}")