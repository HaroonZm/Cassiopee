n = int(input())
for _ in range(n):
    x1, y1, x2, y2, x3, y3 = map(float, input().split())
    # Calcul des coefficients pour le système linéaire
    A = x2 - x1
    B = y2 - y1
    C = x3 - x1
    D = y3 - y1
    
    E = ((x2**2 - x1**2) + (y2**2 - y1**2)) / 2.0
    F = ((x3**2 - x1**2) + (y3**2 - y1**2)) / 2.0
    
    denom = A*D - B*C
    if denom == 0:
        # Points alignés, pas de cercle circonscrit, afficher 0s
        px = 0.0
        py = 0.0
        r = 0.0
    else:
        px = (D*E - B*F) / denom
        py = (-C*E + A*F) / denom
    
        r = ((px - x1)**2 + (py - y1)**2) ** 0.5
    
    print(f"{px:.3f} {py:.3f} {r:.3f}")