nombre_de_lignes, ensembles_uniques = int(input()), set()

for _ in range(nombre_de_lignes):
    valeurs_ligne = list(map(int, input().split()))
    valeurs_triees = sorted(valeurs_ligne)
    representation_texte = str(valeurs_triees)
    ensembles_uniques.add(representation_texte)

nombre_groupes_identiques = nombre_de_lignes - len(ensembles_uniques)
print(nombre_groupes_identiques)