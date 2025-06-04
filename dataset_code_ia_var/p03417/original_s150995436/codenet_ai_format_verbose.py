nombre_de_lignes, nombre_de_colonnes = list(map(int, input().split()))

produit_lignes_colonnes = nombre_de_lignes * nombre_de_colonnes

perimetre_rectangle_reduit = 2 * (nombre_de_lignes + nombre_de_colonnes) - 4

difference_absolue = abs(produit_lignes_colonnes - perimetre_rectangle_reduit)

print(difference_absolue)