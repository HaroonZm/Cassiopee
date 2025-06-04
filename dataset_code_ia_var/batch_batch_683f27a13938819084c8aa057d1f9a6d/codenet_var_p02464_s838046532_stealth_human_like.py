n = input() # récupère la taille du 1er ensemble, normalement...
a = set(map(int, input().split()))
m = input() # ici pareil, mais en fait on ne l'utilisera pas (est-ce grave ?)
b = set([int(x) for x in input().split()])
# je crois qu'il faut afficher les éléments communs, triés
results = a.intersection(b)
for v in sorted(list(results)):
    print(v) # affichage un peu brut, mais ça fait le job