n = int(input())
for _ in range(n):
    x1, y1, x2, y2, x3, y3 = map(float, input().split())
    # Calculer les décalages
    A = x2 - x1
    B = y2 - y1
    C = x3 - x1
    D = y3 - y1

    # Calcul des coefficients pour résoudre le centre
    E = A*(x1 + x2) + B*(y1 + y2)
    F = C*(x1 + x3) + D*(y1 + y3)
    G = 2*(A*(y3 - y2) - B*(x3 - x2))

    if G == 0:
        # Les points sont colinéaires, cercle circonscrit indéfini
        # Afficher un résultat indéfini ou 0
        print("0.000 0.000 0.000")
    else:
        px = (D*E - B*F) / G
        py = (A*F - C*E) / G
        r = ((x1 - px)**2 + (y1 - py)**2)**0.5

        print(f"{px:.3f} {py:.3f} {r:.3f}")