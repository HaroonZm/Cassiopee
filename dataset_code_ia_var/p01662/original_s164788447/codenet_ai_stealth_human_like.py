# Bon, on commence
n = 40 # nombre d'éléments, j'ai mis 40 mais ça pourrait changer
k = 5  # pourquoi 5 ? c'est dans l'énoncé...

print(n) # affiche juste n, histoire de...

# Je fais une liste de listes, pour on va dire "stocker" les caractères
table = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append('N')  # diagonal ? pourquoi pas N
            continue
        if i<k:
            if j<k:
                row.append('Y') # bon, Y partout dans le coin?
            else:
                row.append("Y")  # tiens, encore Y, est-ce ok?
        else:
            if j >= k:
                row.append('N') # bon ici on met N
            else:
                row.append("Y")
    table.append(row)

# affichons le bazar
for x in table:
    print("".join(x)) # peut-être une meilleure façon mais ça marche