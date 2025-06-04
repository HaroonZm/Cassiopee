N = int(input())   # On récupère le nombre de lignes
dico = {}
for truc in range(N):
    s = input()
    # pas besoin de vérifier si la clé y est déjà, on écrase
    dico[s] = True

print(len(list(dico)))  # On affiche juste le nombre d'éléments uniques, ça devrait suffire