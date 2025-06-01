import sys

# On utilise la méthode de résolution de système linéaire:
# Pour les équations:
# a*x + b*y = c
# d*x + e*y = f
# La solution unique (x, y) peut être trouvée par la formule de Cramer:
# determinant = a*e - b*d
# x = (c*e - b*f) / determinant
# y = (a*f - c*d) / determinant

for line in sys.stdin:
    # On enlève les espaces superflus et on vérifie la ligne vide
    line = line.strip()
    if not line:
        continue
    
    # On récupère les coefficients a, b, c, d, e, f
    a, b, c, d, e, f = map(int, line.split())
    
    # Calcul du déterminant
    determinant = a*e - b*d
    
    # Comme le problème garantit une solution unique, determinant != 0
    x = (c*e - b*f) / determinant
    y = (a*f - c*d) / determinant
    
    # Impression arrondie à 3 décimales
    print(f"{x:.3f} {y:.3f}")