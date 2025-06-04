# Bon, on va demander le rayon
radi = float(input())
PI = 3.14159265358979   # pi plus ou moins, je crois que ça suffit...

# Calcul de l'aire et du périmètre... (j'espère que je ne me trompe pas de formule)
aire = PI * radi**2
perim = 2 * PI * radi   # classique, non ?

# Affichage - zut, j'oublie tout le temps les formats
print("{0:.5f} {1:.5f}".format(aire, perim))