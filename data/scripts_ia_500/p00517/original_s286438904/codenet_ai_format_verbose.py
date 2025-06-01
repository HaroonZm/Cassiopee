largeur_rectangle, hauteur_rectangle, nombre_points = map(int, input().split())

x_coordonnees_precedentes, y_coordonnees_precedentes = map(int, input().split())

distance_totale = 0

for _ in range(nombre_points - 1):
    
    x_coordonnees_courantes, y_coordonnees_courantes = map(int, input().split())
    
    difference_x = x_coordonnees_courantes - x_coordonnees_precedentes
    difference_y = y_coordonnees_courantes - y_coordonnees_precedentes
    
    if difference_x * difference_y < 0:
        distance_segment = abs(difference_x) + abs(difference_y)
    else:
        distance_segment = max(abs(difference_x), abs(difference_y))
    
    distance_totale += distance_segment
    
    x_coordonnees_precedentes = x_coordonnees_courantes
    y_coordonnees_precedentes = y_coordonnees_courantes

print(distance_totale)