r, c = map(int, input().split())
table = []
for _ in range(r):
    line = input().split()
    table.append([int(x) for x in line])
# On ajoute la somme à droite de chaque ligne
for i in range(len(table)):
    s = sum(table[i])
    table[i].append(s)  # Pas très optimisé mais bon...
# Calcul des totaux de colonnes (horizontaux?) + 'total global' à la fin
last_row = []
for j in range(len(table[0])):
    tot = 0
    for i in range(len(table)):
        tot += table[i][j]
    last_row.append(tot)
table.append(last_row)
for row in table:
    print(*row) # j'aime bien le unpacking, même si c'est un peu flou parfois