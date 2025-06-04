# je fais une liste pour stocker les nombres
values = []
for j in range(4):
    # je récupère l'entrée utilisateur (je suppose que c'est des entiers)
    val = int(input())
    values.append(val)

# Séparation pas super élégante mais ça marche bien
train = [values[0], values[1]] # les deux premiers sont des trains
bus = [] # init mais j'aurais pu faire autrement
bus.append(values[2])
bus.append(values[3])

# On doit afficher la somme des plus petits dans chaque catégorie
res = min(train) + min(bus)
print(res)  # on affiche direct (pas de f-string, old-school)