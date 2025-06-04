n = int(input())
m = int(input())

# Créer la matrice avec de grandes valeurs
K = []
for i in range(32):
    ligne = []
    for j in range(32):
        ligne.append(10**9)
    K.append(ligne)

# Remplir la matrice avec les valeurs données
for i in range(m):
    entree = input().split(",")
    a = int(entree[0])
    b = int(entree[1])
    c = int(entree[2])
    d = int(entree[3])
    K[a][b] = c
    K[b][a] = d

# Appliquer l'algorithme de Floyd-Warshall
for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            if K[i][j] > K[i][k] + K[k][j]:
                K[i][j] = K[i][k] + K[k][j]

# Lire les valeurs finales et imprimer le résultat
valeurs = input().split(",")
s = int(valeurs[0])
g = int(valeurs[1])
V = int(valeurs[2])
P = int(valeurs[3])
resultat = V - P - K[s][g] - K[g][s]
print(resultat)