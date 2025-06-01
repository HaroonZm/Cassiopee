import math


largeur_image, hauteur_image, cout_par_unite = map(int, input().split())

plus_grand_commun_diviseur = math.gcd(largeur_image, hauteur_image)

largeur_reduite = largeur_image // plus_grand_commun_diviseur
hauteur_reduite = hauteur_image // plus_grand_commun_diviseur

cout_total = largeur_reduite * hauteur_reduite * cout_par_unite

print(cout_total)