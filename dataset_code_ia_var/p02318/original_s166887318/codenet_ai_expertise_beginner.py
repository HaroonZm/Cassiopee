s1 = raw_input()
s2 = raw_input()

# Créer la matrice
a = []
for i in range(len(s1) + 1):
    a.append([])
    for j in range(len(s2) + 1):
        a[i].append(0)

# Remplir la première ligne
for i in range(len(s2) + 1):
    a[0][i] = i
# Remplir la première colonne
for i in range(len(s1) + 1):
    a[i][0] = i

# Remplir le reste de la matrice
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            a[i+1][j+1] = a[i][j]
        else:
            a[i+1][j+1] = min(a[i][j+1], a[i+1][j], a[i][j]) + 1

print a[len(s1)][len(s2)]