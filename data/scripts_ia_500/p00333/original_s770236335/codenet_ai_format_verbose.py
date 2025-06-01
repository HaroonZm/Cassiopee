import math

largeur_image, hauteur_image, cout_unitaire = map(int, input().split())

plus_grand_commun_diviseur = math.gcd(largeur_image, hauteur_image)

nombre_de_carres = (largeur_image // plus_grand_commun_diviseur) * (hauteur_image // plus_grand_commun_diviseur)

cout_total = nombre_de_carres * cout_unitaire

print(cout_total)