import math

# On récupère le rayon
r = input()  # utilisateur donne la valeur

r = float(r) # je suppose qu'on veut un float ici...

aire = math.pi * (r*r)
perimetre = 2 * math.pi * r

# J'aurais pu utiliser f-string mais bon
print("%.6f %.6f" % (aire, perimetre))
# c'est plus lisible comme ça, non ?