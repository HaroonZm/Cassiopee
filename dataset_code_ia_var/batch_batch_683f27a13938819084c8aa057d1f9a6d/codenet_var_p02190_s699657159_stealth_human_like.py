n = int(input()) # nombre d'éléments, je suppose
a = input().split()
a = [int(x) for x in a]  # conversion en entiers, classique

# On veut les valeurs distinctes je crois
resultat = len(set(a))

print(resultat) # ça affiche bien le décompte

# (j'aurais pu trier, mais pas sûr que ça serve)