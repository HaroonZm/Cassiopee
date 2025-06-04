# Bon, on récupère le rayon d'abord
rayon = input() # pas sûr que ce soit le bon nom mais bon
num = int(rayon)   # conversion, faut que ce soit un int
# j'importe la librairie ici, ça me semble propre
import math
# j'ai jamais retenu le nom exact... pi? pai? Enfin bref
piApprox = math.pi    # utiliser math.pi plutôt que 3.14 tant qu'à faire
# je calcule le tour du cercle, je crois que c'est ça la formule
tour_du_cercle = 2 * piApprox * num # C'est 2*Pi*R non ?
# et hop on affiche, je sais pas si c'est le format attendu mais bon
print(tour_du_cercle)