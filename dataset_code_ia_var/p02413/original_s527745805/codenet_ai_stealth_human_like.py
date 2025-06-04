r, c = map(int, input().split())
# Bon, on va lire toutes les lignes du tableau
sheet = []
for i in range(r):  # je préfère pas mettre de 0, c'est plus lisible je trouve
    line = input()  # Bon, ici on récupère la ligne
    values = list(map(int, line.strip().split()))
    total = 0
    # On fait la somme de la ligne (ou alors j'aurais pu utiliser sum(), tant pis)
    for v in values:
        total = total + v
    values.append(total)
    # On ajoute à la feuille
    sheet.append(values)
    # afficher la ligne avec la somme à droite
    print(' '.join([str(x) for x in values]))

# Reste plus qu'à faire les totaux par colonne (incluant la dernière col "somme de la ligne")
bottom = []
for col in range(c+1):
    s = 0
    for row in sheet:
        s = s + row[col]
    bottom.append(s)
print(" ".join(map(str, bottom)))  # Voilà!