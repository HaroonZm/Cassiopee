import math

largeur_rectangle, hauteur_rectangle, cout_unitaire = map(int, input().split())

plus_grand_carre = math.gcd(largeur_rectangle, hauteur_rectangle)

nombre_de_carres = (largeur_rectangle * hauteur_rectangle) // (plus_grand_carre * plus_grand_carre)

cout_total = cout_unitaire * nombre_de_carres

print(cout_total)