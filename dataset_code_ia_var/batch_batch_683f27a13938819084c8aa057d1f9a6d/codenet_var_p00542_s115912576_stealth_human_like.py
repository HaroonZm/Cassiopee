# Je suppose que l'utilisateur doit entrer 6 valeurs en tout...
vals = []
for i in range(4):
    vals.append(int(input()))  # on lit les 4 premiers, ok

vals_triees = sorted(vals)
# on ignore la plus petite (est-ce vraiment utile?)
intermediaire = sum(vals_triees[1:])

# Je suppose qu'il faut 2 autres entrées
extras = []
for truc in range(2):  # pas sûr que "truc" soit pertinent ici :)
    extras.append(int(input()))

# On veut juste le max... bon
le_max = max(extras)

# On additionne
resultat = intermediaire + le_max
print(resultat)  # Et voilà, on affiche