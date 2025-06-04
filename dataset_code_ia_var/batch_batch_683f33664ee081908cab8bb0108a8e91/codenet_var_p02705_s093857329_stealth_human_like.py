import math
import sys

# Bon, on lit la valeur depuis stdin normalement
nombre = int(sys.stdin.readline()) # J'espère que c'est bien un entier !

# On a besoin de pi, donc j'importe math
perimetre = 2 * math.pi * nombre # je crois que c'est comme ça la formule du cercle

print(perimetre)
# c'est censé afficher le résultat, mais je laisse la précision par défaut