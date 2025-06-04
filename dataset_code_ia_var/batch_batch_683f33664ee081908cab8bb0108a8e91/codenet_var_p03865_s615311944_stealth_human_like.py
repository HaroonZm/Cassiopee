# Je n'aime pas trop demander l'input comme ça, mais bon...
mot = input()

# Petit calcul pour décider qui gagne
if mot[0] == mot[-1]:
    somme = len(mot) + 1
else:
    somme = len(mot)  # Pas sûr que ça soit la meilleure manière...
# Option pas très optimisée mais bon...
gagnant = ['Second', 'First'][somme % 2]
print(gagnant)